# Task Design Context

本文件负责建立 Task 创建前的任务设计上下文。

它管理两个内部变量：

`$task_brief`

`$task_design_purpose`

其中 `$task_design_purpose` 始终表示当前 Task 的**任务设计目的**。

---

# 1.$task_brief

`$task_brief` 是用户当前输入中已经确定的任务约束集合。

它可以包含：

```text
task_count
task_name
task_concept
task_design_purpose
specified_characters
preferred_character
preferred_team
task_type
location
client
required_mechanic
risk_direction
information_structure
other_constraints
```

只记录用户已经明确的信息。

用户没有提供的部分由后续流程根据当前项目真源、当前角色池和 Task 字段口径完成。

---

# 2.$task_design_purpose

`$task_design_purpose` 是当前 Task 最终采用的任务设计目的。

它回答：

> 这张任务希望玩家主要进行什么判断，并获得什么任务体验？

它用于指导：

`任务概念`

`角色池利用`

`玩家信息`

`派遣判断`

`后台判定`

`Result 需求`

`最终验收`

---

# 3.用户已经指定任务设计目的

当 `$task_brief.task_design_purpose` 已存在时：

`$task_brief.task_design_purpose → $task_design_purpose`

直接继承用户已经明确的任务设计目的。

然后围绕该目的读取角色池、建立 `$role_task_map` 并完成 Task。

---

# 4.用户留下任务设计目的空间

当 `$task_brief.task_design_purpose` 为空时：

读取当前角色池，寻找能够形成实际派遣判断的人物差异。

然后根据：

`$task_brief`

`当前角色池`

`当前项目阶段`

确定 `$task_design_purpose`。

执行关系：

`$task_brief + 角色池分析 → $task_design_purpose`

随后校准 `$role_task_map` 并继续 Task 设计。

---

# 5.任务约束与任务设计目的

任务名称、指定角色、最佳组合、地点、委托人、任务类型、风险方向等属于任务约束。

任务设计目的负责定义玩家在这张 Task 中主要进行的判断与获得的体验。

例如：

```text
$task_brief.preferred_team = 角色A + 角色B
```

表示用户已经指定一个优先组合。

随后仍需根据正式角色事实确定：

`$task_design_purpose`

以及该组合为什么在当前 Task 中成立。

---

# 6.常见输入模式

## 6.1 用户提供较完整条件

例如：

```text
任务名称：XX
任务设计目的：XXXX
最佳组合：角色A + 角色B
任务概念：XXXX
```

执行：

`提取已明确条件 → 建立 $task_brief → 确定 $task_design_purpose → 读取角色池 → 完成 Task`

## 6.2 用户只提供任务设计目的

执行：

`锁定 $task_design_purpose → 读取角色池 → 建立角色映射 → 完成 Task`

## 6.3 用户只指定角色或组合

执行：

`写入 $task_brief → 读取指定角色与当前角色池 → 确定 $task_design_purpose → 完成 Task`

## 6.4 用户要求角色池驱动生成

例如：

`根据角色池生成若干 Task`

执行：

`读取角色池 → 分析可形成的派遣判断 → 为每张 Task 确定 $task_design_purpose → 分别生成`

## 6.5 用户只提出泛化生成要求

例如：

`生成一个 Task`

执行：

`读取当前项目真源 → 读取角色池 → 选择当前值得验证的人物差异 → 确定 $task_design_purpose → 生成 Task`

用户未指定数量时，默认生成 1 张 Task。

---

# 7.批量生成上下文

用户要求多张 Task 时，为每张 Task 分别建立：

`$task_brief`

`$task_design_purpose`

`$role_task_map`

每张 Task 的核心派遣判断应清楚。

多张 Task 可以从能力、人物行为、关系、状态、信息结构、风险结构、任务目标或其他真实角色差异中形成不同设计。

---

# 8.任务设计目的的验收

检查：

①任务设计目的是否具体到玩家判断与任务体验。

②任务设计目的是否能够由当前角色池和 Task 结构实际实现。

③玩家信息是否支持该判断。

④后台判定与 Result 是否能够反馈该判断。

⑤用户已经明确的任务设计目的是否被完整继承。
