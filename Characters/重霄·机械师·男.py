from PublicReference.carry.base import *


class 技能0(被动技能):
    名称 = '方舟反应堆'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05+0.02*self.等级, 3)


class 技能1(主动技能):
    名称 = 'G1科罗纳'
    备注 = '(秒伤)'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据 = [int(i*1.19) for i in [0, 162, 179, 195, 212, 229, 245, 262, 278, 295, 311, 328, 344, 361, 377, 394, 410, 427, 443, 460, 476, 493, 509, 526, 543, 559, 576, 592, 609, 625, 642, 658, 675, 691, 708, 724, 741, 757, 774, 790, 807, 824, 840, 857, 873, 890, 906, 923, 939, 956, 972, 989, 1005, 1022, 1038, 1055, 1071, 1088, 1104, 1121, 1138, 1154, 1171, 1187, 1204, 1220, 1237, 1253, 1270, 1286, 1303]]
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.59+0.01*self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能2(主动技能):
    名称 = 'G2旋雷者'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据 = [int(i*1.0) for i in [0, 450, 496, 541, 587, 633, 679, 724, 770, 816, 861, 907, 953, 999, 1044, 1090, 1136, 1181, 1227, 1273, 1318, 1364, 1410, 1456, 1501, 1547, 1593, 1638, 1684, 1730, 1776, 1821, 1867, 1913, 1958, 2004, 2050, 2095, 2141, 2187, 2233, 2278, 2324, 2370, 2415, 2461, 2507, 2553, 2598, 2644, 2690, 2735, 2781, 2827, 2872, 2918, 2964, 3010, 3055, 3101, 3147, 3192, 3238, 3284, 3330, 3375, 3421, 3467, 3512, 3558, 3604]]
    攻击次数 = 3
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(6, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.50+0.01*self.等级, 5)

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能3(主动技能):
    名称 = '毒蛇炮'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据1 = [int(i*1.19) for i in [0, 108, 119, 130, 141, 152, 163, 174, 185, 196, 207, 218, 229, 240, 251, 262, 273, 285, 295, 306, 317, 328, 339, 350, 361, 372, 384, 395, 405, 416, 427, 438, 449, 460, 471, 482, 494, 505, 515, 526, 537, 548, 559, 570, 581, 593, 604, 615, 625, 636, 647, 658, 669, 680, 691, 703, 714, 725, 735, 746, 757, 768, 779, 790, 802, 813, 824, 835, 845, 856, 867]]
    攻击次数1 = 30
    CD = 3.5
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能4(被动技能):
    名称 = '机械概论'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['RX78追击者', 'Ez8自爆者', 'RX60陷阱追击者', '毒蛇炮', '空战机械：风暴', '空投支援', '拦截机工厂',
            '盖波加之拳', 'EZ10反击者', 'EXSZero毒蛇炮', 'TN80终结者', 'TX-45特攻队', '超时空行军', 'HS1全息机械猎手', 'GW16-瓦尔德斯坦']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085+0.015*self.等级, 3)


class 技能5(主动技能):
    名称 = 'RX78追击者'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    数据1 = [int(i*1.191) for i in [0, 588, 647, 707, 767, 826, 886, 946, 1005, 1065, 1125, 1185, 1245, 1305, 1364, 1424, 1484, 1543, 1603, 1663, 1722, 1782, 1841, 1901, 1961, 2020, 2080, 2140, 2199, 2259, 2319, 2378, 2438, 2498, 2557, 2617, 2677, 2736, 2796, 2856, 2915, 2975, 3035, 3095, 3155, 3215, 3274, 3334, 3394, 3453, 3513, 3573, 3632, 3692, 3751, 3811, 3871, 3930, 3990, 4050, 4109, 4169, 4229, 4288, 4348, 4408, 4467, 4527, 4587, 4646, 4706]]
    攻击次数1 = 2
    CD = 2.5
    TP成长 = 0.08
    TP上限 = 5
    演出时间 = 5.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能6(主动技能):
    名称 = 'Ez8自爆者'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    数据1 = [int(i*1.1939) for i in [0, 2097, 2310, 2523, 2736, 2949, 3161, 3374, 3587, 3800, 4013, 4226, 4438, 4651, 4864, 5077, 5290, 5502, 5715, 5928, 6141, 6354, 6567, 6779, 6992, 7205, 7418, 7631, 7844, 8056, 8269, 8482, 8695, 8908, 9120, 9333, 9546, 9759, 9972, 10185, 10397, 10610, 10823, 11036, 11249, 11461, 11674, 11887, 12100, 12313, 12526, 12738, 12951, 13164, 13377, 13590, 13803, 14015, 14228, 14441, 14654, 14867, 15079, 15292, 15505, 15718, 15931, 16144, 16356, 16569, 16782]]
    攻击次数1 = 1
    CD = 6.5
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 5.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = 'G3捕食者'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [int(i*1.19) for i in [0, 116, 128, 140, 152, 164, 176, 187, 199, 211, 223, 235, 247, 258, 270, 282, 294, 306, 318, 330, 341, 353, 365, 377, 389, 401, 412, 424, 436, 448, 460, 472, 484, 495, 507, 519, 531, 543, 555, 566, 578, 590, 602, 614, 626, 638, 649, 661, 673, 685, 697, 709, 720, 732, 744, 756, 768, 780, 792, 803, 815, 827, 839, 851, 863, 874, 886, 898, 910, 922, 934]]
    攻击次数1 = 4
    CD = 1
    TP成长 = 0.10
    TP上限 = 5

    def 等效CD(self, 武器类型, 输出类型):
        return round(1, 1)

    def G系加成倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.48+0.01*self.等级, 3)

    def 等效百分比(self, 武器类型):
        return self.数据1[self.等级] * self.攻击次数1 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能8(主动技能):
    名称 = 'RX60陷阱追击者'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据1 = [int(i*1.1737) for i in [0, 4808, 5296, 5784, 6272, 6760, 7248, 7735, 8223, 8711, 9199, 9687, 10175, 10663, 11150, 11638, 12126, 12614, 13102, 13590, 14078, 14565, 15053, 15541, 16029, 16517, 17005, 17493, 17980, 18468, 18956, 19444, 19932, 20420, 20908, 21395, 21883, 22371, 22859, 23347, 23835, 24323, 24810, 25298, 25786, 26274, 26762, 27250, 27738, 28225, 28713, 29201, 29689, 30177, 30665, 31153, 31640, 32128, 32616, 33104, 33592, 34080, 34568, 35055, 35543, 36031, 36519, 37007, 37495, 37983, 38470]]
    攻击次数1 = 1
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5
    演出时间 = 2.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

# class 技能9(主动技能):
#     名称 = '护石风暴'
#     所在等级 = 35
#     等级上限 = 60
#     基础等级 = 36
#     数据1 = [int(i*1) for i in [0, 346, 382, 416, 452, 487, 522, 557, 593, 627, 663, 698, 733, 768, 804, 838, 874, 909, 944, 979, 1015, 1049, 1085, 1120, 1155, 1190, 1225, 1260, 1295, 1331, 1365, 1401, 1436, 1471, 1506, 1542, 1576, 1612, 1647, 1682, 1717, 1753, 1787, 1823, 1858, 1893, 1928, 1964, 1998, 2034, 2069, 2104, 2139, 2175, 2209, 2245, 2280, 2315, 2350, 2385, 2420, 2455, 2491, 2525, 2561, 2596, 2631, 2666]]
#     攻击次数1 = 20*2.64
#     CD = 25.5
#     TP成长 = 0.10
#     TP上限 = 5
#     是否有护石 = 1
#     演出时间 = 3

#     护石选项 = ['魔界', '圣痕']

#     def 装备护石(self, x):
#         if x == 0:
#             self.倍率 *= 1
#         elif x == 1:
#             self.倍率 *= 1.0672

#     def 等效百分比(self, 武器类型):
#         return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能9(主动技能):
    名称 = '空战机械：风暴'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据1 = [int(i*1.1142) for i in [0, 346, 382, 416, 452, 487, 522, 557, 593, 627, 663, 698, 733, 768, 804, 838, 874, 909, 944, 979, 1015, 1049, 1085, 1120, 1155, 1190, 1225, 1260, 1295, 1331, 1365, 1401, 1436, 1471, 1506, 1542, 1576, 1612, 1647, 1682, 1717, 1753, 1787, 1823, 1858, 1893, 1928, 1964, 1998, 2034, 2069, 2104, 2139, 2175, 2209, 2245, 2280, 2315, 2350, 2385, 2420, 2455, 2491, 2525, 2561, 2596, 2631, 2666]]
    攻击次数1 = 1.8738
    CD = 1.0
    TP成长 = 0.10
    TP上限 = 5
    装备护石 = 0
    是否有护石 = 1

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.演出时间 = 3
            self.倍率 *= 2.64 * 20
            self.攻击次数1 = 1
            self.CD *= 30
            self.装备护石 = 1
        elif x == 1:
            self.演出时间 = 3
            self.倍率 *= 2.86 * 20
            self.攻击次数1 = 1
            self.CD *= 30
            self.装备护石 = 1

    def 等效CD(self, 武器类型, 输出类型):
        if self.装备护石 == 1:
            return super().等效CD(武器类型, 输出类型)
        else:
            return round(1, 1)

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能10(主动技能):
    名称 = '空投支援'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据1 = [int(i*1.1012) for i in [0, 704, 776, 847, 919, 990, 1062, 1133, 1205, 1276, 1348, 1419, 1490, 1562, 1633, 1705, 1776, 1848, 1919, 1991, 2062, 2134, 2205, 2277, 2348, 2420, 2491, 2563, 2634, 2706, 2777, 2849, 2920, 2992, 3063, 3135, 3206, 3278, 3349, 3421, 3492, 3564, 3635, 3707, 3778, 3850, 3921, 3992, 4064, 4135, 4207, 4278, 4350, 4421, 4493, 4564, 4636, 4707, 4779, 4850, 4922, 4993, 5065, 5136, 5208, 5279, 5351, 5422, 5494, 5565, 5637]]
    攻击次数1 = 20
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 2.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.21
        elif x == 1:
            self.倍率 *= 1.30

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能11(主动技能):
    名称 = '拦截机工厂'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据1 = [int(i*1.1859) for i in [0, 2658, 2928, 3197, 3467, 3737, 4006, 4276, 4546, 4815, 5085, 5355, 5625, 5894, 6164, 6434, 6703, 6973, 7243, 7512, 7782, 8052, 8321, 8591, 8861, 9130, 9400, 9670, 9940, 10209, 10479, 10749, 11018, 11288, 11558, 11827, 12097, 12367, 12636, 12906, 13176, 13446, 13715, 13985, 14255, 14524, 14794, 15064, 15333, 15603, 15873, 16142, 16412, 16682, 16952, 17221, 17491, 17761, 18030, 18300, 18570, 18839, 19109, 19379, 19648, 19918, 20188, 20458, 20727, 20997, 21267]]
    攻击次数1 = 8
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    光反应能量模块 = 0

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.27

    def 等效百分比(self, 武器类型):
        if self.光反应能量模块 == 1:
            self.数据1 = [int(i*1.1859) for i in [0, 23400, 25774, 28148, 30522, 32896, 35270, 37644, 40018, 42392, 44766, 47140, 49514, 51888, 54262, 56636, 59010, 61384, 63758, 66132, 68506, 70880, 73254, 75627, 78001, 80375, 82749, 85123, 87497, 89871, 92245, 94619, 96993, 99367, 101741, 104115, 106489, 108863, 111237, 113611, 115985, 118359, 120733, 123107, 125481, 127855, 130229, 132603, 134977, 137351, 139725, 142099, 144473, 146847, 149221, 151595, 153969, 156343, 158717, 161090, 163464, 165838, 168212, 170586, 172960, 175334, 177708, 180082, 182456, 184830, 187204]]
            self.攻击次数1 = 1
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能12(被动技能):
    名称 = '光反应能量模块'
    所在等级 = 45
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['拦截机工厂']
    倍率 = 1.0

    def 技能描述(self, 武器类型):
        temp = ''
        temp += '将拦截机互相连结， 生成能量散热板<br>'+ \
            '能量散热板蓄积能量并向前方发射， 然后消失'
        return temp

    def 加成倍率(self, 武器类型):
        return self.倍率

class 技能13(被动技能):
    名称 = '斗志之歌'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 < 17:
            return round(1.01+0.015*self.等级, 3)
        else:
            return round(1.25+0.02*(self.等级-16), 3)


class 技能14(主动技能):
    名称 = '盖波加之拳'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [int(i*1.2373) for i in [0, 7568, 9323, 11079, 12834, 14589, 17978, 19909, 21839, 190160, 205600, 221048, 236504, 251944, 267392, 282832, 298280, 313720, 329168, 344608, 360056, 375496, 390952, 406392, 421840, 437280, 452728, 468168, 483616, 499056, 514504, 529952, 545400, 560840, 576288, 591728, 607176, 622616, 638064, 653504, 668952, 684400, 699848, 715288, 730736, 746176, 761624, 777064, 792512, 807952, 823408, 838848, 854296, 869736, 885184, 900624, 916072, 931512, 946960, 962400, 977856, 993304, 1008744, 1024192, 1039632, 1055080, 1070520, 1085968, 1101408, 1116856, 1132304]]
    攻击次数1 = 1
    CD = 145.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率



class 技能15(主动技能):
    名称 = 'EZ10反击者'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据1 = [int(i*1.1742) for i in [0, 7672, 8451, 9229, 10008, 10786, 11564, 12343, 13121, 13900, 14678, 15457, 16235, 17013, 17792, 18570, 19349, 20127, 20905, 21684, 22462, 23241, 24019, 24797, 25576, 26354, 27133, 27911, 28690, 29468, 30246, 31025, 31803, 32582, 33360, 34138, 34917, 35695, 36474, 37252, 38030, 38809, 39587, 40366, 41144, 41922, 42701, 43479, 44258, 45036, 45815]]
    攻击次数1 = 1
    数据2 = [int(i*1.1742) for i in [0, 2557, 2817, 3076, 3336, 3595, 3854, 4114, 4373, 4633, 4892, 5152, 5411, 5671, 5930, 6190, 6449, 6709, 6968, 7228, 7487, 7747, 8006, 8265, 8525, 8784, 9044, 9303, 9563, 9822, 10082, 10341, 10601, 10860, 11120, 11379, 11639, 11898, 12158, 12417, 12676, 12936, 13195, 13455, 13714, 13974, 14233, 14493, 14752, 15012, 15271]]
    攻击次数2 = 3
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 1.5

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24
        elif x == 1:
            self.倍率 *= 1.334

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能16(主动技能):
    名称 = 'EXSZero毒蛇炮'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据1 = [int(i*1.1937) for i in [0, 383, 422, 461, 499, 538, 577, 616, 655, 694, 733, 772, 811, 849, 888, 927, 966, 1005, 1044, 1083, 1122, 1161, 1199, 1238, 1277, 1316, 1355, 1394, 1433, 1472, 1510, 1549, 1588, 1627, 1666, 1705, 1744, 1783, 1822, 1860, 1899, 1938, 1977, 2016, 2055, 2094, 2133, 2172, 2210, 2249, 2288]]
    攻击次数1 = 40
    数据2 = [int(i*1.1937) for i in [0, 1542, 1698, 1855, 2011, 2168, 2324, 2481, 2637, 2794, 2950, 3107, 3263, 3419, 3576, 3732, 3889, 4045, 4202, 4358, 4515, 4671, 4828, 4984, 5141, 5297, 5454, 5610, 5766, 5923, 6079, 6236, 6392, 6549, 6705, 6862, 7018, 7175, 7331, 7488, 7644, 7801, 7957, 8114, 8270, 8426, 8583, 8739, 8896, 9052, 9209]]
    攻击次数2 = 19
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.19
        elif x == 1:
            self.倍率 *= 1.273

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能17(被动技能):
    名称 = 'HS1机械助手'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    冷却关联技能 = ['所有']
    非冷却关联技能 = ['盖波加之拳', '超时空行军','GW16-瓦尔德斯坦']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18+0.02*self.等级, 3)

    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 0.85

class 技能18(主动技能):
    名称 = 'TN80终结者'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    数据1 = [int(i*1.097*1.1936) for i in [0, 2616, 2882, 3147, 3413, 3678, 3944, 4209, 4474, 4739, 5005, 5270, 5535, 5801, 6066, 6332, 6597, 6863, 7128, 7394, 7659, 7925, 8190, 8455, 8721, 8986, 9252, 9517, 9783, 10048, 10314, 10579, 10845, 11110, 11375, 11641, 11906, 12172, 12437, 12703, 12968, 13234, 13499, 13765, 14030, 14295, 14561, 14826, 15092, 15357, 15623, 15888, 16154, 16419, 16685, 16950, 17215, 17481, 17746, 18012, 18277, 18543, 18808, 19074, 19338, 19604, 19869, 20135, 20400, 20665, 20931]]
    攻击次数1 = 18
    数据2 = [int(i*1*1.1936) for i in [0, 9121, 10047, 10972, 11898, 12823, 13748, 14674, 15599, 16525, 17450, 18375, 19301, 20226, 21152, 22077, 23002, 23928, 24853, 25779, 26704, 27630, 28555, 29480, 30406, 31331, 32257, 33182, 34107, 35033, 35958, 36884, 37809, 38734, 39660, 40585, 41511, 42436, 43361, 44287, 45212, 46138, 47063, 47989, 48914, 49839, 50765, 51690, 52616, 53541, 54466, 55392, 56317, 57243, 58168, 59093, 60019, 60944, 61870, 62795, 63720, 64646, 65571, 66497, 67422, 68347, 69273, 70198, 71124, 72049, 72975]]
    攻击次数2 = 1
    CD = 40
    演出时间 = 2
    是否有护石 = 1
    演出时间 = 3

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.352

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能19(主动技能):
    名称 = 'TX-45特攻队'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据1 = [int(i*1.2150) for i in [0, 5891, 6489, 7087, 7684, 8282, 8880, 9477, 10075, 10673, 11271, 11868, 12466, 13064, 13661, 14259, 14857, 15455, 16052, 16650, 17248, 17845, 18443, 19041, 19639, 20236, 20834, 21432, 22029, 22627, 23225, 23823, 24420, 25018, 25616, 26213, 26811, 27409, 28007, 28604, 29202, 29800, 30397, 30995, 31593, 32191, 32788, 33386, 33984, 34581, 35179, 35777, 36375, 36972, 37570, 38168, 38765, 39363, 39961, 40559, 41156, 41754, 42352, 42949, 43547, 44145, 44742, 45340, 45938, 46536, 47133]]
    攻击次数1 = 2
    数据2 = [int(i*1.2150) for i in [0, 7855, 8652, 9449, 10246, 11043, 11840, 12637, 13434, 14231, 15028, 15825, 16622, 17419, 18215, 19012, 19809, 20606, 21403, 22200, 22997, 23794, 24591, 25388, 26185, 26982, 27779, 28576, 29373, 30170, 30967, 31764, 32561, 33358, 34154, 34951, 35748, 36545, 37342, 38139, 38936, 39733, 40530, 41327, 42124, 42921, 43718, 44515, 45312, 46109, 46906, 47703, 48500, 49296, 50093, 50890, 51687, 52484, 53281, 54078, 54875, 55672, 56469, 57266, 58063, 58860, 59657, 60454, 61251, 62048, 62845]]
    攻击次数2 = 2
    数据3 = [int(i*1.2150) for i in [0, 11783, 12978, 14174, 15369, 16565, 17760, 18955, 20151, 21346, 22542, 23737, 24933, 26128, 27323, 28519, 29714, 30910, 32105, 33301, 34496, 35691, 36887, 38082, 39278, 40473, 41669, 42864, 44059, 45255, 46450, 47646, 48841, 50037, 51232, 52427, 53623, 54818, 56014, 57209, 58404, 59600, 60795, 61991, 63186, 64382, 65577, 66772, 67968, 69163, 70359, 71554, 72750, 73945, 75140, 76336, 77531, 78727, 79922, 81118, 82313, 83508, 84704, 85899, 87095, 88290, 89485, 90681, 91876, 93072, 94267]]
    攻击次数3 = 1
    CD = 45
    演出时间 = 1.5
    是否有护石 = 1

    护石选项 = ['圣痕']

    def 装备护石(self, x):
        self.倍率 *= 1.29

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能20(主动技能):
    名称 = '超时空行军'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据1 = [int(i*1.2050) for i in [0, 491, 606, 720, 834, 948, 1062, 1176, 1290, 1404, 1518, 1632, 1746, 1860, 1975, 2089, 2203, 2317, 2431, 2545, 2659, 2773, 2887, 3001, 3115, 3229, 3344, 3458, 3572, 3686, 3800, 3914, 4028, 4142, 4256, 4370, 4484, 4598, 4712, 4827, 4941, 5055, 5169, 5283, 5397, 5511, 5625, 5739, 5853, 5967, 6081, 6196, 6310, 6424, 6538, 6652, 6766, 6880, 6994, 7108, 7222, 7336, 7450, 7565, 7679, 7793, 7907, 8021, 8135, 8249, 8363]]
    攻击次数1 = 12
    数据2 = [int(i*1.2050) for i in [0, 15743, 19393, 23044, 26695, 30345, 33996, 37646, 41297, 44948, 48598, 52249, 55899, 59550, 63201, 66851, 70502, 74153, 77803, 81454, 85104, 88755, 92406, 96056, 99707, 103357, 107008, 110659, 114309, 117960, 121611, 125261, 128912, 132562, 136213, 139864, 143514, 147165, 150815, 154466, 158117, 161767, 165418, 169068, 172719, 176370, 180020, 183671, 187322, 190972, 194623, 198273, 201924, 205575, 209225, 212876, 216526, 220177, 223828, 227478, 231129, 234779, 238430, 242081, 245731, 249382, 253033, 256683, 260334, 263984, 267635]]
    攻击次数2 = 9
    CD = 180

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能21(被动技能):
    名称 = 'SOPHIA'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(主动技能):
    名称 = 'HS1全息机械猎手'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 6
    数据1 = [int(i*1.1929) for i in [0, 120525, 132753, 144980, 157208, 169435, 181662, 193889, 206116, 218344, 230571, 242799, 255026, 267253, 279480, 291707, 303935, 316162, 328390, 340616, 352844, 365071, 377299, 389526, 401753, 413980, 426207, 438435, 450662, 462890, 475117, 487344, 499571, 511798, 524026, 536253, 548481, 560708, 572935, 585162, 597390, 609617, 621844, 634072, 646298, 658526, 670753, 682981, 695208, 707436, 719662, 731889, 744117, 756344, 768572, 780799, 793026, 805253, 817481, 829708, 841935, 854163, 866389, 878617, 890844, 903072, 915299, 927527, 939753, 951980, 964208]]
    攻击次数1 = 1
    CD = 60
    演出时间 = 3

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能23(主动技能):
    名称 = 'GW16-瓦尔德斯坦'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    数据1 = [int(i*1.1811) for i in [0, 90262, 111193, 132123, 153053, 173984, 194914, 215845, 236775, 257706, 278636, 299567, 320497, 341428, 362358, 383289, 404219, 425149, 446080, 467010, 487941, 508871, 529802, 550732, 571663, 592593, 613524, 634454, 655385, 676315, 697245, 718176, 739106, 760037, 780967, 801898, 822828, 843759, 864689, 885620, 906550, 927481, 948411, 969341, 990272, 1011202, 1032133, 1053063, 1073994, 1094924, 1115855, 1136785, 1157716, 1178646, 1199576, 1220507, 1241437, 1262368, 1283298, 1304229, 1325159, 1346090, 1367020, 1387951, 1408881, 1429812, 1450742, 1471672, 1492603, 1513533, 1534464]]
    攻击次数1 = 1
    数据2 = [int(i*1.1811) for i in [0, 3223, 3971, 4718, 5466, 6213, 6961, 7708, 8456, 9203, 9951, 10698, 11446, 12193, 12941, 13688, 14436, 15183, 15931, 16678, 17426, 18173, 18921, 19669, 20416, 21164, 21911, 22659, 23406, 24154, 24901, 25649, 26396, 27144, 27891, 28639, 29386, 30134, 30881, 31629, 32376, 33124, 33871, 34619, 35366, 36114, 36861, 37609, 38356, 39104, 39851, 40599, 41347, 42094, 42842, 43589, 44337, 45084, 45832, 46579, 47327, 48074, 48822, 49569, 50317, 51064, 51812, 52559, 53307, 54054, 54802]]
    攻击次数2 = 7
    数据3 = [int(i*1.1811) for i in [0, 135393, 166789, 198185, 229580, 260976, 292372, 323768, 355163, 386559, 417955, 449350, 480746, 512142, 543537, 574933, 606329, 637724, 669120, 700516, 731912, 763307, 794703, 826099, 857494, 888890, 920286, 951681, 983077, 1014473, 1045868, 1077264, 1108660, 1140056, 1171451, 1202847, 1234243, 1265638, 1297034, 1328430, 1359825, 1391221, 1422617, 1454012, 1485408, 1516804, 1548200, 1579595, 1610991, 1642387, 1673782, 1705178, 1736574, 1767969, 1799365, 1830761, 1862156, 1893552, 1924948, 1956343, 1987739, 2019135, 2050531, 2081926, 2113322, 2144718, 2176113, 2207509, 2238905, 2270300, 2301696]]
    攻击次数3 = 1
    数据4 = [int(i*1.1811) for i in [0, 14506, 17870, 21234, 24597, 27961, 31325, 34689, 38053, 41417, 44780, 48144, 51508, 54872, 58236, 61600, 64963, 68327, 71691, 75055, 78419, 81782, 85146, 88510, 91874, 95238, 98602, 101965, 105329, 108693, 112057, 115421, 118785, 122148, 125512, 128876, 132240, 135604, 138967, 142331, 145695, 149059, 152423, 155787, 159150, 162514, 165878, 169242, 172606, 175970, 179333, 182697, 186061, 189425, 192789, 196152, 199516, 202880, 206244, 209608, 212972, 216335, 219699, 223063, 226427, 229791, 233155, 236518, 239882, 243246, 246610]]
    攻击次数4 = 14
    CD = 290

    def 加成倍率(self, 武器类型):
        return 0.0

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3 + self.数据4[self.等级] * self.攻击次数4) * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能24(被动技能):
    名称 = '机械引爆'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 5
    是否主动 = 1
    关联技能 = ['RX78追击者', 'Ez8自爆者', 'RX60陷阱追击者',
            '空投支援', '拦截机工厂',   'EZ10反击者', 'TX-45特攻队']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return 1.40


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

一觉序号 = 0
二觉序号 = 0
三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        三觉序号 = 技能序号[i.名称]

护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        护石选项.append(i.名称)

符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        符文选项.append(i.名称)


class 职业角色属性(角色属性):

    实际名称 = '重霄·机械师·男'
    角色 = '神枪手(男)'
    职业 = '机械师'

    武器选项 = ['自动手枪']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 1.850

    远古记忆 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        if self.技能栏[self.技能序号['光反应能量模块']].等级 != 0:
            self.技能栏[self.技能序号['拦截机工厂']].光反应能量模块 = 1
            if self.装备检查('雷霆怒啸手枪'):
                self.技能栏[self.技能序号['光反应能量模块']].倍率 *= 1.2
        super().被动倍率计算()
        self.技能栏[self.技能序号['G1科罗纳']].被动倍率 *= 1+self.技能栏[self.技能序号['G2旋雷者']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G2旋雷者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G3捕食者']].G系加成倍率()
        self.技能栏[self.技能序号['G3捕食者']].被动倍率 *= 1+self.技能栏[self.技能序号['G1科罗纳']
                                                        ].G系加成倍率()+self.技能栏[self.技能序号['G2旋雷者']].G系加成倍率()
class 重霄·机械师·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业角色属性()
        self.角色属性A = 职业角色属性()
        self.角色属性B = 职业角色属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)
