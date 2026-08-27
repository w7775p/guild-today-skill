# guild-today-skill

《今日公会照常营业》项目专用 Skill 仓库。

本仓库用于集中维护多个可独立使用、独立迭代的项目 Skill。每个 Skill 占用一个独立目录，目录内保存自己的 `SKILL.md`、references 和后续 examples。

## 仓库结构

```text
guild-today-skill/
├── README.md
├── guild-today-char-card/
│   ├── SKILL.md
│   ├── assets/
│   ├── references/
│   │   ├── character-card-fields.md
│   │   ├── regression-cases.md
│   │   └── source-map.md
│   ├── scripts/
│   └── tests/
└── guild-today-task-card/
    ├── SKILL.md
    └── references/
        ├── role-task-mapping.md
        ├── source-map.md
        ├── task-card-fields.md
        ├── task-design-context.md
        └── task-field-guidance.md
```

## 目录约定

①每个 Skill 使用独立文件夹。

目录名应直接表达 Skill 用途，例如：

```text
guild-today-char-card/
guild-today-task-card/
guild-today-event-card/
```

②每个 Skill 的主入口固定为：

```text
<skill-name>/SKILL.md
```

`SKILL.md` 负责工作方法、执行流程、边界、验收与输出规则。

③与 Skill 一起维护、但不适合复制进主文件的内容放入：

```text
<skill-name>/references/
```

常见内容包括：

```text
source-map.md             # 真源名称、链接与裁决范围
*-fields.md               # 字段口径快照
其他稳定参考资料
```

④已通过真实项目工作验收的范例，后续可以放入：

```text
<skill-name>/examples/
```

examples 应来源于实际完成并确认的项目内容，避免用未经验证的合成范例反向形成错误模板。

## 真源原则

Skill 负责方法，正式真源负责项目事实。

固定 Notion 页面、正式资产、字段口径等信息应通过各 Skill 的 `references/source-map.md` 维护。

随 Skill 保存的字段或规则 reference 属于工作快照。若快照与其指向的当前正式真源冲突，以当前正式真源为准。

旧草案、历史 Demo、旧工作台和淘汰方案默认作为历史资料。只有当前任务明确要求追溯、比较或取材时才进入工作范围。

## Skill 设计原则

①优先解决当前实际任务。

②Skill 管方法、边界和验收，减少重复复制正式策划内容。

③reference 管字段、真源映射和稳定参考资料。

④正式资产管具体事实。

⑤尚未冻结的项目规则保持当前工作状态，不由单个 Skill 擅自冻结。

⑥新增规则应由真实需求触发，避免为了完整性扩展系统。

⑦验收用于确认当前成果满足当前任务，完成直接验收后停止。

## 当前 Skill

### guild-today-char-card

用于创建、补全、修改与审查正式角色卡。

核心方向：

```text
理解设计目的 → 建立人物 → 让人物进入游戏 → 检查实际效果
```

角色字段日常工作优先读取随 Skill 保存的字段快照；需要确认最新口径、处理冲突、涉及尚未冻结规则或维护 reference 时，再读取 source map 指向的当前 Notion 真源。

### guild-today-task-card

用于创建、补全、修改与审查正式 Task，并把当前角色池差异转化为可理解的派遣判断、后台判定和 Result 交接。

核心方向：

```text
任务设计上下文 → 角色映射 → Task → 后台判定 → Result 交接 → 资产依赖
```

Task 字段日常工作优先读取 `task-card-fields.md`；字段使用边界读取 `task-field-guidance.md`。Result、Event、Report、Time 与 Rules 的归属按 `source-map.md` 指向的当前 Notion 真源裁决。

当前 Godot 垂直切片以一张真实任务的生成、派遣、判定、Result、结算与报告闭环为验证目标。暂不为完整性新增 Result / Event / Time Skill。

## 新增 Skill 的最小要求

新 Skill 至少应包含：

```text
<skill-name>/
└── SKILL.md
```

若该 Skill 依赖外部真源或较长的稳定参考资料，再增加：

```text
<skill-name>/references/
```

若已经存在经过真实项目验收的标准范例，再增加：

```text
<skill-name>/examples/
```

不要为了统一目录形式提前创建没有实际内容的文件。
