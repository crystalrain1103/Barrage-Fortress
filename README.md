# 感谢您的下载与游玩！

（伪）狂弹要塞 ***by github@<u>crystalrain1103</u>***

#### 本程序基于python语言，主要依靠pygame库编写

#### （顺带一提，这是作者大一的程设大作业，并且作者大一程设课学的是C语言，因此所有的python语言均为作者仓促自学而成，若源码部分有疏漏及改进点，请不吝向作者提出，在此提前表示感谢！）

#### 以下是对本小游戏的简单介绍：~~（如果您曾经游玩过2022年明日方舟的愚人节活动，您应该对本游戏再熟悉不过了）~~



### 目录：

##### 一、游玩方式简介

##### 二、我方干员图鉴

##### 三、敌方生物图鉴

##### 四、特殊生物图鉴



——————————————————这是分割线————————————————————

##### 一、游玩方式简介：

1.打开本应用程序 `Ciallo～(∠・ω )⌒★.exe` 

 <img src=".\README.assets\pic_step1.png"/>

2.现在您应该看到了本游戏的主菜单：（现版本为alpha测试版）

<img src=".\README.assets\pic_step2.png" />

3.左上角为您**上一局游戏**的**时间**与**分数**。现在，您可以选择三个选项中的其一，~~`settings`正在开发中所以您点击后可以看见弹出**’COMING SOON!'**的对话框~~，点击`quit`后即直接退出，点击`start game`后进入难度选择界面：

<img src=".\README.assets\pic_step3.png" />

4.您可以点击`back`返回，或是选择`PRESENT`,`FUTURE`或是`BEYOND`难度~~（您如果熟悉ACRAEA的话便可一眼看出难度从上到下递增）~~，然后进入正式游戏界面

<img src=".\README.assets\pic_step4.png"/>

5.基本玩法如下：<img src=".\README.assets\pic_step5-1.png"/>

键盘的`W`,`S`,`A`,`D`控制上，下，左，右；`esc`键可以暂停游戏，再次点击`esc`键即可恢复游戏

屏幕左上角分别为**游戏时间**与**游戏分数（目前版本，除BOSS第一阶段外，击杀一名敌人分数 + 1）**

玩家与敌人的**血量条**分别在各自上方，我方发射的子弹为**拳头**，敌方发射的子弹分为**白色**与**红色**两种

其中白色子弹**不可**被我方子弹抵消，红色子弹**可以**被我方子弹抵消

您需要操控左方干员~~（船）~~移动并尽可能地多击杀敌人~~（虽然这不会让您的合成玉变得更多）~~

在这个过程中您需要同时躲避敌人发射的子弹，玩家的判定点在**干员脚底的的蓝色圆圈处**

当游戏时间到达**第一分钟**时**BOSS（上图右下）**会在地图右上角刷新，玩家击败**BOSS第一阶段（上图右下）**与**第二阶段（下图）**后游戏结束，玩家**胜利**；若玩家血量到达0，游戏结束，玩家**失败**。<img src=".\README.assets\pic_step5-2.png" alt="pic_step5-2" style="zoom:50%;" />

6.游戏结束后您会回到**第2步的界面**，之后您可按照前面的指引再次进行游戏或退出。



—————————————————这是分割线—————————————————————

##### 二、我方干员图鉴

<u>断罪者</u>：																	<img src=".\README.assets\staff_conviction.png" alt="staff_conviction" style="zoom:50%;" />

HP：100

DMG：1

tears：0.4

speed：15



——————————————————这是分割线————————————————————

##### 三、敌方生物图鉴：

<u>法术大师A1</u>：															<img src=".\README.assets\enemy_planeA1.png" alt="enemy_planeA1" style="zoom:67%;" />				

HP：10

DMG：1

tears：1

speed：5



<u>寒霜无人机</u>：															<img src=".\README.assets\enemy_planeIce.png" alt="enemy_planeIce" style="zoom: 33%;" />

HP：10

DMG：0

tears：0

speed：5

SKILL：接近时对我方干员造成<u>**寒冷**</u>效果（如右图）<img src=".\README.assets\debuff_cold.png" alt="debuff_cold" style="zoom:50%;" />



**<u>寒冷：干员上方有雪花提示，攻击间隔变为原来的3倍</u>**





<u>“巨大的丑东西”（阶段一）</u>：										<img src=".\README.assets\enemy_boss_stage1.png" alt="enemy_boss_stage1" style="zoom:33%;" />

HP：500

DMG：1（白色子弹）/5（红色子弹）

tears：1

speed：15



<u>“巨大的丑东西”（阶段二）</u>：												<img src=".\README.assets\enemy_boss_stage2.png" alt="enemy_boss_stage2" style="zoom:50%;" />

HP：100

DMG：0

tears：0

speed：25



——————————————————这是分割线————————————————————

##### 四、特殊生物图鉴



<u>BUFF</u>：																								<img src=".\README.assets\special_buff.png" alt="special_buff" style="zoom:50%;" />

**拾取后：攻击间隔变为原来的1/2，攻击变为3连发**



<u>HEAL</u>：																								<img src=".\README.assets\special_heal.png" alt="heal" style="zoom:50%;" />

**拾取后：血量+50/+25/+5（PRESENT/FUTURE/BEYOND难度）**



——————————————————这是分割线————————————————————

##### 附录：不同难度改变的参数：（以下参数按照PRESENT/FUTURE/BEYOND排列）

1.HEAL恢复量：+50/+25/+5

2.HEAL刷新的CD：30/45/60

3.BUFF持续时间：40/35/20

4.BUFF刷新的CD：35/40/30

5.寒霜无人机施加寒冷的范围：150/300/500

6.寒霜无人机刷新的CD：20/15/10

7.法术大师A1刷新的CD：5/5/3

~~8.BGM：Äventyr (Long Ver.)/Äventyr (Long Ver.)/8bit弹雨与断罪之拳 （我觉得这个变化很酷）~~







## THE END 感谢观看！