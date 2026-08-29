模板版本：v8.1

本模板用于完整角色卡制作及获授权的统一排版。结构、字段顺序与填写要求依据 Notion《角色卡字段口径》和当前角色池的现行页面格式；使用接口见 `../SKILL.md`。

生成时替换所有提示文字，保留全部64个正式字段。明确没有该项设计时填写“暂无”，尚未决定时填写“待定”或“未设定”，用户指定占位原样保留。
**角色名_角色卡v版本号**

版本：填写当前版本 · 状态：填写当前状态 · 更新：填写实际日期

[返回当前角色池](https://app.notion.com/p/3c87fb71ada48046859dd6319bf6d491)
# 1.设计目的

用一小段说明：这个角色预期带来什么玩家体验，以及怎样影响派遣判断。

# 2.人物

**外貌：** 填写外貌、衣着与辨识特征。

**任务外生活：** 填写日常习惯、兴趣与相处方式。动机、关系和专属行为分别放入对应字段。

# 3.基础资料

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>角色ID</td>
<td>采用 `hero_` 前缀与稳定的小写英文标识。</td>
<td>必填</td>
</tr>
<tr>
<td>角色名称</td>
<td>角色姓名。</td>
<td>必填</td>
</tr>
<tr>
<td>英文名</td>
<td>英文姓名。</td>
<td>必填</td>
</tr>
<tr>
<td>年龄</td>
<td>当前年龄。</td>
<td>必填</td>
</tr>
<tr>
<td>职业</td>
<td>执行任务所依靠的专业能力。</td>
<td>必填</td>
</tr>
<tr>
<td>身份</td>
<td>社会职位、组织归属或法律身份。</td>
<td>必填</td>
</tr>
<tr>
<td>简要印象</td>
<td>玩家初见时的一句话印象。</td>
<td>必填</td>
</tr>
<tr>
<td>叙事定位（玩家不可见）</td>
<td>一句话说明角色在世界或故事中的位置。</td>
<td>必填</td>
</tr>
</table>

# 4.能力与初始状态

以下五项均为必填；简要描述与详细描述按数值逐字取自字段真源。

<table fit-page-width="true" header-row="true">
<tr>
<td>属性</td>
<td>数值</td>
<td>简要描述</td>
<td>详细描述</td>
</tr>
<tr>
<td>战斗</td>
<td>待定</td>
<td>按数值原文填写。</td>
<td>按数值原文填写。</td>
</tr>
<tr>
<td>调查</td>
<td>待定</td>
<td>按数值原文填写。</td>
<td>按数值原文填写。</td>
</tr>
<tr>
<td>交涉</td>
<td>待定</td>
<td>按数值原文填写。</td>
<td>按数值原文填写。</td>
</tr>
<tr>
<td>冒险者等级</td>
<td>待定</td>
<td>按等级原文填写。</td>
<td>按等级原文填写。</td>
</tr>
<tr>
<td>声望</td>
<td>待定</td>
<td>按区间原文填写。</td>
<td>按区间原文填写。</td>
</tr>
</table>

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>个人金币</td>
<td>角色个人持有的金币。</td>
<td>必填</td>
</tr>
<tr>
<td>状态</td>
<td>初始身心状态。</td>
<td>必填</td>
</tr>
<tr>
<td>公开特质</td>
<td>列出2—4条，每条采用“①特质名：行为习惯”。</td>
<td>必填</td>
</tr>
<tr>
<td>是否可派遣</td>
<td>由当前伤势、休息、离队等状态共同决定。</td>
<td>自动生成</td>
</tr>
</table>

声望具体积分保留在后台，玩家看到对应等级描述。

# 5.记载档案

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>公开关系</td>
<td>对象及双方公开承认、或可被第三方确认的关系。</td>
<td>选填</td>
</tr>
<tr>
<td>弱线索</td>
<td>启用时列出2—4条真实但不完整的异常记录。</td>
<td>选填</td>
</tr>
<tr>
<td>入会记录</td>
<td>加入公会的时间与方式，采用中性事实记录。</td>
<td>必填</td>
</tr>
</table>

隐藏信息达到“确认”后，将已确认事实写入本模块；里档案保留后台真源。

# 6.里档案

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>隐藏面</td>
<td>概括词或简短词组＋必要说明。</td>
<td>必填</td>
</tr>
<tr>
<td>触发条件</td>
<td>隐藏面开始影响行为或暴露的具体情境。</td>
<td>必填</td>
</tr>
<tr>
<td>抑制条件</td>
<td>已设计的抑制方式及其代价；没有此项设计写“暂无”。</td>
<td>必填</td>
</tr>
<tr>
<td>强化条件</td>
<td>隐藏面进一步加剧的情境。</td>
<td>选填</td>
</tr>
<tr>
<td>揭露等级</td>
<td>当前阶段，以及进入“怀疑”“确认”阶段的依据。</td>
<td>必填</td>
</tr>
<tr>
<td>行为优先级</td>
<td>按由高到低的顺序排列角色的取舍。</td>
<td>必填</td>
</tr>
</table>

# 7.本色与任务行为

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>核心动机</td>
<td>一句话说明持续驱动角色选择的根本需求。</td>
<td>必填</td>
</tr>
<tr>
<td>独有行为</td>
<td>具有角色辨识度的专属行为。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>派遣前拒绝条件</td>
<td>接受委托前，什么情况会让角色拒绝。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>派遣前拒绝表现</td>
<td>拒绝时的台词或动作；台词可以编造借口。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务中违抗条件</td>
<td>写清被违反的命令与触发情境。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务中违抗表现</td>
<td>角色实际采取的行动。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>违抗后果</td>
<td>对任务、队友、公会或自身的影响。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>违抗抑制条件</td>
<td>玩家能够采取的抑制措施及其代价。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>抑制后状态</td>
<td>成功抑制后残留的心理或行为变化。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>自主行动</td>
<td>没有收到相关命令时，角色主动采取的行动。</td>
<td>选填</td>
</tr>
<tr>
<td>自主脱离条件</td>
<td>角色自行脱离任务的情境。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务后自发行为</td>
<td>任务结束、报告提交后的个人行为。</td>
<td>选填</td>
</tr>
<tr>
<td>关系触发行为</td>
<td>指定对象的何种变化，会引起角色怎样的反应。</td>
<td>仅特殊角色使用</td>
</tr>
</table>

# 8.关系与成长

## ①关系与冲突

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>关键关系摘要</td>
<td>对角色选择有重要影响的关系，可包含隐藏或单向关系。</td>
<td>选填</td>
</tr>
<tr>
<td>争执对象</td>
<td>对象姓名及角色ID。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执原因</td>
<td>双方冲突的利益、价值观或历史原因。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执触发条件</td>
<td>冲突实际发生的情境。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执表现</td>
<td>玩家可见或报告可知的言行。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执后果</td>
<td>对任务、关系、状态或后续派遣的影响。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>特殊组合</td>
<td>指定角色共同出勤或同队时的专属效果。</td>
<td>仅特殊角色使用</td>
</tr>
</table>

## ②状态、风险与成长

以下状态规则只填写角色特例，通用规则由公共系统维护。

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>轻伤规则</td>
<td>轻伤时的专属变化。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>重伤规则</td>
<td>重伤时的专属变化。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>疲劳规则</td>
<td>疲劳积累或影响的个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>恢复规则</td>
<td>特殊恢复方式、时间或条件。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>永久伤残规则</td>
<td>获得永久伤残的条件及变化。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>死亡条件</td>
<td>通用任务结果之外的特殊死亡条件或限制。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>永久离队条件</td>
<td>角色特有的永久退出条件。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>关系变化</td>
<td>对象、触发事件与关系变化。</td>
<td>选填</td>
</tr>
<tr>
<td>角色弧线</td>
<td>人物主线、心理或价值观的变化方向与关键节点，简要说明。</td>
<td>选填</td>
</tr>
</table>

# 9.任务复用接口

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>适配任务类型</td>
<td>能发挥角色优势的任务类别。</td>
<td>必填</td>
</tr>
<tr>
<td>高风险任务类型</td>
<td>容易引发角色风险的任务类别。</td>
<td>必填</td>
</tr>
<tr>
<td>可解锁任务</td>
<td>任务引用、概要与解锁意图。</td>
<td>选填</td>
</tr>
<tr>
<td>个人事件</td>
<td>事件引用、概要与触发意图。</td>
<td>选填</td>
</tr>
<tr>
<td>特定结果台词</td>
<td>触发情境＋对应台词。</td>
<td>选填</td>
</tr>
<tr>
<td>报告文本风格</td>
<td>稳定的措辞、称呼、句式与信息表达习惯。</td>
<td>选填</td>
</tr>
</table>

任务、事件建立独立资产后，完整正文由所属资产维护。

# 10.设计说明

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>测试目的</td>
<td>要验证的玩法假设，以及希望观察到的玩家选择。</td>
<td>选填</td>
</tr>
<tr>
<td>开发备注</td>
<td>实现时需要注意的跨系统依赖或风险。</td>
<td>选填</td>
</tr>
</table>

## 程序字段

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>程序字段</td>
<td>正文确认且获得结构化授权后生成；当前保留此位置。</td>
<td>自动生成</td>
</tr>
</table>
