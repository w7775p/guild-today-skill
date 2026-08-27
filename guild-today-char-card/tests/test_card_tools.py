"""Generic regression fixtures; no live project assets or network access."""
import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("card_tools", ROOT / "scripts/card_tools.py")
card = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = card
SPEC.loader.exec_module(card)
FIELDS = (ROOT / "references/character-card-fields.md").read_text(encoding="utf-8")
TEMPLATE = (ROOT / "assets/character-card-template.md").read_text(encoding="utf-8")


def fixture():
    required, stat_map = card.schema(FIELDS)
    lines = []
    for line in TEMPLATE.splitlines():
        if line.startswith("|") and not card.separator(line):
            cells = card.split_row(line)
            key = cells[0]
            if key in card.STATS:
                value = "SS" if key == "冒险者等级" else "8"
                cells = [key, value, *card.expected_stat(key, value, stat_map)]
            elif key in required:
                cells = [key, "hero_sample" if key == "角色ID" else "泛式测试内容"]
            line = "| " + " | ".join(cells) + " |"
        lines.append(line)
    return "\n".join(lines) + "\n"


class FieldChecks(unittest.TestCase):
    def setUp(self):
        self.text = fixture()

    def errors(self, text, **kwargs):
        return card.check(text, FIELDS, **kwargs)["errors"]

    def test_complete_card(self):
        self.assertEqual(self.errors(self.text), [])

    def test_template_is_unfilled(self):
        self.assertTrue(self.errors(TEMPLATE))

    def test_original_dictionary(self):
        required, values = card.schema(FIELDS)
        self.assertIn("角色ID", required)
        self.assertEqual(set(values), set(card.STATS))
        for name in ("战斗", "调查", "交涉"):
            self.assertEqual(set(values[name]), {str(i) for i in range(11)})
        for value in ("0", "100"):
            self.assertEqual(len(card.expected_stat("声望", value, values)), 2)

    def test_numeric_description_change(self):
        table = next(t for t in card.tables(self.text) if t.rows[0][0] == "项目")
        original = table.rows[1][3]
        self.assertTrue(any("描述与字段原文不一致" in e for e in self.errors(self.text.replace(original, "改写描述", 1))))

    def test_numeric_out_of_range(self):
        changed = self.text.replace("| 战斗 | 8 |", "| 战斗 | 11 |")
        self.assertIn("战斗超出0—10", self.errors(changed))

    def test_rank_out_of_range(self):
        changed = self.text.replace("| 冒险者等级 | SS |", "| 冒险者等级 | Z |")
        self.assertIn("冒险者等级无效", self.errors(changed))

    def test_inference_is_retained(self):
        changed = self.text.replace("| 战斗 | 8 |", "| 战斗 | 8（推测） |")
        result = card.check(changed, FIELDS)
        self.assertEqual(result["errors"], [])
        self.assertTrue(result["warnings"])
        self.assertIn("8（推测）", card.render_notion(changed))

    def test_missing_and_empty_field(self):
        self.assertIn("缺少必填字段：年龄", self.errors(self.text.replace("| 年龄 | 泛式测试内容 |\n", "")))
        self.assertIn("年龄内容为空", self.errors(self.text.replace("| 年龄 | 泛式测试内容 |", "| 年龄 | |")))

    def test_duplicate_field(self):
        changed = self.text.replace("| 年龄 | 泛式测试内容 |", "| 年龄 | 泛式测试内容 |\n| 年龄 | 泛式测试内容 |")
        self.assertTrue(any("年龄重复" in e for e in self.errors(changed)))

    def test_invalid_ids(self):
        for value in ("hero_Sample", "sample", "hero_xxx", "hero_", "hero_a__b"):
            with self.subTest(value=value):
                self.assertTrue(any("角色ID须" in e for e in self.errors(self.text.replace("hero_sample", value))))

    def test_duplicate_pool_id(self):
        self.assertIn("角色ID与提供的角色池重复", self.errors(self.text, pool=["hero_sample"]))

    def test_partial_draft(self):
        text = "| 字段 | 内容 |\n|---|---|\n| 角色ID | hero_sample |\n"
        self.assertEqual(self.errors(text, partial=True), [])
        self.assertTrue(self.errors(text))

    def test_initial_state_alias(self):
        self.assertEqual(self.errors(self.text.replace("| 状态 |", "| 初始状态 |")), [])

    def test_heading_order(self):
        self.assertTrue(any("十模块" in e for e in self.errors(self.text.replace("## 3.基础资料", "## 4.基础资料"))))

    def test_notion_card_check(self):
        self.assertEqual(self.errors(card.render_notion(self.text)), [])


class ConversionChecks(unittest.TestCase):
    def test_divider_is_not_table(self):
        self.assertEqual(card.tables("文字\n\n---\n\n正文\n"), [])

    def test_round_trip(self):
        text = fixture()
        converted = card.render_notion(text)
        self.assertTrue(card.compare(text, converted)["equal"])
        self.assertEqual(card.render_notion(converted), converted)

    def test_inline_content(self):
        text = "| 字段 | 内容 |\n|---|---|\n| 中文 | **文字**、`a|b`、甲\\|乙<br/>后续 &amp; 3 > 2 |\n"
        converted = card.render_notion(text)
        self.assertTrue(card.compare(text, converted)["equal"])
        self.assertIn("甲|乙", converted)
        self.assertIn("3 &gt; 2", converted)

    def test_fenced_table_untouched(self):
        text = "```markdown\n| 字段 | 内容 |\n|---|---|\n| 甲 | 乙 |\n```\n"
        self.assertEqual(card.tables(text), [])
        self.assertEqual(card.render_notion(text), text)

    def test_fenced_code_changes_detected(self):
        self.assertFalse(card.compare("```\n  x\n```", "```\nx\n```")["equal"])
        self.assertFalse(card.compare("```\nx\n\n```", "```\nx\n```")["equal"])

    def test_manual_deletion_detected(self):
        self.assertFalse(card.compare("人工保留句。\n", "")["equal"])
        self.assertFalse(card.compare("候选（推测）", "候选")["equal"])
        self.assertFalse(card.compare("甲\n乙", "乙\n甲")["equal"])

    def test_literal_marks_not_discarded(self):
        self.assertFalse(card.compare("`a**b`", "`ab`")["equal"])

    def test_bad_table_shape(self):
        text = "| 字段 | 内容 |\n|---|---|\n| 甲 | 乙 | 丙 |\n"
        with self.assertRaises(ValueError):
            card.render_notion(text)

    def test_unclosed_code(self):
        with self.assertRaises(ValueError):
            card.split_row("| 甲 | `乙 |")

    def test_unsupported_html(self):
        text = "| 字段 | 内容 |\n|---|---|\n| 甲 | <div>乙</div> |\n"
        with self.assertRaises(ValueError):
            card.render_notion(text)

    def test_unclosed_notion_table(self):
        with self.assertRaises(ValueError):
            card.render_notion("<table>\n<tr><td>甲</td></tr>\n")

    def test_cli_negative_check(self):
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/card_tools.py"), "check", str(ROOT / "assets/character-card-template.md")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 1)
        self.assertIn('"scope": "mechanical"', result.stdout)

    def test_cli_missing_file(self):
        result = subprocess.run([sys.executable, "-B", str(ROOT / "scripts/card_tools.py"), "check", str(ROOT / "tests/does-not-exist.md")], capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('"error"', result.stderr)


if __name__ == "__main__":
    unittest.main()
