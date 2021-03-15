from PublicReference.base import *

class 技能0(主动技能):
    名称 = '烟尘弹'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 365
    成长 = 41
    攻击次数 = 6
    CD = 6
    TP成长 = 0.08
    TP上限 = 7


class 技能1(主动技能):
    名称 = '刺踢'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    #物理攻击力：<data0>%
    data0 = [ int(i*1.0*1.167) for i in [0, 1989, 2190, 2393, 2594, 2795, 2998, 3199, 3402, 3603, 3804, 4007, 4209, 4412, 4613, 4814, 5017, 5218, 5421, 5622, 5823, 6026, 6227, 6430, 6631, 6832, 7035, 7236, 7439, 7640, 7844, 8045, 8246, 8449, 8650, 8853, 9054, 9255, 9458, 9659, 9861, 10063, 10264, 10467, 10668, 10870, 11072, 11273, 11475, 11677, 11879, 12081, 12282, 12484, 12686, 12888, 13089, 13291, 13493, 13695, 13897, 14098, 14300, 14502, 14704, 14906, 15107, 15310, 15512, 15714, 15916]]
    CD = 4.4
    TP成长 = 0.08
    TP上限 = 5


class 技能2(主动技能):
    名称 = '致命射击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    # 基础 = 1281.30 
    # 成长 = 144.70  
    CD = 6.2
    TP成长 = 0.1
    TP上限 = 5
    data0 = [ int(i*1.0*1.121) for i in [0, 1426, 1570, 1715, 1860, 2005, 2149, 2294, 2439, 2583, 2728, 2873, 3017, 3162, 3307, 3452, 3596, 3741, 3886, 4030, 4175, 4320, 4464, 4609, 4754, 4899, 5043, 5188, 5333, 5477, 5622, 5767, 5911, 6056, 6201, 6346, 6490, 6635, 6780, 6924, 7069, 7214, 7358, 7503, 7648, 7792, 7937, 8082, 8227, 8371, 8516, 8661, 8805, 8950, 9095, 9239, 9384, 9529, 9674, 9818, 9963, 10108, 10252, 10397, 10542, 10686, 10831, 10976, 11121, 11265, 11410]]
    攻击次数 = 1

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能3(被动技能):
    名称 = '左轮奥义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)


class 技能4(被动技能):
    名称 = '花式枪术'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 10:
                return round(1 + 0.01 * self.等级, 5)
            else:
                return round(1.1 + 0.02 * (self.等级 - 10), 5)

class 技能5(主动技能):
    名称 = '锁链截击'
    所在等级 = 25
    学习间隔 = 3
    SP消耗 = 25
    等级上限 = 60
    学习上限 = 50
    基础等级 = min(int((105 - 所在等级) / 学习间隔 + 1), 学习上限)
    CD = 5.0
    data = [
    #0  第1击多段攻击力 : <data0>%
        [ int(i*1.0) for i in [0, 556, 645, 734, 822, 911, 1000, 1089, 1177, 1266, 1355, 1444, 1532, 1621, 1710, 1799, 1887, 1976, 2065, 2154, 2242, 2331, 2420, 2509, 2597, 2686, 2775, 2863, 2952, 3041, 3130, 3218, 3307, 3396, 3485, 3573, 3662, 3751, 3840, 3928, 4017, 4106, 4195, 4283, 4372, 4461, 4550, 4638, 4727, 4816, 4905, 4993, 5082, 5171, 5260, 5348, 5437, 5526, 5615, 5703, 5792]],
    #1  第2击攻击力 : <data1>%
        [ int(i*1.0) for i in [0, 834, 968, 1101, 1234, 1367, 1500, 1633, 1766, 1899, 2033, 2166, 2299, 2432, 2565, 2698, 2831, 2964, 3097, 3231, 3364, 3497, 3630, 3763, 3896, 4029, 4162, 4295, 4429, 4562, 4695, 4828, 4961, 5094, 5227, 5360, 5494, 5627, 5760, 5893, 6026, 6159, 6292, 6425, 6558, 6692, 6825, 6958, 7091, 7224, 7357, 7490, 7623, 7757, 7890, 8023, 8156, 8289, 8422, 8555, 8688]],
    #2  第3击攻击力 : <data2>%
        [ int(i*1.0) for i in [0, 834, 968, 1101, 1234, 1367, 1500, 1633, 1766, 1899, 2033, 2166, 2299, 2432, 2565, 2698, 2831, 2964, 3097, 3231, 3364, 3497, 3630, 3763, 3896, 4029, 4162, 4295, 4429, 4562, 4695, 4828, 4961, 5094, 5227, 5360, 5494, 5627, 5760, 5893, 6026, 6159, 6292, 6425, 6558, 6692, 6825, 6958, 7091, 7224, 7357, 7490, 7623, 7757, 7890, 8023, 8156, 8289, 8422, 8555, 8688]],
    ]

    #index：   0      1      2      
    rate = [1.000, 1.000, 1.000]
    hits = [5.000, 1.000, 1.000]

    def 等效百分比(self, 武器类型):
        sum = 0
        for i in range(len(self.hits)):
            sum += self.data[i][self.等级] * self.rate[i] * self.hits[i]
        return self.倍率 * sum

"""
数据描述(已匹配)：
第1击多段攻击力 : <data0>%
第1击多段攻击间隔 : 0.2秒
第2击攻击力 : <data1>%
第3击攻击力 : <data2>%
技能描述：
    使枪刃往垂直方向旋转， 并聚集周围的敌人。 施放技能时， 若再次激活技能键， 则可以将敌人推开； 若此时第二次激活技能键， 则可以将推开的敌人吸附到身边。
    #95被动新增:
    锁链截击
    删除第一打的多段攻击力，使用时发动2，3打后向前方射击.
    射击攻击力为1打多段攻击力的一定比率.
"""



class 技能6(主动技能):
    名称 = '音速劫击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2789.63
    成长 = 315.38
    CD = 4.4
    TP成长 = 0.1
    TP上限 = 5
    data0 = [ int(i*1.0*1.158) for i in [0, 1035, 1141, 1246, 1351, 1456, 1561, 1666, 1771, 1876, 1981, 2087, 2192, 2297, 2402, 2507, 2612, 2717, 2822, 2927, 3032, 3138, 3243, 3348, 3453, 3558, 3663, 3768, 3873, 3978, 4083, 4189, 4294, 4399, 4504, 4609, 4714, 4819, 4924, 5029, 5134, 5240, 5345, 5450, 5555, 5660, 5765, 5870, 5975, 6080, 6185, 6291, 6396, 6501, 6606, 6711, 6816, 6921, 7026, 7131, 7236, 7342, 7447, 7552, 7657, 7762, 7867, 7972, 8077, 8182, 8287]]
    攻击次数 = 3

    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
"""
#95被动新增:
音速截击
突进攻击不再浮空，在突进攻击完成后向后射击.
射击攻击力为突进攻击力的一定比率.
"""

class 技能7(主动技能):
    名称 = '致命回射'
    所在等级 = 30
    等级上限 = 1
    基础等级 = 1
    CD = 12.5

class 技能8(主动技能):
    名称 = '枪舞'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 212.00
    # 成长 = 24.00
    data0 = [ int(i*1.0*1.158) for i in [0, 236, 260, 284, 308, 332, 356, 380, 404, 428, 452, 476, 500, 524, 548, 572, 596, 620, 644, 668, 692, 716, 740, 764, 788, 812, 836, 860, 884, 908, 932, 956, 980, 1004, 1028, 1052, 1076, 1100, 1124, 1148, 1172, 1196, 1220, 1244, 1268, 1292, 1316, 1340, 1364, 1388, 1412, 1436, 1461, 1485, 1509, 1533, 1557, 1581, 1605, 1629, 1653, 1677, 1701, 1725, 1749, 1773, 1797, 1821, 1845, 1869, 1893] ]
    攻击次数 = 20
    # 基础2 = 377.30
    # 成长2 = 42.70
    data1 = [ int(i*1.0*1.158) for i in [0, 420, 463, 506, 548, 591, 634, 676, 719, 762, 804, 847, 890, 932, 975, 1018, 1060, 1103, 1146, 1188, 1231, 1274, 1316, 1359, 1402, 1444, 1487, 1530, 1573, 1615, 1658, 1701, 1743, 1786, 1829, 1871, 1914, 1957, 1999, 2042, 2085, 2127, 2170, 2213, 2255, 2298, 2341, 2383, 2426, 2469, 2511, 2554, 2597, 2640, 2682, 2725, 2768, 2810, 2853, 2896, 2938, 2981, 3024, 3066, 3109, 3152, 3194, 3237, 3280, 3322, 3365]]
    攻击次数2 = 9
    CD = 17.6
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.9
            self.攻击次数 = 0
            self.攻击次数2 *= (2 * 1.39)
        elif x == 1:
            self.CD *= 0.9
            self.攻击次数 = 0
            self.攻击次数2 *= (2 * 1.49)
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率+self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能9(主动技能):
    名称 = '移动射击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [ int(i*1.0*1.129) for i in [0, 431, 474, 518, 562, 605, 649, 693, 737, 780, 824, 868, 912, 955, 999, 1043, 1087, 1130, 1174, 1218, 1261, 1305, 1349, 1393, 1436, 1480, 1524, 1568, 1611, 1655, 1699, 1743, 1786, 1830, 1874, 1917, 1961, 2005, 2049, 2092, 2136, 2180, 2224, 2267, 2311, 2355, 2398, 2442, 2486, 2530, 2573, 2617, 2661, 2705, 2748, 2792, 2836, 2880, 2923, 2967, 3011, 3054, 3098, 3142, 3186, 3229, 3273, 3317, 3361, 3404, 3448]]
    攻击次数 = 30
    # 基础 = 11618.00
    # 成长 = 1312.00
    CD = 24.3
    TP成长 = 0.10
    TP上限 = 5
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率
class 技能10(主动技能):
    名称 = '多重射击'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 基础 = 7723.15
    # 成长 = 871.85
    data0 = [ int(i*1.0*1.21) for i in [0, 1719, 1893, 2067, 2242, 2416, 2591, 2765, 2939, 3114, 3288, 3463, 3637, 3811, 3986, 4160, 4335, 4509, 4683, 4858, 5032, 5207, 5381, 5555, 5730, 5904, 6079, 6253, 6427, 6602, 6776, 6951, 7125, 7299, 7474, 7648, 7823, 7997, 8171, 8346, 8520, 8695, 8869, 9043, 9218, 9392, 9567, 9741, 9915, 10090, 10264, 10439, 10613, 10787, 10962, 11136, 11311, 11485, 11659, 11834, 12008, 12183, 12357, 12531, 12706, 12880, 13055, 13229, 13403, 13578, 13752]]
    攻击次数 = 5
    CD = 19.8
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 = 1.18
        elif x == 1:
            self.倍率 = 1.27
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能11(主动技能):
    名称 = '双鹰回旋'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 464.17
    # 成长 = 54.83
    # 基础2 = 474.00
    # 成长2 = 56.00
    # 基础3 = 502.58
    # 成长3 = 59.42
     #第1次物理攻击力：<data0>%
    data0 = [ int(i*1.0) for i in [0, 519, 571, 624, 676, 729, 782, 834, 887, 940, 992, 1045, 1097, 1151, 1203, 1255, 1308, 1361, 1414, 1466, 1518, 1572, 1624, 1677, 1729, 1783, 1835, 1887, 1940, 1993, 2046, 2098, 2150, 2204, 2256, 2309, 2361, 2415, 2467, 2519, 2572, 2625, 2678, 2730, 2782, 2836, 2888, 2940, 2993, 3046, 3099, 3151, 3203, 3257, 3309, 3362, 3414, 3468, 3520, 3572, 3625, 3678, 3731, 3783, 3835, 3889, 3941, 3994, 4046, 4100, 4152]]
    #第2次物理攻击力：<data1>%
    data1 = [ int(i*1.0) for i in [0, 530, 583, 637, 691, 745, 798, 852, 907, 960, 1014, 1067, 1121, 1176, 1229, 1283, 1336, 1390, 1445, 1498, 1552, 1605, 1659, 1714, 1767, 1821, 1874, 1928, 1983, 2036, 2090, 2143, 2197, 2251, 2305, 2359, 2412, 2466, 2520, 2574, 2628, 2681, 2735, 2789, 2843, 2896, 2950, 3004, 3058, 3112, 3165, 3219, 3273, 3327, 3381, 3434, 3488, 3543, 3596, 3650, 3703, 3757, 3812, 3865, 3919, 3972, 4026, 4081, 4134, 4188, 4241]]
    #第3次物理攻击力：<data2>%
    data2 = [ int(i*1.0) for i in [0, 562, 619, 676, 733, 790, 847, 904, 962, 1019, 1076, 1133, 1190, 1247, 1303, 1360, 1417, 1474, 1532, 1589, 1646, 1703, 1760, 1817, 1874, 1931, 1988, 2046, 2103, 2160, 2217, 2274, 2331, 2388, 2444, 2501, 2559, 2616, 2673, 2730, 2787, 2844, 2901, 2958, 3015, 3073, 3130, 3187, 3244, 3301, 3358, 3415, 3472, 3530, 3585, 3643, 3700, 3757, 3814, 3871, 3928, 3985, 4042, 4100, 4157, 4214, 4271, 4328, 4385, 4442, 4499]]
    攻击次数 = 14
    攻击次数2 = 18
    攻击次数3 = 32
    CD = 44.6
    TP成长 = 0.10
    TP基础 = 5
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 0
            self.攻击次数2 = 24
            self.攻击次数3 = 46
            # self.倍率 *= 1.15  
            # self.倍率 /= 0.8
        elif x == 1:
            self.攻击次数 = 0
            self.data1 = [ int(i*1.2) for i in self.data1]
            self.攻击次数2 = 24
            self.攻击次数3 = 46
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率+self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级) * self.倍率+self.data2[self.等级] * self.攻击次数3 * (1 + self.TP成长 * self.TP等级) * self.倍率
class 技能12(被动技能):
    名称 = '隐匿切割'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 技能13(主动技能):
    名称 = '血腥狂欢'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    #向前斩击物理攻击力：<data0>%
    data0 = [ int(i*1.0*1.121) for i in [0, 1810, 2230, 2649, 3069, 3489, 3909, 4328, 4748, 5168, 5588, 6008, 6427, 6847, 7267, 7687, 8106, 8526, 8946, 9366, 9785, 10205, 10626, 11046, 11466, 11885, 12305, 12725, 13145, 13564, 13984, 14404, 14824, 15243, 15663, 16083, 16503, 16923, 17342, 17762, 18182]]
    # 该次数存疑
    攻击次数 = 24
    #最后一击攻击力：<data1>%
    data1 = [ int(i*1.0*1.121) for i in [0, 5369, 6615, 7860, 9105, 10351, 11595, 12841, 14086, 15332, 16577, 17821, 19067, 20312, 21558, 22803, 24048, 25293, 26538, 27784, 29029, 30275, 31520, 32764, 34010, 35255, 36501, 37746, 38990, 40236, 41481, 42727, 43972, 45218, 46462, 47707, 48953, 50198, 51444, 52688, 53933]]
    攻击次数2 = 1
    # 基础 = 38871.42
    # 成长 = 11779.22
    CD = 145
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率 + self.data1[self.等级] * self.攻击次数2 * self.倍率

class 技能14(主动技能):
    名称 = '鲜血劫击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    # 基础 = 5698.53
    # 成长 = 643.47
    # 基础2 = 6385.12
    # 成长2 = 720.88
    #上升物理攻击力：<data0>%
    data0 = [ int(i*1.0*1.194) for i in [0, 6342, 6986, 7629, 8273, 8916, 9559, 10203, 10846, 11490, 12133, 12777, 13420, 14064, 14707, 15351, 15994, 16637, 17281, 17924, 18568, 19211, 19855, 20498, 21142, 21785, 22429, 23072, 23715, 24359, 25002, 25646, 26289, 26933, 27576, 28220, 28863, 29507, 30150, 30794, 31437, 32080, 32724, 33367, 34011, 34654, 35298, 35941, 36585, 37228, 37872, 38515, 39158, 39802, 40445, 41089, 41732, 42376, 43019, 43663, 44306, 44950, 45593, 46236, 46880, 47523, 48167, 48810, 49454, 50097, 50741]]
    #[新月斩击]物理攻击力：<data1>%
    data1 = [ int(i*1.0*1.194) for i in [0, 7106, 7827, 8547, 9268, 9989, 10710, 11431, 12152, 12873, 13594, 14315, 15036, 15757, 16477, 17198, 17919, 18640, 19361, 20082, 20803, 21524, 22245, 22966, 23687, 24407, 25128, 25849, 26570, 27291, 28012, 28733, 29454, 30175, 30896, 31617, 32337, 33058, 33779, 34500, 35221, 35942, 36663, 37384, 38105, 38826, 39547, 40267, 40988, 41709, 42430, 43151, 43872, 44593, 45314, 46035, 46756, 47477, 48197, 48918, 49639, 50360, 51081, 51802, 52523, 53244, 53965, 54686, 55407, 56128, 56848]]
    攻击次数 = 1
    攻击次数2 = 1
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 += 1.47+0.25
            self.攻击次数2 = 0
            # self.倍率 *= 1.25
        elif x == 1:
            self.攻击次数 += 1.47+0.44
            self.攻击次数2 = 0
            # self.倍率 *= 1.44
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率+self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能15(主动技能):
    名称 = '压制射击'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 基础 = 1254.33
    # 成长 = 141.67
    # 基础2 = 2789.17
    # 成长2 = 314.83
    #前方乱射攻击力：<data0>%
    data0 = [ int(i*1.0*1.173) for i in [0, 1396, 1537, 1679, 1821, 1962, 2105, 2247, 2388, 2530, 2672, 2813, 2955, 3096, 3238, 3380, 3521, 3663, 3804, 3946, 4089, 4230, 4372, 4514, 4655, 4797, 4939, 5080, 5222, 5363, 5505, 5647, 5788, 5930, 6071, 6214, 6356, 6497, 6639, 6781, 6922]]
    #最后射击攻击力：<data1>%
    data1 = [ int(i*1.0*1.173) for i in [0, 3104, 3418, 3733, 4047, 4363, 4678, 4992, 5307, 5622, 5937, 6252, 6566, 6882, 7196, 7511, 7827, 8141, 8456, 8770, 9086, 9401, 9715, 10031, 10345, 10660, 10975, 11290, 11605, 11919, 12234, 12550, 12864, 13179, 13493, 13809, 14124, 14438, 14754, 15068, 15383]]
    攻击次数 = 20
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.185
            self.攻击次数2 *= 1.50
        elif x == 1:
            self.攻击次数 *= 1.185
            self.攻击次数2 *= 2.30
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率+self.data1[self.等级] * self.攻击次数2 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能16(被动技能):
    名称 = '枪刃改良'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 技能17(主动技能):
    名称 = '死亡锁链'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    # 基础 = 29878.17
    # 成长 = 5667.83
    #快速射击攻击力：<data0>%
    data0 = [ int(i*1.0*1.196) for i in [0, 4443, 5151, 5860, 6568, 7277, 7986, 8694, 9403, 10111, 10820, 11528, 12236, 12944, 13653, 14361, 15070, 15778, 16487, 17195, 17904, 18612, 19321, 20030, 20737, 21445, 22154, 22862, 23571, 24280, 24988, 25697, 26405, 27114, 27822, 28531, 29238, 29947, 30655, 31364, 32072]]
    攻击次数 = 5
    #最终射击攻击力：<data1>%
    data1 = [ int(i*1.0*1.196) for i in [0, 13331, 15457, 17582, 19707, 21832, 23958, 26083, 28208, 30333, 32459, 34585, 36709, 38835, 40960, 43086, 45210, 47336, 49462, 51587, 53712, 55837, 57963, 60089, 62213, 64339, 66464, 68590, 70714, 72840, 74965, 77091, 79215, 81341, 83467, 85592, 87717, 89842, 91968, 94094, 96218]]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1 + 0.375 * 0.94
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率 + self.data1[self.等级] * self.攻击次数2 * self.倍率


class 技能18(主动技能):
    名称 = '锁链切割'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 基础 = 36301.00
    # 成长 = 4099.00
    #第1击攻击力：<data0>%
    data0 = [ int(i*1.0*1.195) for i in [0, 12120, 13350, 14580, 15809, 17039, 18268, 19498, 20728, 21957, 23187, 24417, 25646, 26876, 28106, 29335, 30565, 31794, 33024, 34254, 35483, 36713, 37943, 39172, 40402, 41632, 42861, 44091, 45321, 46550, 47780, 49009, 50239, 51469, 52698, 53928, 55158, 56387, 57617, 58847, 60076]]
    攻击次数 = 1
    #第2击攻击力：<data1>%
    data1 = [ int(i*1.0*1.195) for i in [0, 12120, 13350, 14580, 15809, 17039, 18268, 19498, 20728, 21957, 23187, 24417, 25646, 26876, 28106, 29335, 30565, 31794, 33024, 34254, 35483, 36713, 37943, 39172, 40402, 41632, 42861, 44091, 45321, 46550, 47780, 49009, 50239, 51469, 52698, 53928, 55158, 56387, 57617, 58847, 60076]]
    攻击次数2 = 1
    #第3击攻击力：<data2>%
    data2 = [ int(i*1.0*1.195) for i in [0, 16160, 17800, 19440, 21079, 22719, 24358, 25998, 27637, 29277, 30916, 32556, 34195, 35835, 37474, 39114, 40753, 42393, 44032, 45672, 47311, 48951, 50590, 52230, 53869, 55509, 57148, 58788, 60428, 62067, 63707, 65346, 66986, 68625, 70265, 71904, 73544, 75183, 76823, 78462, 80102]]
    攻击次数3 = 1
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.34
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率 + self.data1[self.等级] * self.攻击次数2 * self.倍率+ self.data2[self.等级] * self.攻击次数3 * self.倍率

class 技能19(主动技能):
    名称 = '血舞祭'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    # 基础 = 82497.00
    # 成长 = 24905.00
    data0 = [ int(i*1.0*1.138) for i in [0, 107402, 132308, 157212, 182118, 207023, 231927, 256833, 281738, 306643, 331548, 356454, 381358, 406264, 431168, 456073, 480979, 505883, 530789, 555694, 580599, 605504, 630408, 655314, 680219, 705124, 730029, 754935, 779839, 804745, 829649, 854554, 879460, 904364, 929270, 954175, 979080, 1003985, 1028891, 1053795, 1078700]]
    CD = 180
    def 等效百分比(self, 武器类型):
        return self.data0[self.等级] * self.攻击次数 * self.倍率



class 技能20(被动技能):
    名称 = '锁链意志'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4
    关联技能 = ['所有']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能21(主动技能):
    名称 = '毁灭风暴'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    CD = 60.0
    基础=19924
    成长=2251
    攻击次数=3
    基础2=29893.8
    成长2=3375.2
    攻击次数2=1
    基础3=1991.8
    成长3=225.2
    攻击次数3=5

"""
部分1：
第1击斩击攻击力 
第2击斩击攻击力
第3击斩击攻击力
第4击斩击攻击力
第5击斩击攻击力
部分2：
终结射击攻击力
部分3：
枪刃与锁链碎片攻击力
"""
class 技能22(主动技能):
    名称 = '盛放·绯红花园'
    关联技能 = ['无']
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    CD = 290.0
    基础=274307
    成长=82840
    攻击次数=1

    def 加成倍率(self, 武器类型):
        return 0.0

    # def 等效百分比(self, 武器类型):
    #     return self.data0[self.等级] * self.攻击次数 * self.倍率 + self.data1[self.等级] * self.攻击次数2 * self.倍率+ self.data2[self.等级] * self.攻击次数3 * self.倍率


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

class 职业属性(角色属性):

    实际名称 = '重霄·漫游枪手·女'
    角色 = '神枪手(女)'
    职业 = '漫游枪手'

    武器选项 = ['左轮枪']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.25
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号= deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['致命回射']].基础 = self.技能栏[self.技能序号['致命射击']].等效百分比(self.武器类型)*1.25
        self.技能栏[self.技能序号['致命回射']].被动倍率 = self.技能栏[self.技能序号['致命射击']].被动倍率

class 重霄·漫游枪手·女(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)
