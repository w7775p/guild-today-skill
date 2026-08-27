# Task Design Context

本文件负责建立 Task 创建前的任务设计上下文。

它管理两个内部变量：

`$task_brief`

`$task_design_purpose`

---

# 1.$task_brief

`$task_brief` 是用户当前输入中已经确定的任务约束集合。

它可以包含：

```text
task_count
task_name
task_concept
task_design_purpose
focus_characters
target_best_character
target_best_team
task_type
location
client
required_mechanic
risk_direction
information_structure
other_constraints
```

只记录用户已经明确的信息。

字段含义：

`focus_characters`
→ 用户希望当前 Task 重点考虑的人物。

`target_best_character`
→ 用户明确指定的最佳单角色答案。

`target_best_team`
→ 用户明确指定的最佳组合答案。

其他约束按用户实际输入记录。

---

# 2.$task_design_purpose

`$task_design_purpose` 始终表示当前 Task 的**任务设计目的**。

定义：

> 当前 Task 主要承担或验证的设计作用。

它可以涉及：

`派遣判断`

`角色认识`

`地区或世界表达`

`关系展示`

`任务结构验证`

`系统玩法验证`

`风险与资源取舍`

`其他当前 Task 实际承担的设计作用`

当任务设计目的涉及玩家决策时，同时明确：

`玩家主要判断什么`

`玩家预期获得什么任务体验`

---

# 3.用户已经指定任务设计目的

当 `$task_brief.task_design_purpose` 已存在时：

`$task_brief.task_design_purpose → $task_design_purpose`

直接继承用户已经明确的任务设计目的。

后续角色池分析围绕该目的建立 `$role_task_map`。

---

# 4.用户留下任务设计目的空间

当 `$task_brief.task_design_purpose` 为空时：

结合：

`$task_brief`

`当前角色池`

`当前项目需求`

确定 `$task_design_purpose`。

角色池驱动生成时，可以先寻找值得形成 Task 的人物差异，再确定任务设计目的。

---

# 5.任务约束与任务设计目的

任务名称、重点角色、目标最佳角色、目标最佳组合、地点、委托人、任务类型、风险方向等属于任务约束。

任务设计目的负责定义当前 Task 主要承担或验证的设计作用。

例如：

```text
$task_brief.target_best_team = 角色A + 角色B
```

表示用户已经指定目标最佳组合。

随后需要结合正式角色事实确定：

`$task_design_purpose`

以及该组合为什么在当前 Task 中成立。

---

# 6.默认输入处理

用户可以提供完整 Task 草案、部分条件、单一任务设计目的、指定角色或组合、任务数量，或只提出生成 Task 的要求。

用户未指定数量时：

`task_count = 1`

用户要求多张 Task 时，为每张 Task 分别建立：

`$task_brief`

`$task_design_purpose`

`$role_task_map`

完整执行顺序由 `SKILL.md` 维护。
