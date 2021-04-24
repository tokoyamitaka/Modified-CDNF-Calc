from PublicReference.base import *

# 2020.6.20 数据有待修整
# 2020.6.22 全部使用回归方程，捷影步段数改为5段，修正枪刃乱舞护石算法
#           轮盘连射取非抓取，大回旋坠斩护石跳跃暂不考虑，致命焰火取后方射击
#           剑刃突刺、回旋飞剑实战中会因位置原因丢失段数
#           潜行射击段数随攻速加快而减少，取12段
#           全方位护石游戏内会吃同时释放的其他技能的判定导致伤害显示偏高
# 2020.8.13 添加轮盘连射，大回旋坠斩，致命焰火选项
#           添加韩服新护石
# 2020.8.20 修正碧波瞬斩护石提升

# 武器长刀
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '长刀':
#             return round(self.CD / self.恢复 * 1.05, 1)


# 长刀精通
class 铁血统帅技能0(被动技能):
    名称 = '长刀精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.95


# 暗刃战略
class 铁血统帅技能1(被动技能):
    名称 = '暗刃战略'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)


# 一觉被动
class 铁血统帅技能2(被动技能):
    名称 = 'B.G枪刃改造'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


# 二觉被动
class 铁血统帅技能3(被动技能):
    名称 = 'B.C精锐特训'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 卓越之力
class 铁血统帅技能4(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 超卓之心
class 铁血统帅技能5(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


# 觉醒之抉择
class 铁血统帅技能6(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


# 掩护射击
class 铁血统帅技能7(主动技能):
    名称 = '掩护射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 10
    基础 = 1847.755698 - 攻击段数 * 0.5
    成长 = 209.2273524
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 捷影步
class 铁血统帅技能8(主动技能):
    名称 = '捷影步'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 5
    基础 = 1658.836937
    成长 = 187.6461134
    CD = 5
    TP成长 = 0.10
    TP上限 = 5


# 轮盘连射
class 铁血统帅技能9(主动技能):
    名称 = '轮盘连射'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1332.874675
    成长 = 150.5275803
    攻击次数 = 1

    基础2 = 1696.315584  # 下劈
    成长2 = 191.5866712
    攻击次数2 = 1

    基础3 = 191.5866712  # 射击
    成长3 = 22.58072454
    攻击次数3 = 0  # 10

    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 剑刃突刺
class 铁血统帅技能10(主动技能):
    名称 = '剑刃突刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    攻击段数 = 8
    基础 = 2270.46039 - 攻击段数 * 0.5
    成长 = 258.1335954
    CD = 6
    TP成长 = 0.10
    TP上限 = 5


# 潜行射击
class 铁血统帅技能11(主动技能):
    名称 = '潜行射击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 15
    基础 = (2709.696017 - 攻击段数 * 0.5) * 0.8
    成长 = 307.081761 * 0.8  # 游戏中攻速越高攻击段数越低，取本人60%-90%攻速时大致为12/15
    CD = 7
    TP成长 = 0.10
    TP上限 = 5


# 利刃旋斩
class 铁血统帅技能12(主动技能):
    名称 = '利刃旋斩'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    攻击段数 = 8
    基础 = 2730.212439 - 攻击段数 * 0.5
    成长 = 308.7161807
    CD = 7
    TP成长 = 0.10
    TP上限 = 5


# 游弹枪袭
class 铁血统帅技能13(主动技能):
    名称 = '游弹枪袭'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    攻击段数 = 30
    基础 = 3624.235294 - 攻击段数 * 0.5
    成长 = 411.4886878
    CD = 8
    TP成长 = 0.10
    TP上限 = 5


# 全方位射击
class 铁血统帅技能14(主动技能):
    名称 = '全方位射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    基础 = 253.6930612 - 0.5
    成长 = 28.71635054
    攻击次数 = 15

    基础2 = 423.2865306 - 0.5
    成长2 = 47.85935174
    攻击次数2 = 6

    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.倍率 = self.倍率 * 1.27 * 1.07
            self.CD *= 0.95
        elif x == 1:
            self.攻击次数2 = 0
            self.攻击次数 = 20
            self.倍率 = self.倍率 * 1.27 * 1.16  # 改动位置
            self.CD *= 0.95


# 回旋飞剑
class 铁血统帅技能15(主动技能):
    名称 = '回旋飞剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    攻击段数 = 14
    基础 = 7642.573878 + 攻击段数 * 0.5
    成长 = 863.4943577
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 枪刃乱舞
class 铁血统帅技能16(主动技能):
    名称 = '枪刃乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 285.9777983 - 0.5
    成长 = 32.3413506
    攻击次数 = 10

    基础2 = 197.4236818 - 0.5
    成长2 = 22.34227567
    攻击次数2 = 15

    基础3 = 3738.310823 - 0.5
    成长3 = 422.1492831
    攻击次数3 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.80  # 加算
            self.攻击次数3 *= 1.27
            self.攻击次数 *= 1.07
            self.攻击次数2 *= 1.07
        elif x == 1:
            self.CD *= 0.80  # 加算
            self.攻击次数3 *= 1.50  # 改动位置
            self.攻击次数 *= 1.07
            self.攻击次数2 *= 1.07


# 血光斩
class 铁血统帅技能17(主动技能):
    名称 = '血光斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    攻击段数 = 1
    基础 = 14496.06087 - 0.5
    成长 = 1636.743941
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.25  # 加算
        elif x == 1:
            self.倍率 *= 1.33  # 加算   改动位置


# 一觉
class 铁血统帅技能18(主动技能):
    名称 = '电光飞掠'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    攻击段数 = 29
    基础 = 34891.02857 - 攻击段数 * 0.5
    成长 = 10539.71429
    CD = 145


# 近敌灭杀
class 铁血统帅技能19(主动技能):
    名称 = '近敌灭杀'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 5288.051613 - 0.5
    成长 = 597.1358871
    攻击次数 = 1

    基础2 = 396.1870968 - 0.5
    成长2 = 44.7766129
    攻击次数2 = 20

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.85
            self.攻击次数2 *= (1 + 0.35 * 1.2)
        elif x == 1:
            self.CD *= 0.85
            self.攻击次数2 *= (1 + 0.35 * 1.58)  # 改动位置


# 大回旋坠斩，护石暂不考虑跳跃
#   2020.8.13新增护石跳
class 铁血统帅技能20(主动技能):
    名称 = '大回旋坠斩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    基础 = 795.9230769 + 832.6695157 - 1
    成长 = 90.02136752 + 94.03418803
    攻击次数 = 10

    基础2 = 6902.951567 - 0.5
    成长2 = 779.4108669
    攻击次数2 = 1

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1
            self.倍率 *= 1.16
        elif x == 1:
            self.攻击次数 += 1
            self.倍率 *= 1.23  # 改动位置


# 致命焰火
class 铁血统帅技能21(主动技能):
    名称 = '致命焰火'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16

    基础 = 1529.956522
    成长 = 172.7934783
    攻击次数 = 10

    基础2 = 1532.086957  # 后方
    成长2 = 172.923913
    攻击次数2 = 15

    基础3 = 2294.980237  # 原地
    成长3 = 259.215415
    攻击次数3 = 0  # 10

    CD = 40

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.基础2 = self.基础3
            self.成长2 = self.成长3
            self.攻击次数2 = 10  # 猜测，否则提升过高
            self.倍率 *= 1.3
            self.CD *= 0.90


# 碧波瞬斩
class 铁血统帅技能22(主动技能):
    名称 = '碧波瞬斩'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    攻击次数 = 3
    基础 = 15133.18947
    成长 = 1708.524812
    CD = 50

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 1
            self.倍率 *= 4.11  # 2.51*1.6


# 二觉
class 铁血统帅技能23(主动技能):
    名称 = '集结·暮光之翼'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    攻击段数 = 36
    基础 = 81504.02778 - 攻击段数 * 0.5
    成长 = 24603.08333
    CD = 180


铁血统帅技能列表 = []
i = 0
while i >= 0:
    try:
        exec('铁血统帅技能列表.append(铁血统帅技能' + str(i) + '())')
        i += 1
    except:
        i = -1

铁血统帅技能序号 = dict()
for i in range(len(铁血统帅技能列表)):
    铁血统帅技能序号[铁血统帅技能列表[i].名称] = i

铁血统帅一觉序号 = 0
铁血统帅二觉序号 = 0
铁血统帅三觉序号 = 0
for i in 铁血统帅技能列表:
    if i.所在等级 == 50:
        铁血统帅一觉序号 = 铁血统帅技能序号[i.名称]
    if i.所在等级 == 85:
        铁血统帅二觉序号 = 铁血统帅技能序号[i.名称]
    if i.所在等级 == 100:
        铁血统帅三觉序号 = 铁血统帅技能序号[i.名称]

铁血统帅护石选项 = ['无']
for i in 铁血统帅技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        铁血统帅护石选项.append(i.名称)

铁血统帅符文选项 = ['无']
for i in 铁血统帅技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        铁血统帅符文选项.append(i.名称)


class 铁血统帅角色属性(角色属性):
    实际名称 = '铁血统帅'
    角色 = '枪剑士'
    职业 = '暗刃'

    武器选项 = ['长刀']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 1.85

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(铁血统帅技能列表)
        self.技能序号 = deepcopy(铁血统帅技能序号)


class 铁血统帅(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 铁血统帅角色属性()
        self.角色属性A = 铁血统帅角色属性()
        self.角色属性B = 铁血统帅角色属性()
        self.一觉序号 = 铁血统帅一觉序号
        self.二觉序号 = 铁血统帅二觉序号
        self.三觉序号 = 铁血统帅三觉序号
        self.护石选项 = deepcopy(铁血统帅护石选项)
        self.符文选项 = deepcopy(铁血统帅符文选项)

    def 护石判断(self):
        if self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentText() != '/CD':
            大回旋坠斩次数 = int(self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentText())
        else:
            大回旋坠斩次数 = 1

        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '大回旋坠斩' and 大回旋坠斩次数 != 0:
                sign = 1
        if sign == 0:
            self.大回旋护石跳跃选项.setEnabled(False)
            self.大回旋护石跳跃选项.setStyleSheet(复选框样式)
            self.大回旋护石跳跃选项.setChecked(False)
        else:
            self.大回旋护石跳跃选项.setEnabled(True)
            self.大回旋护石跳跃选项.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())
        self.次数输入[self.角色属性A.技能序号['大回旋坠斩']].currentIndexChanged.connect(
            lambda state: self.护石判断())

        self.大回旋护石跳跃选项 = QCheckBox('大回旋护石跳跃释放', self.main_frame2)
        self.大回旋护石跳跃选项.resize(135, 20)
        self.大回旋护石跳跃选项.move(320, 420)
        self.大回旋护石跳跃选项.setStyleSheet(复选框样式)
        self.大回旋护石跳跃选项.setToolTip('跳跃释放大回旋坠斩，仅佩戴护石时生效')

        self.轮盘连射类型选项 = MyQComboBox(self.main_frame2)
        self.轮盘连射类型选项.addItem('轮盘连射：非抓取')
        self.轮盘连射类型选项.addItem('轮盘连射：抓取')
        self.轮盘连射类型选项.resize(135, 20)
        self.轮盘连射类型选项.move(320, 360)
        self.轮盘连射类型选项.setToolTip('选择轮盘连射的形态')

        self.致命焰火方向选项 = MyQComboBox(self.main_frame2)
        self.致命焰火方向选项.addItem('致命焰火方向：向后')
        self.致命焰火方向选项.addItem('致命焰火方向：原地')
        self.致命焰火方向选项.resize(135, 20)
        self.致命焰火方向选项.move(320, 450)
        self.致命焰火方向选项.setToolTip('选择致命焰火的形态')

        self.职业存档.append(('致命焰火方向选项', self.致命焰火方向选项, 1))
        self.职业存档.append(('轮盘连射类型选项', self.轮盘连射类型选项, 1))
        self.职业存档.append(('大回旋护石跳跃选项', self.大回旋护石跳跃选项, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.大回旋护石跳跃选项.isChecked():
            属性.技能栏[属性.技能序号['大回旋坠斩']].攻击次数 = 0
            属性.技能栏[属性.技能序号['大回旋坠斩']].攻击次数2 = 3 * 1.07

        if self.轮盘连射类型选项.currentIndex() == 1:
            属性.技能栏[属性.技能序号['轮盘连射']].攻击次数2 = 0
            属性.技能栏[属性.技能序号['轮盘连射']].攻击次数3 = 10

        if self.致命焰火方向选项.currentIndex() == 1:
            属性.技能栏[属性.技能序号['致命焰火']].攻击次数2 = 0
            属性.技能栏[属性.技能序号['致命焰火']].攻击次数3 = 10
