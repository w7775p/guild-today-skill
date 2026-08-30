本示例只展示完整角色卡的格式、字段颗粒度与缺项写法，不属于项目角色真源。

**示例角色_角色卡v1**

版本：v1 · 状态：示例 · 更新：2026-08-29

# 1.设计目的

让玩家在可靠的路线能力与暴露高处的停步风险之间作出派遣判断。

# 2.人物

**外貌：** 深棕色短发，风衣下摆沾着干泥，腰间挂着卷起的地图与细绳。

**任务外生活：** 空闲时整理旧地图，吃饭前会先把桌面上的杯子和盘子摆到不会挡路的位置。

# 3.基础资料

<table fit-page-width="true" header-row="true">
<tr>
<td>字段</td>
<td>内容</td>
<td>要求</td>
</tr>
<tr>
<td>角色ID</td>
<td>`hero_sample`</td>
<td>必填</td>
</tr>
<tr>
<td>角色名称</td>
<td>示例角色</td>
<td>必填</td>
</tr>
<tr>
<td>英文名</td>
<td>Sample Character</td>
<td>必填</td>
</tr>
<tr>
<td>年龄</td>
<td>30</td>
<td>必填</td>
</tr>
<tr>
<td>职业</td>
<td>巡林员</td>
<td>必填</td>
</tr>
<tr>
<td>身份</td>
<td>公会登记冒险者；长期负责北侧林道护送。</td>
<td>必填</td>
</tr>
<tr>
<td>简要印象</td>
<td>记路很准，出发前总要先确认退路。</td>
<td>必填</td>
</tr>
<tr>
<td>叙事定位（玩家不可见）</td>
<td>可靠的林道向导；暴露高处会使她中断原定行动。</td>
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
<td>4</td>
<td>哥布林老大</td>
<td>什么？不是长相。</td>
</tr>
<tr>
<td>调查</td>
<td>6</td>
<td>优秀调查员</td>
<td>没什么好说的。</td>
</tr>
<tr>
<td>交涉</td>
<td>4</td>
<td>阅读空气</td>
<td>自己看。</td>
</tr>
<tr>
<td>冒险者等级</td>
<td>C</td>
<td>熟练</td>
<td>有一定专长领域，会被委托人指名。</td>
</tr>
<tr>
<td>声望</td>
<td>23</td>
<td>略有所闻</td>
<td>在本地有一些人听说过这个人的名字，但记不住脸。</td>
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
<td>120G。</td>
<td>必填</td>
</tr>
<tr>
<td>状态</td>
<td>良好。</td>
<td>必填</td>
</tr>
<tr>
<td>公开特质</td>
<td>**①先看退路：** 进入陌生区域前先确认返回路线。<br>**②路标记忆：** 走过一次的道路很少认错。<br>**③少说保证：** 很少承诺绝对安全，只说明自己已经准备了什么。</td>
<td>必填</td>
</tr>
<tr>
<td>是否可派遣</td>
<td>由当前伤势、休息与离队状态生成。</td>
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
<td>暂无。</td>
<td>选填</td>
</tr>
<tr>
<td>弱线索</td>
<td>**①** 她提交的路线图从不标注悬索桥。<br>**②** 高塔护送记录中，她把“绕行两小时”写成了必要路线调整。</td>
<td>选填</td>
</tr>
<tr>
<td>入会记录</td>
<td>三年前以林道向导身份完成登记，此后主要接受护送与搜寻委托。</td>
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
<td>**畏高。** 处于缺少遮挡的高处时，她会把离开当前位置放在原定任务之前。</td>
<td>必填</td>
</tr>
<tr>
<td>触发条件</td>
<td>进入能够清楚看见下方落差、且缺少稳定护栏或锚点的高处。</td>
<td>必填</td>
</tr>
<tr>
<td>抑制条件</td>
<td>提前设置安全绳，并安排一名同行者全程引导。该同行者会被占用，无法同时承担侦查。</td>
<td>必填</td>
</tr>
<tr>
<td>强化条件</td>
<td>隐藏面已经触发后出现强风，或安全绳、锚点受损。</td>
<td>选填</td>
</tr>
<tr>
<td>揭露等级</td>
<td>**未知：** 初始阶段。<br>**怀疑：** 报告连续出现高处绕行与停步记录。<br>**确认：** 同行记录明确说明她因恐惧拒绝继续前进，或她本人承认畏高。</td>
<td>必填</td>
</tr>
<tr>
<td>行为优先级</td>
<td>离开无保护的高处 → 确保队伍有退路 → 保护同行者 → 完成护送 → 自身报酬。</td>
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
<td>把同行者平安带回能够辨认的道路。</td>
<td>必填</td>
</tr>
<tr>
<td>独有行为</td>
<td>每次抵达岔路都会在地图背面记下一个只供自己识别的方向符号。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>派遣前拒绝条件</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>派遣前拒绝表现</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务中违抗条件</td>
<td>玩家明确命令她继续通过暴露的高处；隐藏面已经触发且未被抑制。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务中违抗表现</td>
<td>停在最近的稳定位置，随后退回锚点，无视继续前进的命令。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>违抗后果</td>
<td>队伍行程延误，可能错过限时目标；她与队伍暂时脱离危险区域。具体任务结果由对应任务承接。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>违抗抑制条件</td>
<td>使用里档案中的安全绳与同行引导安排，并承担一个队员无法侦查的代价。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>抑制后状态</td>
<td>继续前进时始终抓住安全绳，说话明显缩短，并反复确认锚点。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>自主行动</td>
<td>没有相关命令时，主动记录岔路、可用水源与撤离路线。</td>
<td>选填</td>
</tr>
<tr>
<td>自主脱离条件</td>
<td>高处锚点失效且现场没有替代保护时，她会退回最近的稳定地面；与明确命令冲突时归入任务中违抗。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>任务后自发行为</td>
<td>任务结束后重新整理路线图，把临时绕行路线补成可复用记录。</td>
<td>选填</td>
</tr>
<tr>
<td>关系触发行为</td>
<td>暂无。</td>
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
<td>暂无。</td>
<td>选填</td>
</tr>
<tr>
<td>争执对象</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执原因</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执触发条件</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执表现</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>争执后果</td>
<td>暂无。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>特殊组合</td>
<td>暂无。</td>
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
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>重伤规则</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>疲劳规则</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>恢复规则</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>永久伤残规则</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>死亡条件</td>
<td>暂无特殊前置或限制。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>永久离队条件</td>
<td>暂无个人特例。</td>
<td>仅特殊角色使用</td>
</tr>
<tr>
<td>关系变化</td>
<td>暂无。</td>
<td>选填</td>
</tr>
<tr>
<td>角色弧线</td>
<td>未设定。</td>
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
<td>林道护送、失踪者搜寻、路线勘察、野外追踪。</td>
<td>必填</td>
</tr>
<tr>
<td>高风险任务类型</td>
<td>高塔、悬崖、悬索桥及其他必须穿越暴露高处的委托。</td>
<td>必填</td>
</tr>
<tr>
<td>可解锁任务</td>
<td>暂无。</td>
<td>选填</td>
</tr>
<tr>
<td>个人事件</td>
<td>暂无。</td>
<td>选填</td>
</tr>
<tr>
<td>特定结果台词</td>
<td>**确认安全路线后：** “这条路能回来。”<br>**畏高确认后：** “我知道路在前面。我走不过去。”</td>
<td>选填</td>
</tr>
<tr>
<td>报告文本风格</td>
<td>路线、时间与地形记录精确；涉及自己的停步时使用“调整路线”“等待保护”等措辞。</td>
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
<td>观察玩家能否从路线记录发现她对高处的回避，并在后续派遣中安排保护成本。</td>
<td>选填</td>
</tr>
<tr>
<td>开发备注</td>
<td>本例只演示字段颗粒度与缺项写法，不进入当前角色池。</td>
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
<td>等待正文确认及结构化授权后生成。</td>
<td>自动生成</td>
</tr>
</table>
