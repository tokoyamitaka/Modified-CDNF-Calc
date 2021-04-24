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

# 源力剑精通


class 技能0(被动技能):
    名称 = '源力剑精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    谍影专用倍率 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        if self.等级 <= 20:
            return round(1 + (0.05 + 0.01 * self.等级) * self.谍影专用倍率, 5)
        else:
            return round(1 + (0.25 + 0.02 * (self.等级 - 20)) * self.谍影专用倍率, 5)

    def 魔法攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


# 细胞弱化
class 技能1(被动技能):
    名称 = '细胞弱化'
    所在等级 = 25
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.23 + 0.02 * self.等级, 5)


# 源能增幅一觉被动
class 技能2(被动技能):
    名称 = '源能增幅'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


# 二觉被动
class 技能3(被动技能):
    名称 = '源力汇聚'
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
    名称 = '奇点核心'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


# 源光斩
class 技能5(职业主动技能):
    名称 = '源光斩'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    攻击段数 = 2
    # 斩击攻击力：<data0>%
    data0 = [0, 859, 946, 1033, 1120, 1208, 1295, 1382, 1469, 1556, 1644, 1730, 1818, 1906, 1992, 2080, 2166, 2254, 2341, 2428, 2516, 2602, 2690, 2777, 2864, 2951, 3039, 3126, 3213, 3300, 3387, 3475, 3561, 3649, 3736,
             3823, 3911, 3997, 4085, 4172, 4259, 4347, 4433, 4521, 4608, 4695, 4782, 4869, 4957, 5044, 5131, 5218, 5306, 5392, 5480, 5566, 5654, 5742, 5828, 5916, 6002, 6090, 6178, 6264, 6352, 6439, 6526, 6613, 6700, 6787, 6875]
    # 能量多段攻击力：<data1>%
    data1 = [0, 146, 161, 176, 191, 205, 221, 236, 251, 265, 280, 295, 310, 326, 340, 355, 370, 385, 399, 414, 429, 444, 460, 474, 489, 504, 519, 533, 548, 563, 579, 594, 608, 623, 638, 653,
             667, 682, 698, 713, 728, 742, 757, 772, 787, 801, 817, 832, 847, 862, 876, 891, 906, 921, 935, 951, 966, 981, 996, 1010, 1025, 1040, 1056, 1070, 1085, 1100, 1115, 1129, 1144, 1159, 1175]
    攻击次数2 = 4
    # 基础 = 1443.00 - 146.85
    # 成长 = 146.85
    CD = 5
    TP成长 = 0.08
    TP上限 = 5


# 旋转源能波
class 技能6(职业主动技能):
    名称 = '旋转源能波'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    攻击段数 = 2
    # 基础 = 1896.00 - 193.16
    # 成长 = 193.16
    # 波动攻击力：<data0>%
    data0 = [int(i*1.13) for i in [0, 284, 314, 342, 371, 400, 429, 457, 487, 516, 544, 573, 602, 632, 660, 689, 718, 746, 775, 805, 834, 862, 891, 920, 950, 978, 1007, 1036, 1064, 1093, 1123,
                                   1152, 1180, 1209, 1238, 1266, 1296, 1325, 1354, 1382, 1411, 1441, 1470, 1498, 1527, 1556, 1584, 1614, 1643, 1672, 1700, 1729, 1759, 1787, 1816, 1845, 1874, 1902, 1932, 1961, 1990]]
    # 源能波攻击力：<data1>%
    data1 = [int(i*1.13) for i in [0, 403, 444, 486, 527, 568, 609, 650, 691, 732, 773, 814, 855, 897, 938, 979, 1020, 1060, 1101, 1142, 1183, 1224, 1265, 1306, 1348, 1389, 1430, 1471, 1512, 1553,
                                   1594, 1635, 1675, 1716, 1757, 1799, 1840, 1881, 1922, 1963, 2004, 2045, 2086, 2127, 2168, 2210, 2251, 2292, 2332, 2373, 2414, 2455, 2496, 2537, 2578, 2619, 2660, 2702, 2743, 2784, 2825]]
    攻击次数2 = 4
    CD = 5
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.13

# 源能护盾，未提炼


class 技能7(职业主动技能):
    名称 = '源能护盾'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 攻击段数 = 2
    data0 = [0, 2996, 3299, 3907, 4210, 4515, 4819, 5122, 5426, 5731, 6035, 6338, 6642, 6946, 7250, 7554, 7858, 8161, 8466, 8770, 9073, 9377, 9681, 9986, 10289, 10593, 10897, 11200, 11505, 11809, 12112, 12416, 12721, 13025, 13328, 13632,
             13936, 14240, 14544, 14848, 15151, 15456, 15760, 16063, 16367, 16671, 16976, 17279, 17583, 17887, 18191, 18495, 18799, 19102, 19406, 19711, 20014, 20318, 20622, 20927, 21230, 21534, 21838, 22141, 22446, 22750, 23053, 23357, 23662, 23965]
    # 基础 = 2996.00 - 310.67
    # 成长 = 310.67
    CD = 8
    TP成长 = 0.08
    TP上限 = 5


# 镭射源能枪
class 技能8(职业主动技能):
    名称 = '镭射源能枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    攻击段数 = 2
    # 基础 = 3116.00 - 316.33
    # 成长 = 316.33
    data0 = [0, 636, 700, 765, 830, 894, 959, 1024, 1088, 1153, 1217, 1281, 1346, 1411, 1476, 1540, 1605, 1670, 1733, 1798, 1863, 1927, 1992, 2057, 2121, 2186, 2251, 2315, 2379, 2444, 2509,
             2573, 2638, 2703, 2767, 2831, 2896, 2960, 3025, 3090, 3155, 3219, 3284, 3349, 3412, 3477, 3542, 3606, 3671, 3736, 3800, 3865, 3929, 3994, 4058, 4123, 4188, 4252, 4317, 4382, 4445]
    攻击次数 = 2
    data1 = [0, 1844, 2031, 2219, 2405, 2593, 2780, 2966, 3154, 3341, 3528, 3715, 3903, 4089, 4277, 4464, 4650, 4838, 5025, 5212, 5399, 5587, 5773, 5961, 6148, 6335, 6522, 6709, 6896, 7083, 7271,
             7457, 7645, 7832, 8020, 8206, 8393, 8581, 8767, 8955, 9142, 9329, 9516, 9704, 9890, 10078, 10265, 10451, 10639, 10826, 11013, 11200, 11388, 11574, 11762, 11949, 12135, 12323, 12510, 12697, 12884]
    攻击次数2 = 1
    CD = 10
    TP成长 = 0.10
    TP上限 = 5


# 源能波刃
class 技能9(职业主动技能):
    名称 = '源能波刃'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 攻击段数 = 11 * 1.073
    # 基础 = 3138.00 - 318.48
    # 成长 = 318.48
    # 斩击攻击力：<data0>%
    data0 = [int(i*1.073) for i in [0, 1726, 1901, 2076, 2252, 2427, 2602, 2777, 2952, 3127, 3302, 3477, 3653, 3829, 4004, 4179, 4354, 4529, 4704, 4879, 5054, 5229, 5404, 5580, 5755, 5930, 6105, 6280, 6456,
                                    6631, 6806, 6981, 7156, 7332, 7507, 7682, 7857, 8032, 8207, 8382, 8557, 8732, 8907, 9083, 9259, 9434, 9609, 9784, 9959, 10134, 10309, 10484, 10659, 10835, 11010, 11185, 11360, 11535, 11710, 11885, 12061]]
    # 吸附攻击力：<data1>%
    data1 = [int(i*1.073) for i in [0, 1412, 1555, 1698, 1842, 1986, 2129, 2272, 2415, 2559, 2702, 2845, 2989, 3132, 3275, 3419, 3562, 3705, 3848, 3992, 4135, 4279, 4422, 4565, 4708, 4851, 4996, 5139,
                                    5282, 5425, 5568, 5711, 5855, 5999, 6142, 6285, 6428, 6571, 6715, 6858, 7002, 7145, 7288, 7431, 7575, 7718, 7861, 8005, 8148, 8292, 8435, 8578, 8721, 8864, 9008, 9152, 9295, 9438, 9581, 9724, 9867]]
    攻击次数2 = 1
    CD = 8
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.073

# 能量飞鱼弹


class 技能10(职业主动技能):
    名称 = '能量飞鱼弹'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 攻击段数 = 1 * 1.102
    data0 = [int(i*1.102) for i in [0, 3254, 3584, 3915, 4245, 4575, 4905, 5236, 5565, 5896, 6226, 6557, 6886, 7217, 7547, 7877, 8207, 8538, 8868, 9198, 9528, 9859, 10188, 10519, 10849, 11180, 11509, 11840, 12170, 12500,
                                    12830, 13161, 13491, 13821, 14151, 14482, 14812, 15142, 15472, 15803, 16132, 16463, 16793, 17124, 17453, 17784, 18114, 18444, 18774, 19105, 19435, 19765, 20095, 20426, 20755, 21086, 21416, 21747, 22076, 22407, 22737]]
    # 基础 = 3254.00 - 330.23
    # 成长 = 330.23
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.102

# 脉冲斩


class 技能11(职业主动技能):
    名称 = '脉冲斩'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 攻击段数 = 8 * 1.101
    # 基础 = 4080.00 - 413.84
    # 成长 = 413.84
    # 多段攻击力：<data0>%
    data0 = [int(i*1.101) for i in [0, 1020, 1123, 1227, 1330, 1434, 1537, 1640, 1744, 1847, 1951, 2054, 2158, 2261, 2364, 2469, 2572, 2676, 2779, 2882, 2986, 3089, 3193, 3296, 3399, 3503, 3606, 3710,
                                    3813, 3918, 4021, 4124, 4228, 4331, 4435, 4538, 4641, 4745, 4848, 4952, 5055, 5158, 5262, 5365, 5470, 5573, 5677, 5780, 5883, 5987, 6090, 6194, 6297, 6400, 6504, 6607, 6711, 6814, 6918, 7022, 7125]]
    攻击次数 = 4
    CD = 10
    TP成长 = 0.10
    TP上限 = 5
    ###
    # 倍率 = 1.101


# 电磁领域
class 技能12(职业主动技能):
    名称 = '电磁领域'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    攻击段数 = 3
    data0 = [0, 934, 1029, 1125, 1220, 1314, 1409, 1504, 1599, 1693, 1788, 1883, 1978, 2073, 2168, 2263, 2358, 2452, 2547, 2642, 2737, 2831, 2926, 3022, 3117, 3212, 3306, 3401, 3496, 3591,
             3685, 3780, 3875, 3971, 4065, 4160, 4255, 4350, 4444, 4539, 4634, 4729, 4825, 4919, 5014, 5109, 5204, 5298, 5393, 5488, 5583, 5677, 5773, 5868, 5963, 6057, 6152, 6247, 6342, 6436, 6531]
    攻击次数 = 5
    data1 = [0, 2003, 2206, 2410, 2613, 2816, 3020, 3223, 3426, 3630, 3833, 4037, 4239, 4442, 4646, 4849, 5052, 5256, 5459, 5662, 5866, 6069, 6272, 6476, 6679, 6882, 7085, 7288, 7492, 7695, 7898, 8102,
             8305, 8508, 8712, 8915, 9118, 9322, 9524, 9728, 9931, 10134, 10338, 10541, 10744, 10948, 11151, 11354, 11558, 11761, 11964, 12167, 12370, 12574, 12777, 12980, 13184, 13387, 13590, 13794, 13997]
    攻击次数2 = 1
    # 基础 = 6673.00 - 677.71
    # 成长 = 677.71
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


# 引力源光弹
class 技能13(职业主动技能):
    名称 = '引力源光弹'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36

    # 基础 = 593 - 60
    # 成长 = 60
    # 攻击次数 = 8 * 1.101

    # 基础2 = 1673 - 170
    # 成长2 = 170
    # 攻击次数2 = 1 * 1.101

    # 多段攻击力：<data0>%
    data0 = [int(i*1.101) for i in [0, 593, 652, 713, 773, 833, 893, 954, 1013, 1074, 1134, 1194, 1255, 1314, 1375, 1435, 1495, 1555, 1616, 1675, 1736, 1795, 1856, 1916, 1976, 2036, 2097, 2157, 2217,
                                    2278, 2337, 2398, 2457, 2518, 2578, 2638, 2698, 2759, 2818, 2879, 2938, 2999, 3060, 3119, 3180, 3240, 3300, 3360, 3421, 3480, 3541, 3600, 3661, 3721, 3781, 3841, 3902, 3962, 4022, 4082, 4142]]
    攻击次数 = 8
    # 爆炸攻击力：<data1>%
    data1 = [int(i*1.101) for i in [0, 1673, 1843, 2012, 2181, 2351, 2521, 2691, 2861, 3030, 3200, 3370, 3540, 3710, 3879, 4049, 4219, 4389, 4559, 4728, 4898, 5068, 5238, 5406, 5576, 5746, 5916, 6086, 6255,
                                    6425, 6595, 6765, 6935, 7104, 7274, 7444, 7614, 7784, 7953, 8123, 8293, 8463, 8633, 8801, 8971, 9141, 9311, 9480, 9650, 9820, 9990, 10160, 10329, 10499, 10669, 10839, 11009, 11178, 11348, 11518, 11688]]
    攻击次数2 = 1

    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    技能施放时间 = 1

    ###
    # 倍率 = 1.101

    是否装备护石 = 0
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            # self.攻击次数2 = 1.28
            self.data1 = [int(i*1.28) for i in self.data1]
            self.是否装备护石 = 1
        elif x == 1:
            self.data1 = [int(i*1.60) for i in self.data1]
            # self.攻击次数2 = 1.60 #修改位置
            self.是否装备护石 = 1


# 光裂斩，护石取最大蓄气
class 技能14(职业主动技能):
    名称 = '光裂斩'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 攻击段数 = 1
    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    # 基础 = 5612 - 569
    # 成长 = 569
    # 攻击次数 = 1

    # 基础2 = 747 - 76
    # 成长2 = 76
    # 攻击次数2 = 5

    # 斩击攻击力：<data0>%
    data0 = [int(i*1.125) for i in [0, 5612, 6181, 6750, 7320, 7889, 8459, 9028, 9597, 10167, 10735, 11305, 11875, 12443, 13013, 13583, 14152, 14721, 15291, 15860, 16429, 16999, 17568, 18138, 18707, 19276, 19846, 20415, 20984,
                                    21554, 22122, 22692, 23262, 23831, 24400, 24970, 25539, 26108, 26678, 27247, 27817, 28386, 28955, 29525, 30094, 30663, 31233, 31803, 32371, 32941, 33510, 34079, 34649, 35218, 35787, 36357, 36926, 37496, 38065, 38634, 39204]]
    # 能量多段攻击力：<data1>%
    data1 = [int(i*1.125) for i in [0, 747, 823, 899, 975, 1051, 1127, 1204, 1280, 1354, 1430, 1507, 1583, 1659, 1735, 1811, 1887, 1963, 2038, 2114, 2190, 2266, 2342, 2418, 2494, 2570, 2646, 2721, 2797,
                                    2873, 2949, 3025, 3101, 3177, 3253, 3329, 3404, 3480, 3556, 3632, 3708, 3784, 3860, 3937, 4013, 4087, 4163, 4240, 4316, 4392, 4468, 4544, 4620, 4695, 4771, 4847, 4923, 4999, 5075, 5151, 5227]]
    攻击次数2 = 5

    ###
    # 倍率 = 1.125

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data0 = [int(i*1.98*1.06) for i in self.data0]
            # self.攻击次数 = 1.98 * 1.06
            self.攻击次数2 = 0
        elif x == 1:
            self.data0 = [int(i*1.98*1.14) for i in self.data0]
            # self.攻击次数 = 1.98 * 1.14#修改位置
            self.攻击次数2 = 0

# 光导裂地斩


class 技能15(职业主动技能):
    名称 = '光导裂地斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 攻击段数 = 6
    # 基础 = 6247 - 633.5
    # 成长 = 633.5
    # 攻击次数 = 1

    # 基础2 = 9512 - 965
    # 成长2 = 965
    # 攻击次数2 = 1
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    # 下劈攻击力：<data0>%
    data0 = [int(i*1.121) for i in [0, 6247, 6880, 7514, 8148, 8782, 9415, 10050, 10683, 11317, 11951, 12585, 13218, 13852, 14486, 15119, 15754, 16387, 17021, 17655, 18289, 18922, 19557, 20190, 20824, 21458, 22091, 22725, 23359,
                                    23993, 24626, 25261, 25894, 26528, 27161, 27796, 28429, 29062, 29697, 30330, 30964, 31598, 32232, 32865, 33500, 34133, 34767, 35401, 36035, 36668, 37302, 37936, 38569, 39204, 39837, 40471, 41105, 41739, 42372, 43007, 43640]]
    # 上挑攻击力：<data1>%
    data1 = [int(i*1.121) for i in [0, 9512, 10477, 11442, 12406, 13371, 14337, 15302, 16267, 17232, 18197, 19162, 20127, 21092, 22056, 23022, 23987, 24952, 25917, 26882, 27847, 28812, 29777, 30742, 31706, 32672, 33637, 34602, 35567,
                                    36532, 37497, 38462, 39427, 40392, 41358, 42322, 43287, 44252, 45217, 46182, 47147, 48112, 49077, 50043, 51008, 51972, 52937, 53902, 54867, 55832, 56797, 57762, 58728, 59693, 60658, 61623, 62587, 63552, 64517, 65482, 66447]]
    攻击次数2 = 1

    ###
    # 倍率 = 1.121

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.17
            self.攻击次数2 *= 1.2
        elif x == 1:
            self.攻击次数 *= 1.17
            self.攻击次数2 *= 1.33  # 修改位置


# 一觉，非提炼
class 技能16(职业主动技能):
    名称 = '超能场域'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 能量多段攻击力：<data0>%
    data0 = [int(i*1.128) for i in [0, 567, 698, 829, 960, 1092, 1224, 1355, 1487, 1617, 1749, 1881, 2012, 2144, 2276, 2406, 2538, 2669, 2801,
                                    2933, 3064, 3195, 3326, 3458, 3590, 3721, 3853, 3983, 4115, 4247, 4378, 4510, 4642, 4773, 4904, 5035, 5167, 5299, 5430, 5562, 5692]]
    # 秒C的段数
    攻击次数 = 14
    # 能量爆炸攻击力：<data1>%
    data1 = [int(i*1.128) for i in [0, 28858, 35550, 42241, 48933, 55625, 62317, 69010, 75702, 90632, 97994, 105355, 112716, 120077, 127438, 134799, 142160, 149521, 156883, 164244,
                                    171605, 178965, 186326, 193687, 201048, 208409, 215770, 223131, 230493, 237854, 245215, 252576, 259937, 267298, 274659, 282020, 289382, 296743, 304104, 311465, 318826]]
    攻击次数2 = 1
    # 攻击段数 = 13
    # 基础 = 2012 - 12 * 131.4
    # 成长 = 131.4
    # 攻击次数 = 13

    # 基础2 = 112716 - 7361 * 12
    # 成长2 = 7361
    # 攻击次数2 = 1
    CD = 145
    ###
    # 倍率 = 1.128

# 能量禁锢


class 技能17(主动技能):
    名称 = '能量禁锢'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23

    CD = 25
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    基础 = 792 - 81
    成长 = 81
    攻击次数 = 10

    基础2 = 3397 - 344.5
    成长2 = 344.5
    攻击次数2 = 1
    ###
    倍率 = 1.126

    # 爆炸次数 = 0
    是否装备护石 = 0
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 14 * 0.8  # 14是测试结论
            self.是否装备护石 = 1
            # self.攻击次数2 += self.爆炸次数* 0.33
        elif x == 1:
            self.攻击次数 = 14 * 0.89  # 修改位置
            self.是否装备护石 = 1
            # self.攻击次数2 += self.爆炸次数 *0.33


# 离散能量波

class 技能18(主动技能):
    名称 = '离散能量波'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18

    基础 = 1658 - 168.5
    成长 = 168.5
    攻击次数 = 10

    基础2 = 7109 - 721.5
    成长2 = 721.5
    攻击次数2 = 1

    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    ###
    倍率 = 1.114

    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数 = 15 * 0.75
            self.攻击次数2 *= 1.4
        elif x == 1:
            self.CD *= 0.9
            self.攻击次数 = 15 * 0.75
            self.攻击次数2 *= 1.66  # 修改位置

# 绝望圆舞


class 技能19(职业主动技能):
    名称 = '绝望圆舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 攻击段数 = 8
    # 基础 = 38894.00 - 3946.60
    # 成长 = 3946.60
    CD = 40
    ###
    # 倍率 = 1.121

    # 乱舞攻击力：<data0>% X 8次
    data0 = [int(i*1.121) for i in [0, 3403, 3748, 4094, 4439, 4784, 5129, 5475, 5821, 6166, 6512, 6857, 7202, 7547, 7893, 8238, 8583, 8928, 9274, 9619, 9964, 10309, 10655, 11000, 11345, 11691, 12037, 12382, 12727, 13072,
                                    13418, 13763, 14108, 14453, 14799, 15144, 15489, 15834, 16180, 16525, 16870, 17216, 17562, 17907, 18252, 18598, 18943, 19288, 19633, 19979, 20324, 20669, 21014, 21360, 21705, 22050, 22395, 22741, 23086, 23431, 23777]]
    攻击次数 = 8
    # 最后一击攻击力：<data1>%
    data1 = [int(i*1.121) for i in [0, 11670, 12853, 14038, 15221, 16406, 17589, 18774, 19957, 21142, 22325, 23509, 24693, 25877, 27061, 28245, 29429, 30613, 31797, 32981, 34165, 35349, 36532, 37717, 38900, 40085, 41268, 42452, 43636,
                                    44820, 46004, 47188, 48372, 49555, 50740, 51923, 53108, 54291, 55476, 56659, 57844, 59027, 60212, 61395, 62579, 63763, 64947, 66131, 67315, 68499, 69683, 70867, 72051, 73235, 74419, 75603, 76787, 77970, 79154, 80338, 81522]]
    攻击次数2 = 1

    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35

# CEAB-2超能爆发，满蓄


class 技能20(职业主动技能):
    名称 = 'CEAB-2超能爆发'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 攻击段数 = 1
    # 基础 = 44464.00 - 4510.92
    # 成长 = 4510.92
    # 爆炸攻击力：
    # data0 = [0, 40341, 44434, 48526, 52619, 56710, 60803, 64895, 68988, 73081, 77173, 81266, 85359, 89451, 93544, 97636, 101729, 105822, 109914, 114007, 118099, 122192, 126285, 130377, 134470, 138562, 142655, 146748, 150840, 154933, 159025, 163118, 167211, 171303, 175396, 179488, 183581, 187673, 191765, 195858, 199950, 204043, 208136, 212228, 216321, 220413, 224506, 228599, 232691, 236784, 240876, 244969, 249062, 253154, 257247, 261340, 265432, 269525, 273617, 277710, 281803]
    # 最大蓄气时的爆炸攻击力：
    data0 = [int(i*1.074) for i in [0, 44464, 48975, 53486, 57998, 62508, 67019, 71530, 76041, 80552, 85063, 89574, 94084, 98595, 103106, 107617, 112128, 116639, 121150, 125660, 130171, 134683, 139194, 143705, 148216, 152727, 157238, 161748, 166259, 170770,
                                    175281, 179792, 184303, 188814, 193324, 197835, 202346, 206857, 211368, 215880, 220391, 224902, 229412, 233923, 238434, 242945, 247456, 251967, 256478, 260988, 265499, 270010, 274521, 279032, 283543, 288054, 292566, 297076, 301587, 306098, 310609]]

    CD = 45
    ###
    # 倍率 = 1.074
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.39
            self.CD *= 0.9

# 二觉，1.5秒后c


class 技能21(职业主动技能):
    名称 = '终焉：超世界崩坏'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 攻击段数 = 17

    # 基础 = 1800 - 216.33333 * 5
    # 成长 = 216.33333
    # 攻击次数 = 6

    # 基础2 = 168632 - 20286.5 *5
    # 成长2 = 20286.5
    # 攻击次数2 = 1
    # 多段攻击力：<data0>%
    # 秒C6段，打满14次
    data0 = [int(i*1.1) for i in [0, 934, 1149, 1366, 1583, 1800, 2015, 2232, 2449, 2666, 2882, 3098, 3315, 3531, 3748, 3965, 4182, 4397, 4614, 4831, 5048, 5263, 5480, 5697, 5913, 6130, 6346, 6563, 6779, 6996,
                                  7213, 7428, 7645, 7862, 8079, 8295, 8511, 8728, 8945, 9161, 9378, 9594, 9810, 10027, 10244, 10461, 10676, 10893, 11110, 11327, 11543, 11759, 11976, 12192, 12409, 12626, 12842, 13058, 13275, 13492, 13709]]
    攻击次数 = 6
    # 爆炸攻击力：<data1>%
    data1 = [int(i*1.1) for i in [0, 87485, 107772, 128059, 148345, 168632, 188919, 209205, 229492, 249779, 270064, 290351, 310638, 330924, 351211, 371498, 391784, 412071, 432358, 452644, 472931, 493218, 513504, 533790, 554077, 574363, 594650, 614937, 635223, 655510,
                                  675797, 696083, 716370, 736657, 756943, 777229, 797516, 817802, 838089, 858376, 878662, 898949, 919236, 939522, 959809, 980096, 1000382, 1020669, 1040955, 1061241, 1081528, 1101815, 1122101, 1142388, 1162675, 1182961, 1203248, 1223535, 1243821, 1264108, 1284395]]
    攻击次数2 = 1
    CD = 180
    ###
    # 倍率 = 1.1

# 95


class 技能22(主动技能):
    名称 = '裂变黑核'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 16667 - 1691
    成长 = 1691
    攻击次数 = 5
    基础2 = 92596 - 9393
    成长2 = 9393
    攻击次数2 = 0  # 1
    CD = 60  # 大概

# 三觉


class 技能23(主动技能):
    名称 = '黑之地平线'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 308490 - 71581
    成长 = 71581
    攻击次数 = 1
    CD = 290  # 大概
    关联技能 = ['无']

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

苍暮·源能专家一觉序号 = 0
苍暮·源能专家二觉序号 = 0
苍暮·源能专家三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        苍暮·源能专家一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        苍暮·源能专家二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        苍暮·源能专家三觉序号 = 技能序号[i.名称]

苍暮·源能专家护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        苍暮·源能专家护石选项.append(i.名称)

苍暮·源能专家符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        苍暮·源能专家符文选项.append(i.名称)


class 苍暮·源能专家角色属性(角色属性):
    实际名称 = '苍暮·源能专家'
    角色 = '枪剑士'
    职业 = '源能专家'

    武器选项 = ['源力剑']

    类型选择 = ['魔法百分比']

    类型 = '魔法百分比'
    防具类型 = '布甲'
    防具精通属性 = ['智力']

    主BUFF = 2.0

    远古记忆 = 0

    引力源光弹充能次数 = 0
    能量禁锢爆炸次数 = 0

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        if self.装备检查('谍影：超级核心'):
            self.技能栏[self.技能序号['源力剑精通']].谍影专用倍率 = 2

        super().被动倍率计算()

    def 数据计算(self, x=0, y=-1):
        self.预处理()
        # 初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)

        # 能量禁锢护石
        if self.技能栏[self.技能序号['能量禁锢']].是否装备护石 == 1:
            技能单次伤害[self.技能序号['能量禁锢']] += (0.33*self.能量禁锢爆炸次数)*(self.技能栏[self.技能序号['能量禁锢']].基础2 + self.技能栏[self.技能序号['能量禁锢']].成长2 * self.技能栏[self.技能序号['能量禁锢']].等级)*(
                1 + self.技能栏[self.技能序号['能量禁锢']].TP成长 * self.技能栏[self.技能序号['能量禁锢']].TP等级) * self.技能栏[self.技能序号['能量禁锢']].倍率 * self.伤害指数*i.被动倍率

        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        # 引力源光弹护石
        if self.技能栏[self.技能序号['引力源光弹']].是否装备护石 == 1:
            if self.宠物次数[self.技能序号['引力源光弹']] < self.引力源光弹充能次数:
                技能总伤害[self.技能序号['CEAB-2超能爆发']] += (技能单次伤害[self.技能序号['引力源光弹']] * 0.3 * self.引力源光弹充能次数 * (
                    1+self.白兔子技能*0.20 + self.年宠技能*0.10*self.宠物次数[self.技能序号['引力源光弹']]/self.引力源光弹充能次数+self.斗神之吼秘药*0.12))
            else:
                技能总伤害[self.技能序号['CEAB-2超能爆发']] += (技能单次伤害[self.技能序号['引力源光弹']] * 0.3 * self.引力源光弹充能次数 * (
                    1+self.白兔子技能*0.20 + self.年宠技能*0.10+self.斗神之吼秘药*0.12))

        # 返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)


class 苍暮·源能专家(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 苍暮·源能专家角色属性()
        self.角色属性A = 苍暮·源能专家角色属性()
        self.角色属性B = 苍暮·源能专家角色属性()
        self.一觉序号 = 苍暮·源能专家一觉序号
        self.二觉序号 = 苍暮·源能专家二觉序号
        self.三觉序号 = 苍暮·源能专家三觉序号
        self.护石选项 = deepcopy(苍暮·源能专家护石选项)
        self.符文选项 = deepcopy(苍暮·源能专家符文选项)
        QMessageBox.information(self, "提示",  "4.7日测试服数据，仅供参考")

    def 引力源光弹充能次数判断(self, 警告, 选项变更):
        引力源光弹次数 = 0
        超能爆发次数 = 0

        if self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText() != '/CD':
            try:
                引力源光弹次数 = int(
                    self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText())
            except:
                引力源光弹次数 = 100
        else:
            引力源光弹次数 = 100
        if self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText() != '/CD':
            超能爆发次数 = int(
                self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText())
        else:
            超能爆发次数 = 100

        sign = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '引力源光弹' and 引力源光弹次数 != 0 and 超能爆发次数 != 0:
                sign = 1

        充能次数上限 = 1
        if 引力源光弹次数 != 0 and 超能爆发次数 != 0 and (self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText() != '/CD' or self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText() != '/CD'):
            if 超能爆发次数 >= 引力源光弹次数:
                充能次数上限 = 引力源光弹次数
            else:
                充能次数上限 = 超能爆发次数
            # self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
        if self.引力源光弹护石选项.currentIndex() > 充能次数上限 and sign == 1 and (self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText() != '/CD' or self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText() != '/CD') and 警告 == 0:
            self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
            if 选项变更 == 0:
                QMessageBox.information(self, "错误",  "输入的充能次数超过上限，已自动修正")
            警告 = 1
        elif self.引力源光弹护石选项.currentIndex() < 充能次数上限 and sign == 1 and (self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText() != '/CD' or self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText() != '/CD') and 选项变更 == 1:
            self.引力源光弹护石选项.setCurrentIndex(充能次数上限)
            选项变更 = 0
        elif self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentText() == '/CD' and self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']].currentText() == '/CD' and 选项变更 == 1:
            self.引力源光弹护石选项.setCurrentIndex(1)

        if sign == 0:
            self.引力源光弹护石选项.setEnabled(False)
            self.引力源光弹护石选项.setStyleSheet(下拉框样式)
            self.引力源光弹护石选项.setCurrentIndex(0)
        else:
            self.引力源光弹护石选项.setEnabled(True)
            self.引力源光弹护石选项.setStyleSheet(下拉框样式)
    flag1 = 0
    flag2 = 0
    flag3 = 0

    def 能量禁锢爆炸次数判断(self, 警告):
        能量禁锢次数 = 0
        能量飞鱼弹次数 = 0
        源能护盾次数 = 0

        if self.次数输入[self.角色属性A.技能序号['能量禁锢']].currentText() != '/CD':
            try:
                能量禁锢次数 = int(self.次数输入[self.角色属性A.技能序号['能量禁锢']].currentText())
            except:
                能量禁锢次数 = 1
        else:
            能量禁锢次数 = 1
        if self.次数输入[self.角色属性A.技能序号['能量飞鱼弹']].currentText() != '/CD':
            try:
                能量飞鱼弹次数 = int(
                    self.次数输入[self.角色属性A.技能序号['能量飞鱼弹']].currentText())

            except:
                能量飞鱼弹次数 = 2
        else:
            能量飞鱼弹次数 = 2
        if self.次数输入[self.角色属性A.技能序号['源能护盾']].currentText() != '/CD':
            try:
                源能护盾次数 = int(self.次数输入[self.角色属性A.技能序号['源能护盾']].currentText())
            except:
                源能护盾次数 = 2
        else:
            源能护盾次数 = 2

        sign2 = 0
        for x in range(3):
            if self.护石栏[x].currentText() == '能量禁锢' and 能量禁锢次数 != 0 and (能量飞鱼弹次数+源能护盾次数) != 0:
                sign2 = 1

        护石 = []
        for i in range(3):
            护石.append(self.护石栏[i].currentText())
        if "能量禁锢" in 护石:
            self.flag1 = 1
        elif "能量禁锢" not in 护石:
            self.flag1 = 0
        if self.flag1 == 1 and self.flag2 == 0:
            self.flag2 = 1
            self.flag3 = 1
        elif self.flag1 == 1 and self.flag2 == 1:
            self.flag3 = 0
        if self.flag1 == 0 and self.flag2 == 1:
            self.flag2 = 0
        if self.flag3 == 1:
            警告 = False
        护石 = []

        if 能量禁锢次数 != 0:
            if 能量禁锢次数 == 1:
                if(能量飞鱼弹次数+源能护盾次数) >= 2:
                    self.能量禁锢护石选项.setCurrentIndex(2)
                else:
                    self.能量禁锢护石选项.setCurrentIndex(能量飞鱼弹次数+源能护盾次数)
            else:
                self.能量禁锢护石选项.setCurrentIndex(2)
        else:
            self.能量禁锢护石选项.setCurrentIndex(0)
        if (能量飞鱼弹次数+源能护盾次数) < (能量禁锢次数*2) and sign2 == 1 and 警告 == False and (self.次数输入[self.角色属性A.技能序号['源能护盾']].currentText() != '/CD' and self.次数输入[self.角色属性A.技能序号['能量飞鱼弹']].currentText() != '/CD'):
            QMessageBox.information(
                self, "错误",  "能量飞鱼弹与源能护盾次数不足以为能量禁锢提供"+str(能量禁锢次数*2)+"次爆炸，建议修改技能及爆炸次数，若不修改则按输入的数值计算")
            警告 = True

        if sign2 == 0:
            self.能量禁锢护石选项.setEnabled(False)
            self.能量禁锢护石选项.setStyleSheet(下拉框样式)
            self.能量禁锢护石选项.setCurrentIndex(0)
        else:
            self.能量禁锢护石选项.setEnabled(True)
            self.能量禁锢护石选项.setStyleSheet(下拉框样式)

    def 界面(self):
        super().界面()

        self.引力源光弹护石选项 = MyQComboBox(self.main_frame2)
        for i in range(100):
            self.引力源光弹护石选项.addItem('引力源光弹充能次数：'+str(i))
        self.引力源光弹护石选项.resize(160, 20)
        self.引力源光弹护石选项.move(300, 480)
        self.引力源光弹护石选项.setCurrentIndex(1)
        self.引力源光弹护石选项.setToolTip(
            '修改对CEAB-2进行充能的次数，每次CEAB-2上限一次，受宠物技能影响。仅佩戴引力源光弹护石时生效')

        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(
                lambda state: self.引力源光弹充能次数判断(警告=1, 选项变更=1))
        self.次数输入[self.角色属性A.技能序号['引力源光弹']].currentIndexChanged.connect(
            lambda state: self.引力源光弹充能次数判断(警告=0, 选项变更=1))
        self.次数输入[self.角色属性A.技能序号['CEAB-2超能爆发']
                  ].currentIndexChanged.connect(lambda state: self.引力源光弹充能次数判断(警告=0, 选项变更=1))
        self.引力源光弹护石选项.currentIndexChanged.connect(
            lambda state: self.引力源光弹充能次数判断(警告=0, 选项变更=0))

        self.能量禁锢护石选项 = MyQComboBox(self.main_frame2)
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：0')
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：1')
        self.能量禁锢护石选项.addItem('能量禁锢爆炸次数：2')
        self.能量禁锢护石选项.resize(160, 20)
        self.能量禁锢护石选项.move(300, 390)
        self.能量禁锢护石选项.setCurrentIndex(2)
        self.能量禁锢护石选项.setToolTip('修改每次能量禁锢爆炸次数，与源能护盾、能量飞鱼弹释放次数关联，仅佩戴能量禁锢护石时生效')
        # bldic = {True:1,False:0}
        for i in range(3):
            self.护石栏[i].currentIndexChanged.connect(
                lambda state: self.能量禁锢爆炸次数判断(警告=True))

        self.次数输入[self.角色属性A.技能序号['能量禁锢']].currentIndexChanged.connect(
            lambda state: self.能量禁锢爆炸次数判断(警告=False))
        self.次数输入[self.角色属性A.技能序号['能量飞鱼弹']].currentIndexChanged.connect(
            lambda state: self.能量禁锢爆炸次数判断(警告=False))
        self.次数输入[self.角色属性A.技能序号['源能护盾']].currentIndexChanged.connect(
            lambda state: self.能量禁锢爆炸次数判断(警告=False))

        # 裂变黑核蓄力判断

        self.裂变黑核蓄力选项 = QCheckBox('裂变黑核蓄力释放', self.main_frame2)
        self.裂变黑核蓄力选项.resize(160, 20)
        self.裂变黑核蓄力选项.move(320, 540)
        self.裂变黑核蓄力选项.setStyleSheet(复选框样式)
        self.裂变黑核蓄力选项.setToolTip('蓄力释放裂变黑核')
        self.裂变黑核蓄力选项.setChecked(True)

        self.职业存档.append(('引力源光弹护石选项', self.引力源光弹护石选项, 1))
        self.职业存档.append(('能量禁锢护石选项', self.能量禁锢护石选项, 1))
        self.职业存档.append(('裂变黑核蓄力选项', self.裂变黑核蓄力选项, 0))

    def 输入属性(self, 属性, x=0):
        super().输入属性(属性, x)

        属性.引力源光弹充能次数 = self.引力源光弹护石选项.currentIndex()
        # 属性.技能栏[属性.技能序号['能量禁锢']].爆炸次数 = self.能量禁锢护石选项.currentIndex()
        属性.能量禁锢爆炸次数 = self.能量禁锢护石选项.currentIndex()

        if self.裂变黑核蓄力选项.isChecked():
            属性.技能栏[属性.技能序号['裂变黑核']].攻击次数 = 0
            属性.技能栏[属性.技能序号['裂变黑核']].攻击次数2 = 1
