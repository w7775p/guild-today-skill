# 《今日公会照常营业》Task Skill 真源映射

本文件定义正式信息来源、裁决范围与读取时机。

---

# 1.当前项目真源

URL：

`https://app.notion.com/p/3bb7fb71ada4814888f9ea8e28e501d4`

负责：

`核心游戏循环`

`Task 与 Result 设计原则`

`人物与世界表达原则`

`项目当前阶段`

`当前验证重点`

`项目级已确认事项`

`项目级待定事项`

Task 创建时读取。

---

# 2.任务卡

URL：

`https://app.notion.com/p/3bb7fb71ada481a0a31ccdbdd6a8b0d4`

负责：

`Task 字段名称`

`字段定义`

`字段顺序`

`玩家可见性`

`填写要求`

`生命周期字段`

`后台判定字段`

`资产连接字段`

正常字段工作优先读取：

`references/task-card-fields.md`

需要确认最新字段、处理冲突或维护快照时读取当前 Notion 页面。

---

# 3.当前角色池

URL：

`https://app.notion.com/p/3c87fb71ada48046859dd6319bf6d491`

负责当前所有已确定的正式角色事实。

包括：

`能力`

`职业`

`经历`

`状态`

`公开特质`

`关系`

`行为`

`特殊规则`

`特殊组合`

`其他正式人物事实`

Task 创建时读取。

具体角色参与当前 Task 时，读取对应完整正式角色卡。

---

# 4.角色卡字段口径

URL：

`https://app.notion.com/p/3bb7fb71ada4813d90b0cc063c729d71`

负责：

`Character 字段定义`

`角色行为字段`

`角色关系字段`

`角色程序字段边界`

需要解释角色字段语义或处理字段冲突时读取。

---

# 5.guild-today-char-card

仓库路径：

`guild-today-char-card/`

负责角色创建、补全、修改与审查的方法。

Task Skill 使用已经确认的正式 Character 结果。

---

# 6.结果组卡

URL：

`https://app.notion.com/p/3bb7fb71ada4818ca933f542b5054bbb`

负责：

`Result Group 字段`

`Result 字段`

`结果条件`

`结果事实`

`公会变化`

`角色变化`

`关系变化`

`情报 / 档案变化`

`状态 / Flag`

`后续资产`

进入 Result 交接或需要解释 Result 字段时读取。

---

# 7.事件卡

URL：

`https://app.notion.com/p/3bb7fb71ada4812e8207ef2bdb7247b6`

负责：

`Event 字段`

`触发时机`

`触发条件`

`事件正文`

`玩家选择`

`角色反应`

`情报揭露`

`结果影响`

`后续资产`

当前 Task 出现独立过程内容依赖时读取。

---

# 8.报告与情报揭露系统

负责：

`报告职责`

`玩家最终收到的信息`

`情报揭露状态`

`Result / Event / Character 与 Report 的接口`

当前 Task 需要明确报告依赖时读取。

---

# 9.时间卡

URL：

`https://app.notion.com/p/3bb7fb71ada48168802dd5099592707b`

负责：

`特殊时间节点`

`特殊周期`

`固定触发资产`

`固定世界变化`

当前 Task 涉及特殊时间节点、固定时间触发或特殊周期时读取。

---

# 10.规则表

URL：

`https://app.notion.com/p/3bb7fb71ada481078959df3e3b0f82e4`

负责：

`公共条件`

`状态`

`Flag`

`优先级`

`随机`

`权重`

`隐藏信息公共规则`

`公共生命周期`

`资产归属`

当前 Task 涉及跨资产公共执行语义时读取。

---

# 11.冲突裁决

按领域确定裁决来源：

`项目级结论 → 当前项目真源`

`Task 字段 → 任务卡`

`具体 Task → 对应正式 Task`

`Character 字段 → 角色卡字段口径`

`Character 事实 → 当前角色池 / 对应正式角色卡`

`Result → 结果组卡 / 对应正式 Result`

`Event → 事件卡 / 对应正式 Event`

`Report → 报告与情报揭露系统`

`Time → 时间卡`

`公共规则 → 规则表`

用户当前明确决定作为当前任务最新事实。
