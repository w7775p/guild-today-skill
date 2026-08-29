#!/usr/bin/env python3
"""Read-only card checks and conservative Markdown/Notion table conversion."""
import argparse
from collections import Counter
from dataclasses import dataclass
import html
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FIELDS = ROOT / "references" / "character-card-fields.md"
ID_RE = re.compile(r"hero_[a-z][a-z0-9]*(?:_[a-z0-9]+)*\Z")
MODULES = (
    "设计目的", "人物", "基础资料", "能力与初始状态", "记载档案",
    "里档案", "本色与任务行为", "关系与成长", "任务复用接口", "设计说明",
)
STATS = ("战斗", "调查", "交涉", "冒险者等级", "声望")
UNCONFIRMED = {"待定", "未设定", "占位"}
FACET_FIELDS = ("公开特质", "弱线索")


@dataclass
class Table:
    start: int
    end: int
    rows: list
    kind: str


def split_row(line):
    line = line.strip()
    if not (line.startswith("|") and line.endswith("|")):
        raise ValueError("Markdown 表格须使用首尾竖线")
    cells, current, code, i = [], [], 0, 1
    while i < len(line) - 1:
        char = line[i]
        if char == "\\" and i + 1 < len(line) - 1:
            following = line[i + 1]
            if following in ("|", "\\"):
                current.append(following)
            else:
                current.extend((char, following))
            i += 2
            continue
        if char == chr(96):
            end = i
            while end < len(line) - 1 and line[end] == chr(96):
                end += 1
            length = end - i
            code = 0 if code == length else (length if code == 0 else code)
            current.append(line[i:end])
            i = end
            continue
        if char == "|" and code == 0:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(char)
        i += 1
    if code:
        raise ValueError("表格单元格中的行内代码未闭合")
    cells.append("".join(current).strip())
    return cells


def separator(line):
    if "|" not in line:
        return False
    stripped = line.strip().strip("|").strip()
    return bool(stripped) and all(
        re.fullmatch(r":?-{3,}:?", cell.strip())
        for cell in stripped.split("|")
    )


def check_cell(cell):
    # These are the only HTML-like inline forms this small renderer supports.
    remainder = re.sub(r"<br\s*/?>", "", cell, flags=re.I)
    if re.search(r"</?[A-Za-z][^>]*>", remainder):
        raise ValueError("表格含不支持的 HTML/块结构；请使用纯文本或 Markdown 行内格式")


def notion_rows(block):
    if not re.fullmatch(r"<table\b[^>]*>[\s\S]*</table>", block.strip()):
        raise ValueError("Notion 表格边界不完整")
    inner = re.sub(r"^<table\b[^>]*>|</table>$", "", block.strip())
    row_blocks = list(re.finditer(r"<tr\b[^>]*>([\s\S]*?)</tr>", inner))
    if re.sub(r"<tr\b[^>]*>[\s\S]*?</tr>", "", inner).strip():
        raise ValueError("不支持的 Notion 表格子结构")
    rows = []
    for match in row_blocks:
        row = match.group(1)
        cells = re.findall(r"<td\b[^>]*>([\s\S]*?)</td>", row)
        if not cells or re.sub(r"<td\b[^>]*>[\s\S]*?</td>", "", row).strip():
            raise ValueError("Notion 表格行不完整")
        for cell in cells:
            check_cell(cell)
        rows.append([html.unescape(cell.strip()) for cell in cells])
    return rows


def tables(text):
    lines = text.splitlines(keepends=True)
    offsets, at = [], 0
    for line in lines:
        offsets.append(at)
        at += len(line)
    found, fence, i = [], None, 0
    while i < len(lines):
        stripped = lines[i].strip()
        marker = re.match(r"^(\x60{3,}|~{3,})", stripped)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1]:
                fence = None
            i += 1
            continue
        if fence:
            i += 1
            continue
        if stripped.startswith("<table"):
            j = i
            while j < len(lines) and "</table>" not in lines[j]:
                j += 1
            if j == len(lines):
                raise ValueError("Notion 表格没有闭合")
            block = "".join(lines[i:j + 1])
            rows = notion_rows(block)
            end = offsets[j] + len(lines[j])
            found.append(Table(offsets[i], end, rows, "notion"))
            i = j + 1
            continue
        if i + 1 < len(lines) and separator(lines[i + 1]):
            rows = [split_row(lines[i])]
            delimiter = split_row(lines[i + 1])
            if len(delimiter) != len(rows[0]):
                raise ValueError("表格表头与分隔行列数不同")
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                rows.append(split_row(lines[j]))
                j += 1
            for row in rows:
                for cell in row:
                    check_cell(cell)
            end = offsets[j] if j < len(lines) else len(text)
            found.append(Table(offsets[i], end, rows, "markdown"))
            i = j
            continue
        i += 1
    for table in found:
        if len(table.rows) < 2 or any(
            len(row) != len(table.rows[0]) for row in table.rows
        ):
            raise ValueError("表格缺少数据行或列数不一致")
    return found


def plain(value):
    value = html.unescape(value).replace("**", "").replace(chr(96), "")
    return re.sub(r"\\([_*])", r"\1", value).strip()


def field_requirements(fields_text):
    """Return formal fields and their content requirements; exclude reference rows."""
    kinds = {"必填", "选填", "仅特殊角色使用", "自动生成（非手填）"}
    return {
        row[1]: row[-1]
        for table in tables(fields_text)
        if table.rows[0][:2] == ["模块", "字段名"]
        for row in table.rows[1:]
        if len(row) == 7 and row[-1] in kinds
    }


def schema(fields_text):
    required = {key for key, kind in field_requirements(fields_text).items() if kind == "必填"}
    stat_map = {}
    for table in tables(fields_text):
        heading = list(re.finditer(
            r"^#{2,6}\s+(.+?)\s*$", fields_text[:table.start], flags=re.M
        ))
        if not heading:
            continue
        name = plain(heading[-1].group(1))
        if name == "声望等级":
            name = "声望"
        if name in STATS and plain(table.rows[0][-1]) == "详细描述":
            stat_map[name] = {row[0]: tuple(row[1:]) for row in table.rows[1:]}
    if not required or set(stat_map) != set(STATS):
        raise ValueError("字段快照缺少必填字段或完整数值表")
    return required, stat_map


def expected_stat(name, value, stat_map):
    value = re.sub(r"（推测）[。.]?$", "", plain(value)).strip()
    if name == "冒险者等级":
        if value not in stat_map[name]:
            raise ValueError("冒险者等级无效")
        return stat_map[name][value]
    if not re.fullmatch(r"\d+", value):
        raise ValueError(name + "须为整数")
    number = int(value)
    if name == "声望":
        for interval, descriptions in stat_map[name].items():
            low, high = map(int, interval.split("-"))
            if low <= number <= high:
                return descriptions
        raise ValueError("声望超出0—100")
    if str(number) not in stat_map[name]:
        raise ValueError(name + "超出0—10")
    return stat_map[name][str(number)]


def unconfirmed(value, placeholders=()):
    value = plain(value)
    without_marker = re.sub(r"（推测）[。.]?$", "", value).strip().rstrip("。.")
    return without_marker in UNCONFIRMED or value in set(map(plain, placeholders))


def facet_errors(key, value, placeholders=()):
    """Count explicit entries only; distinct meaning still needs prose review."""
    if key not in FACET_FIELDS:
        return []
    value = re.sub(r"<br\s*/?>", "\n", plain(value), flags=re.I)
    if key == "弱线索" and (value == "暂无" or unconfirmed(value, placeholders)):
        return []
    markers = list(re.finditer(r"[①-⑳]|^(?:\d+[.、)）]\s*|[-+*]\s+)", value, flags=re.M))
    if markers:
        ends = [marker.start() for marker in markers[1:]] + [len(value)]
        entries = [value[marker.end():end].strip() for marker, end in zip(markers, ends)]
    else:
        entries = [value]
    entries = [entry for entry in entries if entry and entry != "暂无" and not unconfirmed(entry, placeholders)]
    errors = []
    if not 2 <= len(entries) <= 4:
        errors.append(f"{key}须有2—4条独立内容，当前{len(entries)}条；单条视为失败")
    if len(set(entries)) != len(entries):
        errors.append(key + "存在完全重复条目，不能凑数；请审查人物侧面的独立性")
    return errors


def prose_fields(text, parsed=None):
    parsed = tables(text) if parsed is None else parsed
    outside, cursor = [], 0
    for table in parsed:
        outside.append(text[cursor:table.start])
        cursor = table.end
    outside.append(text[cursor:])
    fence, pending, content = None, None, []
    # A removed table remains a boundary for any preceding prose field.
    for line in "\n---\n".join(outside).splitlines():
        marker = re.match(r"^\s*(\x60{3,}|~{3,})", line)
        if marker:
            run = marker.group(1)
            if fence is None:
                fence = (run[0], len(run))
            elif run[0] == fence[0] and len(run) >= fence[1]:
                fence = None
            continue
        if fence:
            continue
        match = re.match(r"^\*\*([^：:*]+)(?:[：:]\*\*|\*\*[：:])\s*(.*)$", line)
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        facet_label = re.fullmatch(r"\*\*(公开特质|弱线索)\*\*\s*", line)
        boundary = match or heading or facet_label or re.fullmatch(r"\s*(?:---+|\*\*\*+|___+)\s*", line)
        if pending and boundary:
            yield pending, "\n".join(content)
            pending, content = None, []
        if match:
            key, value = match.groups()
        elif facet_label:
            key, value = facet_label.group(1), ""
        elif heading and plain(heading.group(1)).rstrip("：:") in FACET_FIELDS:
            key, value = plain(heading.group(1)).rstrip("：:"), ""
        else:
            if pending:
                content.append(line)
            continue
        if key in FACET_FIELDS:
            pending, content = key, [value]
        else:
            yield "状态" if key == "初始状态" else key, value
    if pending:
        yield pending, "\n".join(content)


def field_columns(table):
    headers = list(map(plain, table.rows[0]))
    if headers in (["字段", "填写要求", "内容"], ["字段", "要求", "内容"]):
        return 2, 1
    if headers in (["字段", "内容", "填写要求"], ["字段", "内容", "要求"]):
        return 1, 2
    if len(headers) == 2:
        return 1, None
    return None, None


def field_content_index(table):
    return field_columns(table)[0]


def card_id(text, parsed=None):
    parsed = tables(text) if parsed is None else parsed
    for table in parsed:
        index = field_content_index(table)
        for row in table.rows[1:]:
            if plain(row[0]) == "角色ID" and index is not None:
                return plain(row[index])
    for key, value in prose_fields(text, parsed):
        if key == "角色ID":
            return plain(value)
    return None


def check(text, fields_text, partial=False, pool=(), preserve_layout=False, placeholders=()):
    required, stat_map = schema(fields_text)
    definitions = field_requirements(fields_text)
    errors, warnings, seen = [], [], Counter()
    parsed = tables(text)
    for table in parsed:
        for row in table.rows[1:]:
            key = plain(row[0])
            if key == "初始状态":
                key = "状态"
            if key not in definitions:
                continue
            seen[key] += 1
            if key in STATS and len(row) != 4:
                errors.append(key + "须包含数值、简要描述、详细描述")
                continue
            index = 1 if key in STATS else field_content_index(table)
            if index is None:
                errors.append(key + "的字段表格格式未覆盖；请使用字段／内容或含要求列的三列表格")
                continue
            value = row[index]
            if not plain(value):
                errors.append(key + "内容为空")
            elif key not in STATS and unconfirmed(value, placeholders):
                warnings.append(key + "尚未确认")
            _, requirement_index = field_columns(table)
            if requirement_index is not None:
                kind = plain(row[requirement_index])
                expected_kind = definitions[key]
                if kind != expected_kind and not (kind == "自动生成" and expected_kind == "自动生成（非手填）"):
                    errors.append(key + "填写要求与字段原文不一致")
            errors.extend(facet_errors(key, value, placeholders))
            if key in STATS:
                try:
                    expected = expected_stat(key, row[1], stat_map)
                except ValueError as exc:
                    if unconfirmed(row[1], placeholders):
                        warnings.append(key + "尚未确认")
                    else:
                        errors.append(str(exc))
                    continue
                if tuple(map(plain, row[2:])) != expected:
                    errors.append(key + "描述与字段原文不一致")
    # Explicit prose fields get presence checks; stat prose is not silently accepted.
    for key, value in prose_fields(text, parsed):
        if key in definitions:
            seen[key] += 1
            if not plain(value):
                errors.append(key + "内容为空")
            elif unconfirmed(value, placeholders):
                warnings.append(key + "尚未确认")
        if key in STATS:
            errors.append(key + "的文字标签格式未覆盖；数值与原文校验仅支持四列表格，请人工核对")
        errors.extend(facet_errors(key, value, placeholders))
    for key, count in seen.items():
        if count > 1:
            errors.append(key + "重复出现，请核对主要定义")
    if not partial:
        for key in sorted(set(definitions) - set(seen)):
            prefix = "缺少必填字段：" if key in required else "缺少正式字段："
            errors.append(prefix + key)
    if not partial and not preserve_layout:
        headings = re.findall(r"^#{1,3} (\d+)\.\s*(.+?)\s*$", text, flags=re.M)
        expected_headings = [(str(i), title) for i, title in enumerate(MODULES, 1)]
        if headings != expected_headings:
            errors.append("完整新卡的十模块标题或顺序不符")
    identity = card_id(text, parsed)
    if identity is not None:
        if not ID_RE.fullmatch(identity) or identity in {"hero_xxx", "hero_placeholder"}:
            errors.append("角色ID须采用有效的 hero_xxx 格式并替换占位后缀")
        if identity in pool:
            errors.append("角色ID与提供的角色池重复")
    elif not partial:
        errors.append("未取得角色ID")
    if "（推测）" in text:
        warnings.append("包含推测项；本检查不确认其设定")
    if "待定" in text:
        warnings.append("包含待定项")
    return {"scope": "mechanical", "errors": errors, "warnings": warnings}


def encode_cell(cell):
    parts = re.split(r"(<br\s*/?>)", cell, flags=re.I)
    return "".join(
        "<br>" if re.fullmatch(r"<br\s*/?>", part, flags=re.I)
        else html.escape(part, quote=False)
        for part in parts
    )


def render_notion(text):
    result, cursor = [], 0
    for table in tables(text):
        result.append(text[cursor:table.start])
        if table.kind == "notion":
            result.append(text[table.start:table.end])
        else:
            rows = [
                "<tr>\n" + "\n".join("<td>" + encode_cell(c) + "</td>" for c in row) + "\n</tr>"
                for row in table.rows
            ]
            result.append(
                '<table fit-page-width="true" header-row="true">\n'
                + "\n".join(rows) + "\n</table>\n"
            )
        cursor = table.end
    result.append(text[cursor:])
    return "".join(result)


def normalize_inline(value):
    return re.sub(r"<br\s*/?>", "<br>", value.strip(), flags=re.I)


def content_tokens(text):
    tokens, cursor = [], 0

    def outside(block):
        fence = None
        for line in block.splitlines():
            marker = re.match(r"^\s*(\x60{3,}|~{3,})", line)
            if marker:
                run = marker.group(1)
                if fence is None:
                    fence = (run[0], len(run))
                elif run[0] == fence[0] and len(run) >= fence[1]:
                    fence = None
                tokens.append(("code", line))
                continue
            if fence:
                tokens.append(("code", line))
                continue
            line = line.strip()
            if not line or line == "---":
                continue
            line = re.sub(r"^#{1,6}\s+", "", line)
            tokens.append(("text", normalize_inline(line)))

    for table in tables(text):
        outside(text[cursor:table.start])
        for row in table.rows:
            tokens.append(("row", tuple(normalize_inline(c) for c in row)))
        cursor = table.end
    outside(text[cursor:])
    return tokens


def compare(before, after):
    old, new = content_tokens(before), content_tokens(after)
    mismatch = next(
        (i for i, pair in enumerate(zip(old, new)) if pair[0] != pair[1]),
        min(len(old), len(new)) if len(old) != len(new) else None,
    )
    return {"equal": mismatch is None, "first_difference": mismatch}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    check_parser = sub.add_parser("check")
    check_parser.add_argument("card", type=Path)
    check_parser.add_argument("--fields", type=Path, default=DEFAULT_FIELDS)
    check_parser.add_argument("--partial", action="store_true")
    check_parser.add_argument("--preserve-layout", action="store_true", help="保留人工标题，仍检查完整字段")
    check_parser.add_argument("--placeholder", action="append", default=[], help="用户明确指定的未定占位文本，可重复传入")
    check_parser.add_argument("--pool", type=Path, nargs="*", default=[])
    render_parser = sub.add_parser("render-notion")
    render_parser.add_argument("card", type=Path)
    compare_parser = sub.add_parser("compare")
    compare_parser.add_argument("before", type=Path)
    compare_parser.add_argument("after", type=Path)
    args = parser.parse_args()
    read = lambda path: path.read_text(encoding="utf-8")
    try:
        if args.command == "render-notion":
            sys.stdout.write(render_notion(read(args.card)))
            return 0
        if args.command == "compare":
            result = compare(read(args.before), read(args.after))
            print(json.dumps(result, ensure_ascii=False))
            return 0 if result["equal"] else 1
        result = check(
            read(args.card), read(args.fields), args.partial,
            [card_id(read(path)) for path in args.pool],
            preserve_layout=args.preserve_layout, placeholders=args.placeholder,
        )
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if result["errors"] else 0
    except (OSError, ValueError) as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
