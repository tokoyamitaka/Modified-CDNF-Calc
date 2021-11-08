from math import *
from PublicReference.carry.base import *


class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        if len(self.data3) >= self.等级 and len(self.data3) > 0:
            等效倍率 += self.data3[self.等级] * self.攻击次数4
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能0(职业主动技能):
    名称 = '背摔'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    #基础 = 1386.43 * 1.092
    #成长 = 156.57 * 1.092
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5
    data0 = [int(i*1.2150*1.051) for i in [0, 1685, 1859, 2029, 2197, 2367, 2541, 2711, 2880, 3053, 3224, 3394, 3562, 3736, 3906, 4081, 4251, 4418, 4590, 4763, 4934, 5101, 5275, 5446, 5619, 5787, 5958, 6128, 6302, 6473, 6640, 6814, 6984, 7156, 7323, 7497, 7668, 7842, 8009, 8179, 8351, 8524, 8691, 8863, 9036, 9207, 9380, 9548, 9719, 9889, 10063, 10231, 10401, 10575, 10746, 10913, 11084, 11257, 11429, 11603, 11770, 11941, 12111, 12285, 12453, 12624, 12797, 12968, 13136, 13309, 13480]]


class 技能1(职业主动技能):
    名称 = '抛投'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #基础 = 3164.50 * 1.077
    #成长 = 357.47 * 1.077
    CD = 8.5
    TP成长 = 0.1
    TP上限 = 5
    data0 = [int(i*1.2228*1.052) for i in [0, 3793, 4180, 4564, 4948, 5334, 5719, 6104, 6489, 6872, 7259, 7643, 8029, 8414, 8798, 9184, 9568, 9954, 10338, 10723, 11108, 11493, 11878, 12263, 12648, 13033, 13417, 13803, 14187, 14573, 14957, 15342, 15727, 16112, 16499, 16882, 17266, 17653, 18037, 18423, 18807, 19191, 19578, 19961, 20348, 20732, 21118, 21502, 21887, 22272, 22657, 23042, 23427, 23811, 24197, 24581, 24967, 25352, 25736, 26122, 26506, 26892, 27276, 27661, 28046, 28431, 28816, 29201, 29587, 29971, 30355]]


class 技能2(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    关联技能2 = ['裂石破天', '死亡摇篮']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.65


class 技能3(职业主动技能):
    名称 = '折颈'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 41
    #基础 = 3430.65
    #成长 = 387.38
    CD = 7.7
    TP成长 = 0.1
    TP上限 = 5
    data0 = [int(i*1.2836*1.051) for i in [0, 3818, 4205, 4593, 4980, 5366, 5754, 6141, 6529, 6916, 7304, 7691, 8079, 8466, 8854, 9241, 9629, 10016, 10402, 10790, 11177, 11565, 11952, 12340, 12727, 13115, 13502, 13890, 14277, 14665, 15052, 15439, 15825, 16213, 16600,
                                  16988, 17375, 17763, 18150, 18538, 18925, 19313, 19700, 20088, 20475, 20861, 21249, 21636, 22024, 22411, 22799, 23186, 23574, 23961, 24349, 24736, 25124, 25511, 25897, 26285, 26672, 27060, 27447, 27834, 28222, 28609, 28997, 29384, 29772, 30159, 30547]]


class 技能4(职业主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    #基础 = 4091.91 * 1.05
    #成长 = 462.08 * 1.05
    CD = 8.0
    TP成长 = 0.1
    TP上限 = 5
    data0 = [int(i*1.2650*1.051) for i in [0, 4782, 5267, 5752, 6238, 6723, 7208, 7693, 8178, 8664, 9149, 9634, 10119, 10604, 11089, 11574, 12059, 12544, 13029, 13515, 14000, 14485, 14970, 15455, 15940, 16425, 16910, 17395, 17880, 18366, 18851, 19336, 19821, 20306, 20791, 21276, 21761, 22246, 22734, 23219, 23704, 24189, 24674, 25159, 25644, 26129, 26614, 27099, 27585, 28070, 28555, 29040, 29525, 30010, 30495, 30980, 31465, 31950, 32436, 32921, 33406, 33891, 34376, 34861, 35346, 35831, 36316, 36801, 37287, 37772, 38257]]


class 技能5(被动技能):
    名称 = '强力抱摔'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能6(职业主动技能):
    名称 = '霹雳肘击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #基础 = 5348.07 * 1.05
    #成长 = 603.95 * 1.05
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.2505*1.051) for i in [0, 6250, 6885, 7518, 8153, 8786, 9422, 10055, 10689, 11322, 11957, 12591, 13226, 13859, 14494, 15129, 15763, 16397, 17031, 17665, 18298, 18934, 19567, 20202, 20835, 21470, 22104, 22739, 23372, 24006, 24640, 25275, 25908, 26543, 27176, 27811, 28445, 29080, 29713, 30348, 30982, 31616, 32251, 32884, 33519, 34152, 34788, 35421, 36056, 36689, 37323, 37958, 38592, 39225, 39860, 40493, 41129, 41762, 42397, 43030, 43665, 44298, 44933, 45568, 46201, 46836, 47469, 48105, 48738, 49373, 50006]]


class 技能7(职业主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #基础 = 3787.39 * 1.078
    #成长 = 436.65 * 1.078
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.2555*1.051) for i in [0, 4553, 5017, 5485, 5963, 6434, 6901, 7370, 7845, 8318, 8787, 9251, 9727, 10194, 10668, 11137, 11611, 12078, 12553, 13021, 13497, 13960, 14428, 14903, 15376, 15850, 16317, 16784, 17262, 17732, 18194, 18664, 19136, 19616, 20083, 20551, 21018, 21494, 21970, 22432, 22901, 23374, 23843, 24318, 24784, 25261, 25728, 26203, 26668, 27141, 27610, 28081, 28551, 29024, 29494, 29966, 30438, 30901, 31376, 31847, 32314, 32791, 33257, 33733, 34201, 34673, 35138, 35614, 36082, 36557, 37024]]


class 技能8(职业主动技能):
    名称 = '霹雳冲击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #基础 = 2559.92
    #成长 = 289.04
    #基础2 = 5835.91
    #成长2 = 659.11
    攻击次数 = 1
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5
    data0 = [int(i*1.2475*1.05) for i in [0, 3142, 3461, 3780, 4099, 4418, 4736, 5056, 5374, 5694, 6011, 6331, 6649, 6969, 7286, 7606, 7924, 8244, 8561, 8881, 9199, 9519, 9838, 10156, 10475, 10794, 11113, 11431, 11750, 12069, 12388, 12708, 13025, 13345, 13663, 13983, 14300, 14620, 14938, 15258, 15575, 15895, 16213, 16533, 16851, 17170, 17489, 17808, 18127, 18445, 18764, 19083, 19403, 19722, 20040, 20359, 20678, 20997, 21315, 21634, 21953, 22272, 22592, 22909, 23229, 23547, 23867, 24184, 24504, 24822, 25142]]
    data1 = [int(i*1.2475*1.05) for i in [0, 7164, 7892, 8619, 9346, 10073, 10799, 11527, 12254, 12981, 13708, 14435, 15161, 15889, 16616, 17342, 18069, 18796, 19524, 20251, 20978, 21705, 22432, 23157, 23884, 24612, 25339, 26066, 26793, 27520, 28248, 28975, 29702, 30428, 31154, 31881, 32609, 33336, 34063, 34790, 35517, 36245, 36971, 37698, 38425, 39152, 39878, 40605, 41333, 42060, 42786, 43513, 44240, 44968, 45695, 46422, 47149, 47875, 48601, 49329, 50056, 50783, 51510, 52237, 52965, 53692, 54419, 55146, 55871, 56598, 57326]]


class 技能9(职业主动技能):
    名称 = '螺旋彗星落'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #基础 = 8630.10 * 1.078
    #成长 = 974.93 * 1.078
    data0 = [int(i*1.2871*1.052) for i in [0, 10354, 11405, 12456, 13507, 14557, 15608, 16659, 17710, 18760, 19811, 20863, 21911, 22962, 24014, 25064, 26115, 27166, 28216, 29267, 30318, 31369, 32419, 33470, 34519, 35570, 36621, 37672, 38722, 39773, 40824, 41875, 42925, 43976, 45027, 46076, 47127, 48178, 49228, 50279, 51330, 52380, 53431, 54482, 55533, 56583, 57633, 58683, 59734, 60785, 61836, 62886, 63937, 64988, 66039, 67089, 68140, 69189, 70240, 71291, 72342, 73392, 74443, 75494, 76546, 77596, 78647, 79698, 80747, 81798, 82848]]
    CD = 20.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
            self.CD *= 0.88
        elif x == 1:
            self.倍率 *= 1.29
            self.CD *= 0.88
    # 附加效果：攻击力+8%更变至攻击力+17%


class 技能10(职业主动技能):
    名称 = '地狱摇篮（抓轰炮）'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    #基础 = 13623.29 * 1.078
    #成长 = 1539.26 * 1.078
    data0 = [int(i*1.2673*1.05) for i in [0, 16349, 18008, 19668, 21325, 22985, 24642, 26302, 27961, 29619, 31278, 32936, 34595, 36254, 37912, 39571, 41229, 42889, 44548, 46206, 47865, 49523, 51182, 52841, 54499, 56158, 57819, 59475, 61136, 62794, 64453, 66112, 67770, 69429, 71087, 72746, 74406, 76063, 77723, 79380, 81040, 82699, 84357, 86016, 87674, 89333, 90993, 92650, 94310, 95967, 97627, 99286, 100944, 102603, 104262, 105920, 107579, 109237, 110896, 112556, 114214, 115873, 117531, 119190, 120849, 122507, 124166, 125824, 127483, 129143, 130800]]
    CD = 30.0
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.32
            self.CD *= 0.9
    # 附加效果：最后一击攻击力+30%更变至最后一击攻击力+59% ; [抓轰炮]攻击力 +10%更变至[抓轰炮]攻击力 +19%


class 技能11(职业主动技能):
    名称 = '裂石破天'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 15889.25 * 1.10
    # 成长 = 1794.98 * 1.10
    # 落地物理攻击力：<data8>
    # 学习[随机应变]后形态
    data0 = [int(i*1.2495*1.05) for i in [0, 11790, 12987, 14185, 15379, 16577, 17773, 18967, 20165, 21362, 22557, 23755, 24950, 26145, 27343, 28537, 29734, 30932, 32128, 33326, 34519, 35715, 36913, 38110, 39305, 40502, 41697, 42892, 44090, 45287, 46483, 47680, 48875, 50070, 51268, 52465, 53660, 54857, 56053, 57250, 58445, 59640, 60838, 62035, 63232, 64428, 65623, 66817, 68015, 69212, 70410, 71605, 72799, 73997, 75193, 76390, 77587, 78782, 79980, 81175, 82370, 83568, 84763, 85960, 87157, 88352, 89548, 90745, 91940, 93137, 94335]]
    CD = 45
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31
   # 最后一击冲击波攻击力+17%更变至最后一击冲击波攻击力+28% ; [随机应变]冲击波攻击力增加量+13%更变至[随机应变]冲击波攻击力增加量+21%


class 技能12(被动技能):
    名称 = '抓取奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.09 + 0.015 * self.等级, 5)


class 技能13(职业主动技能):
    名称 = '末日风暴'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    #基础 = 1340.79
    #成长 = 406.02
    #基础2 = 20945.11
    #成长2 = 6317.08
    攻击次数2 = 1
    # 倍率 = 1.107
    CD = 140.0
    data0 = [int(i*1.2217) for i in [0, 1937, 2387, 2834, 3283, 3734, 4183, 4632, 5080, 5531, 5979, 6428, 6878, 7326, 7778, 8225, 8674, 9124, 9573, 10021, 10472, 10921, 11369, 11818, 12267, 12718, 13166, 13615, 14064, 14515, 14964, 15412, 15861, 16311, 16759, 17208, 17659, 18107, 18556, 19006, 19454, 19905, 20352, 20802, 21252, 21702, 22150, 22599, 23048, 23499, 23947, 24395, 24846, 25294, 25745, 26193, 26642, 27092, 27541, 27989, 28439, 28888, 29337, 29786, 30235, 30686, 31133, 31583, 32032, 32480, 32932]]
    data1 = [int(i*1.2218) for i in [0, 30164, 37158, 44150, 51148, 58143, 65136, 72131, 79124, 86120, 93114, 100109, 107102, 114098, 121093, 128087, 135082, 142077, 149071, 156065, 163059, 170053, 177049, 184043, 191037, 198032, 205026, 212023, 219016, 226011, 233004, 240000, 246993, 253989, 260983, 267978, 274973, 281966, 288960, 295956, 302952, 309945, 316940, 323934, 330930, 337924, 344918, 351912, 358907, 365902, 372896, 379890, 386885, 393879, 400875, 407869, 414864, 421858, 428853, 435846, 442841, 449836, 456831, 463825, 470819, 477813, 484810, 491804, 498798, 505792, 512787]]


class 技能14(职业主动技能):
    名称 = '空绞连锤（抓轰炮）'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    #基础 = 1170.88
    #成长 = 132.08
    data0 = [int(i*1.2416*1.05) for i in [0, 1475, 1624, 1773, 1924, 2074, 2222, 2372, 2523, 2672, 2821, 2972, 3121, 3270, 3421, 3569, 3720, 3869, 4019, 4168, 4319, 4468, 4617, 4767, 4915, 5067, 5216, 5365, 5516, 5666, 5814, 5963, 6115, 6263, 6413, 6563, 6712, 6862, 7013, 7161, 7310, 7461, 7612, 7760, 7909, 8061, 8209, 8359, 8507, 8659, 8808, 8956, 9107, 9257, 9406, 9556, 9706, 9856, 10005, 10155, 10305, 10454, 10605, 10754, 10902, 11053, 11203, 11352, 11501, 11653, 11801]]
    #基础2 = 14058.93
    #成长2 = 1588.06
    data1 = [int(i*1.2416*1.05) for i in [0, 17712, 19510, 21308, 23104, 24901, 26698, 28495, 30293, 32090, 33888, 35684, 37481, 39279, 41076, 42872, 44669, 46465, 48264, 50060, 51857, 53653, 55451, 57250, 59046, 60844, 62640, 64437, 66234, 68032, 69829, 71625, 73422, 75220, 77017, 78813, 80610, 82407, 84206, 86003, 87799, 89597, 91393, 93191, 94987, 96785, 98581, 100378, 102174, 103973, 105770, 107566, 109363, 111161, 112959, 114755, 116552, 118349, 120146, 121944, 123741, 125538, 127334, 129131, 130929, 132726, 134522, 136319, 138115, 139915, 141712]]
    攻击次数2 = 1
    # 倍率 = 1.132
    CD = 30.0
    # TP成长 = 0.10
    # TP基础 = 5
    # TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.12
        elif x == 1:
            self.倍率 *= 1.21
    # 攻击力 +12%更变至攻击力  +21%


class 技能15(被动技能):
    名称 = '极手奥义'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能16(职业主动技能):
    名称 = '死亡摇篮'
    所在等级 = 70
    等级上限 = 60
    基础等级 = 18
    # 基础 = 25524.88 * 1.10
    # 成长 = 2883.51 * 1.10
    # 旋转攻击物理攻击力：<data6>
    data0 = [int(i*1.2426*1.052) for i in [0, 18939, 20859, 22781, 24704, 26624, 28546, 30468, 32387, 34309, 36233, 38152, 40074, 41996, 43916, 45838, 47761, 49682, 51603, 53525, 55444, 57366, 59290, 61210, 63131, 65053, 66974, 68895, 70817, 72739, 74660, 76582, 78502, 80423, 82345, 84266, 86187, 88110, 90031, 91952, 93874, 95794, 97715, 99639, 101560, 103479, 105403, 107323, 109243, 111168, 113088, 115008, 116930, 118852, 120771, 122695, 124617, 126536, 128458, 130380, 132300, 134222, 136145, 138065, 139987, 141909, 143828, 145750, 147674, 149593, 151515]]
    CD = 50
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.23
        elif x == 1:
            self.倍率 *= 1.31


class 技能17(职业主动技能):
    名称 = '末日摇篮'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    #基础 = 7654.70
    #成长 = 864.27
    #基础2 = 30620.97
    #成长2 = 3457.06
    data0 = [int(i*1.2416*1.052) for i in [0, 9371, 10321, 11272, 12223, 13174, 14124, 15076, 16026, 16976, 17927, 18878, 19829, 20779, 21731, 22681, 23631, 24583, 25533, 26484, 27435, 28386, 29336, 30286, 31238, 32188, 33139, 34090, 35041, 35991, 36942, 37893, 38843, 39795, 40745, 41696, 42646, 43597, 44548, 45498, 46450, 47400, 48351, 49302, 50252, 51203, 52154, 53105, 54055, 55006, 55957, 56907, 57858, 58809, 59760, 60710, 61662, 62612, 63562, 64514, 65464, 66415, 67367, 68317, 69267, 70217, 71169, 72119, 73070, 74021, 74972]]
    data1 = [int(i*1.2416*1.052) for i in [0, 37486, 41286, 45089, 48895, 52696, 56498, 60304, 64105, 67907, 71709, 75515, 79317, 83118, 86924, 90727, 94527, 98333, 102134, 105937, 109743, 113543, 117346, 121147, 124953, 128755, 132557, 136363, 140165, 143966, 147772, 151572, 155375, 159181, 162983, 166784, 170586, 174392, 178195, 181995, 185801, 189604, 193404, 197210, 201011, 204813, 208619, 212421, 216223, 220024, 223830, 227633, 231433, 235239, 239042, 242843, 246649, 250450, 254252, 258058, 261859, 265662, 269467, 273269, 277071, 280872, 284678, 288481, 292281, 296087, 299889]]
    攻击次数2 = 1
    # 倍率 = 1.1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.3225
            self.CD *= 0.9
    # 攻击力+15% ；生成总攻击力15%伤害的旋风（多段，15次攻击，每次1%）


class 技能18(职业主动技能):
    名称 = '风暴之舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    #基础 = 5308.98
    #成长 = 600.99
    #基础2 = 14760.91
    #成长2 = 1665.05
    data0 = [int(i*1.2376*1.053) for i in [0, 6501, 7162, 7819, 8481, 9139, 9798, 10458, 11119, 11778, 12437, 13098, 13754, 14416, 15073, 15733, 16393, 17052, 17713, 18371, 19031, 19690, 20351, 21009, 21669, 22330, 22987, 23649, 24307, 24967, 25626, 26287, 26946, 27605, 28266, 28922, 29585, 30242, 30902, 31561, 32222, 32881, 33540, 34201, 34858, 35520, 36177, 36838, 37499, 38156, 38817, 39475, 40135, 40795, 41454, 42114, 42774, 43432, 44092, 44752, 45410, 46070, 46730, 47389, 48049, 48709, 49368, 50028, 50688, 51346, 52006]]
    data1 = [int(i*1.2376*1.053) for i in [0, 18069, 19900, 21735, 23566, 25399, 27231, 29068, 30900, 32733, 34566, 36398, 38231, 40064, 41897, 43728, 45563, 47395, 49227, 51064, 52896, 54728, 56561, 58395, 60226, 62059, 63892, 65725, 67558, 69392, 71226, 73059, 74892, 76724, 78557, 80389, 82223, 84055, 85887, 87721, 89553, 91387, 93222, 95054, 96887, 98721, 100554, 102385, 104217, 106052, 107885, 109717, 111551, 113384, 115216, 117049, 118883, 120715, 122548, 124380, 126215, 128048, 129880, 131713, 133547, 135379, 137212, 139044, 140878, 142712, 144544]]
    攻击次数 = 6
    攻击次数2 = 1
    # 倍率 = 1.1
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(x*0.56) for x in self.data0]
            self.攻击次数 = 13
            # self.基础 *= 0.56
            # self.成长 *= 0.56
            # self.攻击次数 = 13
            self.倍率 *= 1.19
    # 多段攻击力减少44% ；次数+7；攻击力+19%


class 技能19(职业主动技能):
    名称 = '苍宇彗星落'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    #基础 = 8601.87
    #成长 = 2598.03
    #基础2 = 77442.63
    #成长2 = 23385.07
    data0 = [int(i*1.2257) for i in [0, 12321, 15178, 18036, 20895, 23751, 26609, 29466, 32322, 35179, 38038, 40895, 43751, 46608, 49467, 52324, 55183, 58039, 60896, 63753, 66611, 69467, 72324, 75181, 78041, 80897, 83755, 86612, 89469, 92325, 95183, 98041, 100898, 103755, 106613, 109470, 112328, 115184, 118042, 120899, 123757, 126613, 129470, 132328, 135185, 138043, 140901, 143758, 146615, 149471, 152329]]
    data1 = [int(i*1.2257) for i in [0, 110922, 136642, 162361, 188084, 213805, 239528, 265246, 290968, 316690, 342409, 368134, 393853, 419574, 445295, 471016, 496738, 522458, 548178, 573901, 599622, 625343, 651064, 676785, 702506, 728228, 753950, 779670, 805390, 831113, 856833, 882553, 908276, 933996, 959718, 985438, 1011160, 1036882, 1062601, 1088324, 1114045, 1139764, 1165486, 1191208, 1216930, 1242649, 1268369, 1294093, 1319814, 1345534, 1371256]]
    攻击次数2 = 1
    # 倍率 = 1.1
    CD = 180


class 技能20(被动技能):
    名称 = '光芒之翼'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能21(职业主动技能):
    名称 = '送葬舞步'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    data0 = [int(i*1.2337*1.053) for i in [0, 10553, 11623, 12694, 13765, 14835, 15906, 16977, 18047, 19118, 20188, 21259, 22329, 23400, 24471, 25541, 26612, 27682, 28753, 29824, 30894, 31965, 33036, 34106, 35177, 36247, 37318, 38388, 39459, 40530, 41600, 42671, 43741, 44812, 45883, 46953, 48024, 49095, 50165, 51236, 52306, 53377, 54448, 55518, 56589, 57659, 58730, 59801, 60871, 61942, 63012, 64083, 65153, 66224, 67295, 68365, 69436, 70507, 71577, 72648, 73718, 74789, 75860, 76930, 78001, 79072, 80142, 81213, 82283, 83354, 84424]]
    data1 = [int(i*1.2337*1.053) for i in [0, 47487, 52305, 57123, 61940, 66759, 71576, 76394, 81212, 86029, 90847, 95665, 100482, 105300, 110119, 114936, 119753, 124571, 129389, 134206, 139024, 143842, 148661, 153478, 158295, 163112, 167931, 172748, 177565, 182384, 187202, 192019, 196837, 201655, 206472, 211290, 216107, 220925, 225744, 230561, 235378, 240197, 245014, 249831, 254649, 259467, 264285, 269103, 273920, 278738, 283556, 288373, 293190, 298009, 302827, 307644, 312462, 317280, 322097, 326915, 331733, 336550, 341369, 346186, 351004, 355822, 360639, 365456, 370275, 375092, 379909]]
    攻击次数2 = 1
    data2 = [int(i*1.2337*1.053) for i in [0, 47487, 52305, 57123, 61940, 66759, 71576, 76394, 81212, 86029, 90847, 95665, 100482, 105300, 110119, 114936, 119753, 124571, 129389, 134206, 139024, 143842, 148661, 153478, 158295, 163112, 167931, 172748, 177565, 182384, 187202, 192019, 196837, 201655, 206472, 211290, 216107, 220925, 225744, 230561, 235378, 240197, 245014, 249831, 254649, 259467, 264285, 269103, 273920, 278738, 283556, 288373, 293190, 298009, 302827, 307644, 312462, 317280, 322097, 326915, 331733, 336550, 341369, 346186, 351004, 355822, 360639, 365456, 370275, 375092, 379909]]
    攻击次数3 = 1
    CD = 60.0


class 技能22(职业主动技能):
    名称 = '女皇时代辉煌舞台'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']
    data0 =  [int(i*1.2251) for i in [0, 34656, 42693, 50729, 58766, 66802, 74838, 82875, 90911, 98948, 106984, 115020, 123057, 131093, 139129, 147166, 155202, 163239, 171275, 179311, 187348, 195384, 203421, 211457, 219493, 227530, 235566, 243602, 251639, 259675, 267712, 275748, 283784, 291821, 299857, 307894, 315930, 323966, 332003, 340039, 348076, 356112, 364148, 372185, 380221, 388257, 396294, 404330, 412367, 420403, 428439, 436476, 444512, 452549, 460585, 468621, 476658, 484694, 492730, 500767, 508803, 516840, 524876, 532912, 540949, 548985, 557022, 565058, 573094, 581131, 589167]]
    data1 =  [int(i*1.2251) for i in [0, 69313, 85386, 101459, 117532, 133604, 149677, 165750, 181823, 197896, 213968, 230041, 246114, 262187, 278259, 294332, 310405, 326478, 342551, 358623, 374696, 390769, 406842, 422914, 438987, 455060, 471133, 487205, 503278, 519351, 535424, 551497, 567569, 583642, 599715, 615788, 631860, 647933, 664006, 680079, 696152, 712224, 728297, 744370, 760443, 776515, 792588, 808661, 824734, 840807, 856879, 872952, 889025, 905098, 921170, 937243, 953316, 969389, 985461, 1001534, 1017607, 1033680, 1049753, 1065825, 1081898, 1097971, 1114044, 1130116, 1146189, 1162262, 1178335]]
    攻击次数2 = 3
    data2 = [int(i*1.2251) for i in [0, 17328, 21346, 25364, 29383, 33401, 37419, 41437, 45455, 49474, 53492, 57510, 61528, 65546, 69564, 73583, 77601, 81619, 85637, 89655, 93674, 97692, 101710, 105728, 109746, 113765, 117783, 121801, 125819, 129837, 133856, 137874, 141892, 145910, 149928, 153947, 157965, 161983, 166001, 170019, 174038, 178056, 182074, 186092, 190110, 194128, 198147, 202165, 206183, 210201, 214219, 218238, 222256, 226274, 230292, 234310, 238329, 242347, 246365, 250383, 254401, 258420, 262438, 266456, 270474, 274492, 278511, 282529, 286547, 290565, 294583]]
    攻击次数3 = 6

    CD = 290

    def 加成倍率(self, 武器类型):
        return 0


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能'+str(i)+'())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

归元·柔道家·女一觉序号 = 0
归元·柔道家·女二觉序号 = 0
归元·柔道家·女三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        归元·柔道家·女一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        归元·柔道家·女二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        归元·柔道家·女三觉序号 = 技能序号[i.名称]

归元·柔道家·女护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·柔道家·女护石选项.append(i.名称)

归元·柔道家·女符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·柔道家·女符文选项.append(i.名称)


class 归元·柔道家·女角色属性(角色属性):

    实际名称 = '归元·柔道家·女'
    角色 = '格斗家(女)'
    职业 = '柔道家'

    武器选项 = ['手套', '臂铠', '东方棍', '爪']

    类型选择 = ['物理固伤']

    类型 = '物理固伤'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.07

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 归元·柔道家·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·柔道家·女角色属性()
        self.角色属性A = 归元·柔道家·女角色属性()
        self.角色属性B = 归元·柔道家·女角色属性()
        self.一觉序号 = 归元·柔道家·女一觉序号
        self.二觉序号 = 归元·柔道家·女二觉序号
        self.三觉序号 = 归元·柔道家·女三觉序号
        self.护石选项 = deepcopy(归元·柔道家·女护石选项)
        self.符文选项 = deepcopy(归元·柔道家·女符文选项)

    def 界面(self):
        super().界面()

        self.死亡风暴次数选择 = MyQComboBox(self.main_frame2)
        for i in range(1, 14):
            self.死亡风暴次数选择.addItem('末日风暴：' + str(i) + '段')
        self.死亡风暴次数选择.setCurrentIndex(12)
        self.死亡风暴次数选择.resize(120, 20)
        self.死亡风暴次数选择.move(325, 390)

        self.职业存档.append(('死亡风暴次数选择', self.死亡风暴次数选择, 1))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        属性.技能栏[属性.技能序号['末日风暴']].攻击次数 *= self.死亡风暴次数选择.currentIndex() + 1
