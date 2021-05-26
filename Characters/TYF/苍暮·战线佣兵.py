from math import *
from PublicReference.base import *
# 2021.4.7 韩测


class 职业主动技能(主动技能):

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

# 重剑精通


class 技能0(被动技能):
    名称 = '重剑精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1.05 + 0.01 * self.等级, 5)
        else:
            return round(1.25 + 0.025 * (self.等级 - 20), 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


# 火药改良
class 技能1(被动技能):
    名称 = '火药改良'
    所在等级 = 30
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        return round(1 + 0.015 * self.等级, 5)


# 一觉被动
class 技能2(被动技能):
    名称 = '终极火力'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.02 * self.等级, 5)


# 二觉被动
class 技能3(被动技能):
    名称 = '无法者之歌'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


# 三觉被动
class 技能4(被动技能):
    名称 = '铁血豪情'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 双重散射
class 技能5(职业主动技能):
    名称 = '双重散射'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1725.5
    # 成长 = 195.9
    # 第1次射击攻击力：<data0>%
    data0 = [int(i*1.114) for i in [0, 771, 850, 928, 1006, 1085, 1163, 1240, 1319, 1397, 1476, 1554, 1632, 1711, 1789, 1867, 1946, 2024, 2103, 2181, 2259, 2338, 2416, 2493, 2572, 2650, 2728, 2807, 2885, 2963, 3042, 3120, 3199, 3277,
                                    3355, 3434, 3512, 3590, 3668, 3746, 3824, 3903, 3981, 4060, 4138, 4216, 4295, 4373, 4451, 4530, 4608, 4687, 4765, 4842, 4920, 4999, 5077, 5156, 5234, 5312, 5391, 5469, 5547, 5626, 5704, 5783, 5861, 5939, 6018, 6095, 6173]]
    # 第2次射击攻击力：<data1>%
    data1 = [int(i*1.114) for i in [0, 1158, 1274, 1392, 1509, 1627, 1744, 1862, 1979, 2097, 2215, 2332, 2448, 2566, 2684, 2801, 2919, 3036, 3154, 3271, 3389, 3506, 3624, 3740, 3858, 3976, 4093, 4211, 4328, 4446, 4563, 4681, 4798,
                                    4915, 5032, 5150, 5268, 5385, 5503, 5620, 5738, 5855, 5973, 6089, 6207, 6324, 6442, 6560, 6677, 6795, 6912, 7030, 7147, 7264, 7381, 7499, 7616, 7734, 7852, 7969, 8087, 8204, 8322, 8439, 8556, 8673, 8791, 8908, 9026, 9143, 9261]]
    攻击次数2 = 1
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.114


# 爆裂斩击
class 技能6(职业主动技能):
    名称 = '爆裂斩击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1962.4
    成长 = 221.3
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    ###
    倍率 = 1.157


# 剑刃爆弹
class 技能7(职业主动技能):
    名称 = '剑刃爆弹'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4061.333333
    成长 = 451
    # 击退攻击力：<data0>%
    data0 = [int(i*1.124) for i in [0, 445, 491, 536, 581, 626, 672, 717, 762, 807, 852, 897, 942, 989, 1034, 1079, 1124, 1169, 1214, 1259, 1304, 1351, 1396, 1441, 1486, 1531, 1576, 1621, 1667, 1712, 1757, 1803, 1848, 1893,
                                    1938, 1984, 2029, 2074, 2119, 2164, 2209, 2254, 2301, 2346, 2391, 2436, 2481, 2526, 2571, 2616, 2663, 2708, 2753, 2798, 2843, 2888, 2933, 2979, 3024, 3069, 3114, 3160, 3205, 3250, 3296, 3341, 3386, 3431, 3476, 3521, 3566]]
    # 爆炸攻击力：<data1>%
    data1 = [int(i*1.124) for i in [0, 1263, 1391, 1519, 1648, 1775, 1904, 2032, 2160, 2288, 2417, 2544, 2673, 2802, 2929, 3058, 3185, 3314, 3441, 3570, 3698, 3826, 3955, 4083, 4211, 4339, 4468, 4595, 4724, 4851, 4980, 5109, 5236,
                                    5365, 5492, 5621, 5749, 5877, 6006, 6134, 6262, 6390, 6519, 6646, 6775, 6902, 7031, 7160, 7287, 7416, 7543, 7672, 7800, 7928, 8056, 8185, 8313, 8441, 8570, 8697, 8826, 8953, 9082, 9209, 9338, 9467, 9594, 9723, 9851, 9979, 10107]]
    攻击次数2 = 3
    # 特殊灼伤攻击力：<data2>%
    data2 = [int(i*1.124) for i in [0, 31, 35, 37, 41, 44, 48, 50, 54, 57, 61, 63, 67, 70, 73, 76, 80, 82, 86, 89, 93, 95, 99, 102, 106, 108, 112, 115, 118, 122, 125, 129, 131, 135, 138,
                                    142, 144, 148, 151, 155, 157, 161, 164, 167, 170, 174, 176, 180, 183, 187, 189, 193, 196, 200, 202, 206, 209, 212, 215, 219, 221, 225, 228, 232, 234, 238, 241, 245, 247, 251, 254]]
    # 灼烧次数待定
    攻击次数3 = 7

    CD = 12
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.124

# 广域散射


class 技能8(职业主动技能):
    名称 = '广域散射'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 3084
    # 成长 = 351
    data0 = [int(i*1.114) for i in [0, 3454, 3804, 4155, 4506, 4857, 5207, 5558, 5908, 6258, 6609, 6959, 7310, 7660, 8010, 8361, 8711, 9062, 9412, 9763, 10113, 10465, 10815, 11165, 11516, 11866, 12217, 12567, 12918, 13268, 13618, 13969, 14319, 14670, 15020,
                                    15371, 15721, 16071, 16422, 16773, 17124, 17474, 17825, 18175, 18525, 18876, 19226, 19577, 19927, 20278, 20628, 20978, 21329, 21679, 22030, 22380, 22732, 23082, 23433, 23783, 24133, 24484, 24834, 25185, 25535, 25885, 26236, 26586, 26937, 27287, 27638]]

    CD = 7
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.114

# G型火焰爆弹


class 技能9(职业主动技能):
    名称 = 'G型火焰爆弹'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 3568.333333
    # 成长 = 392
    # 爆炸攻击力：<data0>%
    data0 = [int(i*1.166) for i in [0, 3690, 4065, 4439, 4814, 5189, 5563, 5938, 6311, 6686, 7061, 7435, 7810, 8185, 8559, 8933, 9307, 9682, 10057, 10431, 10806, 11179, 11554, 11929, 12303, 12678, 13053, 13427, 13801, 14175, 14550, 14925, 15299, 15674, 16049,
                                    16422, 16797, 17171, 17546, 17921, 18295, 18670, 19043, 19418, 19793, 20167, 20542, 20917, 21290, 21665, 22039, 22414, 22789, 23163, 23538, 23911, 24286, 24661, 25035, 25410, 25785, 26159, 26533, 26907, 27282, 27657, 28031, 28406, 28781, 29154, 29529]]
    # 特殊灼伤攻击力：<data1>%
    data1 = [int(i*1.166) for i in [0, 27, 30, 32, 36, 39, 41, 44, 46, 50, 53, 55, 58, 61, 63, 67, 70, 72, 75, 77, 81, 84, 86, 89, 91, 95, 98, 100, 103, 106, 108, 112, 115, 117, 120,
                                    122, 126, 129, 131, 134, 136, 140, 143, 145, 148, 151, 153, 157, 160, 162, 165, 167, 171, 174, 176, 179, 182, 185, 188, 191, 193, 196, 198, 202, 205, 207, 210, 212, 216, 219, 221]]
    攻击次数2 = 7
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.166


# 爆裂斩
class 技能10(职业主动技能):
    名称 = '爆裂斩'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 6713.333333
    # 成长 = 757
    # 第一次爆炸攻击力：<data0>%
    data0 = [int(i*1.1) for i in [0, 1492, 1644, 1795, 1947, 2099, 2249, 2401, 2552, 2704, 2856, 3006, 3158, 3309, 3461, 3613, 3763, 3915, 4066, 4218, 4370, 4520, 4672, 4823, 4975, 5127, 5277, 5429, 5580, 5733, 5885, 6036, 6188, 6338, 6490,
                                  6642, 6793, 6945, 7095, 7247, 7399, 7550, 7702, 7852, 8004, 8156, 8307, 8459, 8610, 8761, 8913, 9064, 9216, 9367, 9518, 9670, 9821, 9973, 10124, 10276, 10427, 10578, 10730, 10881, 11033, 11185, 11336, 11488, 11640, 11791, 11943]]
    # 第二次爆炸攻击力：<data1>%
    data1 = [int(i*1.1) for i in [0, 2239, 2466, 2693, 2920, 3147, 3375, 3601, 3829, 4056, 4282, 4510, 4737, 4965, 5191, 5418, 5647, 5874, 6101, 6328, 6555, 6783, 7009, 7237, 7464, 7690, 7918, 8145, 8373, 8599, 8826, 9054, 9280, 9508, 9735, 9961,
                                  10189, 10416, 10644, 10870, 11097, 11326, 11553, 11781, 12007, 12235, 12462, 12688, 12916, 13143, 13371, 13597, 13824, 14052, 14278, 14506, 14733, 14959, 15187, 15414, 15642, 15868, 16095, 16323, 16550, 16777, 17005, 17232, 17460, 17686, 17914]]
    攻击次数2 = 1
    # 第三次爆炸攻击力：<data2>%
    data2 = [int(i*1.1) for i in [0, 3731, 4110, 4488, 4867, 5245, 5624, 6004, 6382, 6761, 7139, 7518, 7896, 8275, 8653, 9032, 9410, 9789, 10167, 10546, 10924, 11304, 11683, 12061, 12440, 12818, 13197, 13575, 13954, 14332, 14711, 15090, 15468, 15847, 16225,
                                  16604, 16983, 17362, 17740, 18119, 18498, 18876, 19255, 19633, 20012, 20390, 20769, 21147, 21526, 21904, 22283, 22663, 23041, 23420, 23798, 24177, 24555, 24934, 25312, 25691, 26069, 26448, 26826, 27205, 27583, 27962, 28342, 28720, 29099, 29477, 29856]]
    攻击次数3 = 1
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.1


# 爆弹罗网
class 技能11(职业主动技能):
    名称 = '爆弹罗网'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    # 射击攻击力：<data0>%
    data0 = [0, 478, 524, 573, 622, 671, 720, 767, 815, 864, 913, 962, 1009, 1058, 1106, 1155, 1204, 1251, 1300, 1349, 1397, 1445, 1494, 1542, 1591, 1639, 1687, 1736, 1784, 1833, 1882, 1929, 1978, 2027, 2075, 2124,
             2172, 2220, 2269, 2318, 2366, 2414, 2463, 2511, 2560, 2607, 2656, 2705, 2754, 2802, 2849, 2898, 2947, 2996, 3044, 3091, 3140, 3189, 3238, 3287, 3333, 3382, 3431, 3480, 3529, 3577, 3624, 3673, 3722, 3770, 3819]
    # 爆炸攻击力：<data1>%
    data1 = [0, 1432, 1576, 1723, 1867, 2012, 2158, 2303, 2449, 2594, 2739, 2885, 3029, 3175, 3320, 3466, 3611, 3757, 3901, 4048, 4192, 4338, 4483, 4629, 4774, 4918, 5064, 5209, 5355, 5499, 5646, 5790, 5937, 6081, 6226, 6372,
             6517, 6662, 6808, 6953, 7099, 7243, 7389, 7534, 7680, 7824, 7971, 8115, 8262, 8406, 8552, 8697, 8841, 8987, 9132, 9278, 9423, 9569, 9713, 9860, 10004, 10149, 10295, 10440, 10586, 10731, 10876, 11022, 11166, 11312, 11457]
    攻击次数2 = 6
    # 特殊灼伤攻击力：<data2>%
    data2 = [0, 68, 75, 81, 88, 95, 103, 109, 116, 124, 130, 136, 143, 151, 157, 165, 171, 179, 185, 192, 198, 206, 212, 220, 227, 234, 241, 247, 254, 261, 268, 274, 282, 290, 296,
             303, 309, 317, 323, 330, 339, 345, 351, 358, 366, 372, 379, 385, 394, 400, 407, 413, 421, 427, 434, 440, 448, 456, 462, 469, 476, 483, 489, 496, 503, 511, 518, 524, 532, 538, 545]
    攻击次数3 = 7

    # 基础 = 425.8333333 + 57.33333333 * 7
    # 成长 = 48.5 + 7 * 7
    # 攻击次数 = 1

    # 基础2 = 1278.833333
    # 成长2 = 145.5
    # 攻击次数2 = 6

    CD = 25  # 韩测改动位置
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 2 * 3.5  # 描述错误
        elif x == 1:
            self.攻击次数2 = 2 * 3.8  # 描述错误，改动位置

# 裂地爆刃


class 技能12(职业主动技能):
    名称 = '裂地爆刃'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 基础 = 9551
    # 成长 = 1076
    # ###
    # 倍率 = 1.158

    # 爆炸攻击力：<data0>%
    data0 = [int(i*1.158) for i in [0, 10610, 11687, 12763, 13839, 14917, 15993, 17070, 18146, 19222, 20299, 21375, 22451, 23528, 24605, 25682, 26758, 27834, 28911, 29987, 31064, 32140, 33216, 34293, 35370, 36447, 37523, 38599, 39676, 40752, 41828, 42905, 43981, 45059,
                                    46135, 47211, 48288, 49364, 50440, 51517, 52593, 53669, 54747, 55823, 56900, 57976, 59052, 60129, 61205, 62282, 63358, 64434, 65512, 66588, 67665, 68741, 69817, 70894, 71970, 73046, 74123, 75200, 76277, 77353, 78429, 79506, 80582, 81658, 82735, 83811, 84887]]

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.92
            self.倍率 *= 1.24
        elif x == 1:
            self.CD *= 0.92
            self.倍率 *= 1.24*1.07  # 改动位置，待测试

# 惊喜大礼


class 技能13(职业主动技能):
    名称 = '惊喜大礼'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 17084
    # 成长 = 1935
    # 爆炸攻击力：<data0>%
    data0 = [int(i*1.124) for i in [0, 3176, 3498, 3821, 4143, 4465, 4788, 5110, 5432, 5755, 6077, 6399, 6722, 7044, 7366, 7689, 8011, 8333, 8656, 8978, 9300, 9623, 9945, 10267, 10590, 10912, 11233, 11557, 11878, 12200, 12524, 12845, 13167, 13490, 13812,
                                    14134, 14457, 14779, 15101, 15424, 15746, 16068, 16391, 16713, 17035, 17357, 17680, 18002, 18324, 18647, 18969, 19291, 19614, 19936, 20258, 20581, 20903, 21224, 21548, 21869, 22191, 22515, 22836, 23158, 23481, 23803, 24125, 24448, 24770, 25092, 25415]]
    攻击次数 = 6

    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    ###
    # 倍率 = 1.124

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.89
            self.倍率 *= 1.07
        elif x == 1:
            self.CD *= 0.89
            self.倍率 *= 1.15  # 改动位置


# 一觉
class 技能14(职业主动技能):
    名称 = 'G型烬灭榴弹'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 34765.84762 * 1.1
    # 成长 = 10495.17143  * 1.1#三级效果，忘了补上
    # 首次爆炸攻击力：<data0>%
    data0 = [int(i*1.114) for i in [0, 4525, 5575, 6624, 7675, 8724, 9773, 10823, 11872, 12922, 13971, 15021, 16070, 17120, 18169, 19218, 20269, 21318, 22368, 23417, 24467, 25516, 26566, 27615, 28664, 29714, 30763, 31814, 32863, 33913, 34962, 36012, 37061, 38110,
                                    39160, 40209, 41259, 42308, 43359, 44408, 45458, 46507, 47556, 48606, 49655, 50705, 51754, 52804, 53853, 54903, 55953, 57002, 58052, 59101, 60151, 61200, 62250, 63299, 64349, 65398, 66447, 67497, 68547, 69597, 70646, 71696, 72745, 73795, 74844, 75893, 76943]]
    # 特殊灼伤攻击力：<data1>%
    data1 = [int(i*1.114) for i in [0, 322, 397, 472, 547, 622, 697, 773, 848, 923, 998, 1073, 1148, 1223, 1298, 1373, 1448, 1523, 1598, 1673, 1748, 1822, 1897, 1972, 2047, 2122, 2197, 2272, 2347, 2422, 2497, 2572, 2647, 2722,
                                    2797, 2872, 2947, 3022, 3097, 3172, 3247, 3322, 3397, 3472, 3547, 3622, 3696, 3771, 3846, 3921, 3996, 4071, 4146, 4221, 4296, 4371, 4446, 4521, 4596, 4671, 4746, 4821, 4896, 4971, 5046, 5121, 5196, 5271, 5346, 5421, 5496]]
    攻击次数2 = 7
    # 霰弹枪射击攻击力：<data2>%
    data2 = [int(i*1.114) for i in [0, 3960, 4878, 5796, 6715, 7633, 8551, 9469, 10388, 11306, 12225, 13144, 14062, 14980, 15898, 16817, 17735, 18653, 19571, 20490, 21408, 22326, 23244, 24164, 25082, 26000, 26918, 27837, 28755, 29673, 30592, 31510, 32428, 33346,
                                    34265, 35183, 36102, 37020, 37939, 38857, 39775, 40693, 41612, 42530, 43448, 44366, 45285, 46203, 47121, 48041, 48959, 49877, 50795, 51714, 52632, 53550, 54468, 55387, 56305, 57223, 58141, 59060, 59978, 60897, 61815, 62734, 63652, 64570, 65489, 66407, 67325]]
    攻击次数3 = 4
    # 最终爆炸攻击力：<data3>%
    data3 = [int(i*1.114) for i in [0, 22630, 27877, 33126, 38373, 43621, 48868, 54115, 59364, 64611, 69859, 75106, 80355, 85602, 90849, 96097, 101344, 106593, 111840, 117087, 122335, 127583, 132831, 138078, 143326, 148573, 153822, 159069, 164316, 169564, 174812, 180060, 185307, 190554, 195802,
                                    201050, 206298, 211545, 216793, 222041, 227289, 232536, 237783, 243031, 248279, 253527, 258774, 264021, 269270, 274517, 279765, 285012, 290260, 295508, 300756, 306003, 311250, 316499, 321746, 326994, 332241, 337488, 342737, 347984, 353232, 358479, 363727, 368975, 374223, 379470, 384717]]
    攻击次数4 = 1

    CD = 145
    # Lv3：[G型烬灭榴弹]攻击力增加10%，目前没有体现在技能面板上，后续需要确认
    倍率 = 1.1
    ###
    # 倍率 = 1.114

# 完美击球


class 技能15(职业主动技能):
    名称 = '完美击球'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 旋转爆炸攻击力：<data0>%
    data0 = [int(i*1.155) for i in [0, 3976, 4379, 4783, 5186, 5589, 5993, 6396, 6799, 7203, 7606, 8009, 8412, 8817, 9220, 9623, 10027, 10430, 10833, 11237, 11640, 12043, 12446, 12850, 13253, 13656, 14061, 14464, 14867, 15271, 15674, 16077, 16481, 16884, 17287,
                                    17690, 18094, 18497, 18901, 19305, 19708, 20111, 20515, 20918, 21321, 21725, 22128, 22531, 22934, 23338, 23742, 24145, 24549, 24952, 25355, 25759, 26162, 26565, 26968, 27372, 27775, 28178, 28583, 28986, 29389, 29793, 30196, 30599, 31003, 31406, 31809]]
    # 最终爆炸攻击力：<data1>%
    data1 = [int(i*1.155) for i in [0, 9278, 10218, 11160, 12101, 13042, 13983, 14925, 15865, 16807, 17748, 18690, 19630, 20572, 21514, 22454, 23396, 24337, 25279, 26219, 27161, 28102, 29043, 29984, 30926, 31867, 32808, 33749, 34691, 35631, 36573, 37514, 38456, 39396,
                                    40338, 41279, 42220, 43161, 44103, 45045, 45985, 46927, 47868, 48809, 49750, 50692, 51633, 52574, 53515, 54457, 55397, 56339, 57280, 58222, 59162, 60104, 61045, 61986, 62927, 63869, 64811, 65751, 66693, 67634, 68574, 69516, 70458, 71398, 72340, 73281, 74223]]
    攻击次数2 = 1

    # 基础 = 3581
    # 成长 = 403
    # 攻击次数 = 1

    # 基础2 = 8329.666667
    # 成长2 = 941.5
    # 攻击次数2 = 1

    护石状态 = 0
    ###
    # 倍率 = 1.155

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 = 0
            self.data0 = [int(i*1.24) for i in self.data0]
            # self.倍率 *= 1.24
            self.护石状态 = 1
        elif x == 1:
            self.攻击次数2 = 0
            self.data0 = [int(i*1.34) for i in self.data0]
            # self.倍率 *= 1.34#改动位置，具体待测试
            self.护石状态 = 1

    def 等效CD(self, 武器类型, 输出类型):
        if self.护石状态 == 0:
            return round(self.CD / self.恢复, 1)
        else:
            return round(8.3 * 0.88, 1)

# 夺命焰火


class 技能16(职业主动技能):
    名称 = '夺命焰火'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    # 基础 = 5074.6 + 7612.2
    # 成长 = 573 + 859.5
    # 攻击次数 = 1

    # 基础2 = 3167.6
    # 成长2 = 358.3
    # 攻击次数2 = 4

    # 第一次射击攻击力：<data0>%
    data0 = [int(i*1.1466) for i in [0, 5647, 6220, 6794, 7367, 7940, 8512, 9085, 9658, 10232, 10805, 11377, 11950, 12523, 13097, 13670, 14242, 14815, 15388, 15962, 16535, 17108, 17680, 18253, 18827, 19400, 19973, 20545, 21118, 21692, 22265, 22838, 23410, 23983,
                                    24557, 25130, 25703, 26275, 26848, 27422, 27995, 28568, 29140, 29713, 30286, 30860, 31433, 32005, 32578, 33151, 33725, 34298, 34870, 35443, 36016, 36590, 37163, 37735, 38308, 38881, 39455, 40028, 40600, 41173, 41746, 42320, 42893, 43466, 44038, 44611, 45185]]
    # 第二次射击攻击力：<data1>%
    data1 = [int(i*1.1466) for i in [0, 8472, 9332, 10190, 11050, 11910, 12769, 13628, 14488, 15348, 16207, 17067, 17926, 18785, 19645, 20505, 21364, 22223, 23083, 23943, 24802, 25662, 26521, 27380, 28240, 29100, 29960, 30818, 31678, 32538, 33397, 34256, 35116, 35975,
                                    36835, 37695, 38554, 39413, 40273, 41133, 41992, 42851, 43711, 44571, 45430, 46290, 47149, 48008, 48868, 49728, 50586, 51446, 52306, 53166, 54025, 54884, 55744, 56603, 57463, 58323, 59182, 60041, 60901, 61761, 62620, 63479, 64339, 65199, 66058, 66918, 67777]]
    攻击次数2 = 1
    # 最终射击攻击力：<data2>%
    data2 = [int(i*1.1466) for i in [0, 3530, 3887, 4245, 4604, 4962, 5320, 5678, 6037, 6395, 6752, 7110, 7469, 7827, 8185, 8543, 8902, 9260, 9617, 9975, 10334, 10692, 11050, 11408, 11767, 12125, 12483, 12840, 13199, 13557, 13915, 14273, 14632, 14990, 15348,
                                    15705, 16064, 16422, 16780, 17138, 17497, 17855, 18213, 18570, 18928, 19287, 19645, 20003, 20362, 20720, 21078, 21435, 21793, 22152, 22510, 22868, 23227, 23585, 23943, 24300, 24658, 25017, 25375, 25733, 26091, 26450, 26808, 27166, 27523, 27882, 28240]]
    攻击次数3 = 4

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    ###
    # 倍率 = 1.146

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.1
            self.攻击次数2 *= 1.23
        elif x == 1:
            self.攻击次数 *= 1.1
            self.攻击次数2 *= 1.39  # 改动位置，具体待测试

# 爆弹华尔兹


class 技能17(职业主动技能):
    名称 = '爆弹华尔兹'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 基础 = 5462.7
    # 成长 = 617.7
    # 攻击次数 = 3

    # 基础2 = 4920.2
    # 成长2 = 555.7
    # 攻击次数2 = 5
    # 第一次爆炸攻击力：<data0>%
    data0 = [int(i*1.1) for i in [0, 6085, 6703, 7320, 7938, 8555, 9171, 9789, 10407, 11024, 11641, 12258, 12877, 13494, 14111, 14728, 15346, 15964, 16581, 17199, 17816, 18433, 19051, 19669, 20285, 20902, 21519, 22138, 22755, 23372, 23989, 24607, 25225, 25842,
                                  26459, 27077, 27694, 28312, 28928, 29546, 30163, 30780, 31399, 32016, 32633, 33250, 33868, 34486, 35103, 35720, 36338, 36955, 37573, 38189, 38807, 39424, 40041, 40659, 41277, 41894, 42511, 43128, 43747, 44364, 44981, 45598, 46216, 46834, 47451, 48069, 48685]]
    攻击次数 = 3
    # 第二次爆炸攻击力：<data1>%
    data1 = [int(i*1.1) for i in [0, 5477, 6032, 6588, 7144, 7698, 8255, 8811, 9366, 9922, 10478, 11033, 11589, 12145, 12700, 13256, 13811, 14367, 14923, 15478, 16034, 16590, 17145, 17701, 18257, 18812, 19368, 19923, 20479, 21036, 21591, 22146, 22703, 23258, 23813,
                                  24370, 24925, 25480, 26035, 26592, 27147, 27703, 28259, 28814, 29370, 29926, 30480, 31037, 31593, 32147, 32704, 33260, 33814, 34371, 34927, 35482, 36038, 36593, 37149, 37705, 38260, 38816, 39372, 39927, 40483, 41039, 41594, 42151, 42705, 43261, 43818]]
    攻击次数2 = 5

    CD = 40
    ###
    # 倍率 = 1.1

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 += 3
            self.data1 = [int(i*1.38) for i in self.data1]
            # self.倍率 *= 1.38
            self.CD *= 0.9
# 覆灭之枪


class 技能18(职业主动技能):
    名称 = '覆灭之枪'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 50430.8
    # 成长 = 5693.7
    # 射击攻击力：<data0>%
    data0 = [int(i*1.114) for i in [0, 56124, 61817, 67511, 73205, 78898, 84592, 90286, 95979, 101673, 107367, 113060, 118755, 124449, 130143, 135836, 141530, 147224, 152917, 158611, 164305, 169998, 175692, 181386, 187079, 192773, 198468, 204161, 209855, 215549, 221242, 226936, 232630, 238323, 244017,
                                    249711, 255404, 261098, 266792, 272485, 278179, 283874, 289567, 295261, 300955, 306648, 312342, 318036, 323729, 329423, 335117, 340811, 346504, 352198, 357893, 363586, 369280, 374974, 380667, 386361, 392055, 397748, 403442, 409136, 414829, 420523, 426217, 431910, 437604, 443299, 448992]]

    CD = 50
    ###
    # 倍率 = 1.114

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i*1.4) for i in self.data0]
            # self.倍率 *= 1.40
# 二觉


class 技能19(职业主动技能):
    名称 = '终焉：硝烟狂欢'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 88115.33333
    # 成长 = 26597.5
    # CTF地雷爆炸攻击力：<data0>%
    data0 = [int(i*1.114) for i in [0, 11470, 14130, 16790, 19450, 22110, 24770, 27430, 30091, 32750, 35410, 38070, 40730, 43390, 46050, 48710, 51369, 54029, 56689, 59349, 62009, 64669, 67330, 69990, 72649, 75309, 77969, 80629, 83289, 85949, 88609, 91268, 93928, 96588, 99248, 101908,
                                    104569, 107229, 109889, 112548, 115208, 117868, 120528, 123188, 125848, 128508, 131167, 133827, 136487, 139147, 141807, 144468, 147128, 149788, 152447, 155107, 157767, 160427, 163087, 165747, 168407, 171067, 173726, 176386, 179046, 181707, 184367, 187027, 189687, 192346, 195006]]
    攻击次数 = 4
    # 最后爆炸攻击力：<data1>%
    data1 = [int(i*1.114) for i in [0, 5293, 6521, 7750, 8977, 10205, 11432, 12660, 13887, 15115, 16342, 17570, 18798, 20026, 21254, 22481, 23709, 24936, 26164, 27391, 28619, 29846, 31075, 32303, 33530, 34758, 35985, 37213, 38440, 39668, 40895, 42124, 43352, 44579,
                                    45807, 47034, 48262, 49489, 50717, 51944, 53173, 54401, 55628, 56856, 58083, 59311, 60538, 61766, 62993, 64222, 65450, 66677, 67905, 69132, 70360, 71587, 72815, 74042, 75271, 76499, 77726, 78954, 80181, 81409, 82636, 83864, 85091, 86320, 87548, 88775, 90003]]
    攻击次数2 = 13
    CD = 180
    ###
    # 倍率 = 1.114

# 95


class 技能20(主动技能):
    名称 = '铁腕爆弹'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 23647
    成长 = 2670
    攻击次数 = 4
    CD = 60  # 假设

# 三觉


class 技能21(主动技能):
    名称 = '烽火硝烟·终末之征'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 10193
    成长 = 3077
    攻击次数 = 5
    基础2 = 203860
    成长2 = 61543
    攻击次数2 = 1
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0.0


技能列表 = []
i = 0
while i >= 0:
    try:
        exec('技能列表.append(技能' + str(i) + '())')
        i += 1
    except:
        i = -1

技能序号 = dict()
for i in range(len(技能列表)):
    技能序号[技能列表[i].名称] = i

苍暮·战线佣兵一觉序号 = 0
苍暮·战线佣兵二觉序号 = 0
苍暮·战线佣兵三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        苍暮·战线佣兵一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        苍暮·战线佣兵二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        苍暮·战线佣兵三觉序号 = 技能序号[i.名称]

苍暮·战线佣兵护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        苍暮·战线佣兵护石选项.append(i.名称)

苍暮·战线佣兵符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        苍暮·战线佣兵符文选项.append(i.名称)


class 苍暮·战线佣兵角色属性(角色属性):
    实际名称 = '苍暮·战线佣兵'
    角色 = '枪剑士'
    职业 = '战线佣兵'

    武器选项 = ['重剑']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '重甲'
    防具精通属性 = ['力量']

    主BUFF = 2.0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)


class 苍暮·战线佣兵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 苍暮·战线佣兵角色属性()
        self.角色属性A = 苍暮·战线佣兵角色属性()
        self.角色属性B = 苍暮·战线佣兵角色属性()
        self.一觉序号 = 苍暮·战线佣兵一觉序号
        self.二觉序号 = 苍暮·战线佣兵二觉序号
        self.三觉序号 = 苍暮·战线佣兵三觉序号
        self.护石选项 = deepcopy(苍暮·战线佣兵护石选项)
        self.符文选项 = deepcopy(苍暮·战线佣兵符文选项)

    def 护石判断(self):
        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '爆弹罗网':
                sign = 1
        if sign == 0:
            self.爆弹罗网护石跳跃选项.setEnabled(False)
            self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)
            self.爆弹罗网护石跳跃选项.setChecked(False)
        else:
            self.爆弹罗网护石跳跃选项.setEnabled(True)
            self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)

    def 界面(self):
        super().界面()
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(lambda state: self.护石判断())
        self.爆弹罗网护石跳跃选项 = QCheckBox('爆弹罗网护石跳跃释放', self.main_frame2)
        self.爆弹罗网护石跳跃选项.resize(140, 20)
        self.爆弹罗网护石跳跃选项.move(320, 360)
        self.爆弹罗网护石跳跃选项.setStyleSheet(复选框样式)
        self.爆弹罗网护石跳跃选项.setToolTip('跳跃释放爆弹罗网，仅佩戴护石时生效')
        self.职业存档.append(('爆弹罗网护石跳跃选项', self.爆弹罗网护石跳跃选项, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)
        if self.爆弹罗网护石跳跃选项.isChecked():
            属性.技能栏[属性.技能序号['爆弹罗网']].攻击次数 = 0
