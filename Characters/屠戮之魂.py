from PublicReference.base import *

class 职业主动技能(主动技能):

    data0 = []
    data1 = []
    data2 = []

    def 等效百分比(self, 武器类型):
        等效倍率 = 0.0
        if len(self.data0) >= self.等级 and len(self.data0) > 0:
            等效倍率 += self.data0[self.等级] * self.攻击次数
        if len(self.data1) >= self.等级 and len(self.data1) > 0:
            等效倍率 += self.data1[self.等级] * self.攻击次数2
        if len(self.data2) >= self.等级 and len(self.data2) > 0:
            等效倍率 += self.data2[self.等级] * self.攻击次数3
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

    # def 等效CD(self, 武器类型):
    #     # 战戟1.1
    #     return round(self.CD  / self.恢复 * 1.05, 1)


class 技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['猎杀枪']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 技能1(被动技能):
    名称 = '光枪精通'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.05 + 0.02 * self.等级, 5)

class 技能2(被动技能):
    名称 = '狩猎本能'
    所在等级 = 20
    等级上限 = 20
    基础等级 = 10
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

class 技能3(被动技能):
    名称 = '枪魂感知'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)

class 技能4(被动技能):
    名称 = '狩猎之心'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)

class 技能5(职业主动技能):
    名称 = '猎杀枪'
    所在等级 = 15
    等级上限 = 5
    基础等级 = 1
    data0 = [0, 248, 274, 299, 324, 349, 374, 400, 425, 450, 475, 501, 526, 551, 576, 602, 627, 652, 677, 703, 728, 753, 778, 804, 829, 854, 879, 904, 930, 955, 980, 1005, 1031, 1056, 1081, 1106, 1132, 1157, 1182, 1207, 1233, 1258, 1283, 1308, 1333, 1359, 1384, 1409, 1434, 1460, 1485, 1510, 1535, 1561, 1586, 1611, 1636, 1662, 1687, 1712, 1737, 1763, 1788, 1813, 1838, 1863, 1889, 1914, 1939, 1964, 1990]
    攻击次数 = 1
    # 基础 = 222.0
    # 成长 = 26.0
    # 固定CD0.85 具体待确认
    CD = 0.85
    TP成长 = 0.10
    TP上限 = 3
    基础释放次数 = 5
    def 等效CD(self, 武器类型,输出类型):
        return 0.85

class 技能6(职业主动技能):
    名称 = '隐鼠袭杀'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    data0 = [0, 2066, 2275, 2485, 2694, 2904, 3114, 3323, 3533, 3742, 3952, 4162, 4371, 4581, 4791, 5000, 5210, 5419, 5629, 5839, 6048, 6258, 6467, 6677, 6887, 7096, 7306, 7515, 7725, 7935, 8144, 8354, 8563, 8773, 8983, 9192, 9402, 9612, 9821, 10031, 10240, 10450, 10660, 10869, 11079, 11288, 11498, 11708, 11917, 12127, 12336, 12546, 12756, 12965, 13175, 13384, 13594, 13804, 14013, 14223, 14433, 14642, 14852, 15061, 15271, 15481, 15690, 15900, 16109, 16319, 16529]
    攻击次数 = 1
    # 基础 = 1856.40
    # 成长 = 209.60
    CD = 5.0
    TP成长 = 0.10
    TP上限 = 5

class 技能7(职业主动技能):
    名称 = '光焰飞枪'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    data0 = [0, 514, 566, 618, 671, 723, 775, 827, 879, 931, 984, 1036, 1088, 1140, 1192, 1245, 1297, 1349, 1401, 1453, 1506, 1558, 1610, 1662, 1714, 1767, 1819, 1871, 1923, 1975, 2027, 2080, 2132, 2184, 2236, 2288, 2341, 2393, 2445, 2497, 2549, 2602, 2654, 2706, 2758, 2810, 2863, 2915, 2967, 3019, 3071, 3123, 3176, 3228, 3280, 3332, 3384, 3437, 3489, 3541, 3593]
    攻击次数 = 5
    # 基础 = 2309.05
    # 成长 = 260.95
    CD = 6.0
    TP成长 = 0.10
    TP上限 = 5

class 技能8(职业主动技能):
    名称 = '蛮横冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [0, 1205, 1328, 1450, 1572, 1695, 1817, 1939, 2062, 2184, 2306, 2429, 2551, 2673, 2796, 2918, 3040, 3163, 3285, 3407, 3530, 3652, 3774, 3897, 4019, 4141, 4264, 4386, 4508, 4631, 4753, 4875, 4997, 5120, 5242, 5364, 5487, 5609, 5731, 5854, 5976, 6098, 6221, 6343, 6465, 6588, 6710, 6832, 6955, 7077, 7199, 7322, 7444, 7566, 7689, 7811, 7933, 8056, 8178, 8300, 8423, 8545, 8667, 8790, 8912, 9034, 9157, 9279, 9401, 9524, 9646]
    攻击次数 = 1
    #下刺攻击力：<data1>%
    data1 = [0, 1467, 1616, 1765, 1913, 2062, 2211, 2360, 2509, 2658, 2807, 2956, 3104, 3253, 3402, 3551, 3700, 3849, 3998, 4146, 4295, 4444, 4593, 4742, 4891, 5040, 5188, 5337, 5486, 5635, 5784, 5933, 6082, 6231, 6379, 6528, 6677, 6826, 6975, 7124, 7273, 7421, 7570, 7719, 7868, 8017, 8166, 8315, 8463, 8612, 8761, 8910, 9059, 9208, 9357, 9506, 9654, 9803, 9952, 10101, 10250, 10399, 10548, 10696, 10845, 10994, 11143, 11292, 11441, 11590, 11739]
    攻击次数2 = 1
    #生成的魔法枪攻击力：<data2>%
    data2 = [0, 489, 538, 588, 637, 687, 737, 786, 836, 886, 935, 985, 1034, 1084, 1134, 1183, 1233, 1283, 1332, 1382, 1431, 1481, 1531, 1580, 1630, 1680, 1729, 1779, 1828, 1878, 1928, 1977, 2027, 2077, 2126, 2176, 2225, 2275, 2325, 2374, 2424, 2473, 2523, 2573, 2622, 2672, 2722, 2771, 2821, 2870, 2920, 2970, 3019, 3069, 3119, 3168, 3218, 3267, 3317, 3367, 3416, 3466, 3516, 3565, 3615, 3664, 3714, 3764, 3813, 3863, 3913]
    攻击次数3 = 3
    # 基础 = 3719.00
    # 成长 = 420.00
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5

class 技能9(职业主动技能):
    名称 = '猎杀枪掠食'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    #地面发射攻击力：<data0>%
    data0 = [0, 3635, 4003, 4372, 4741, 5110, 5478, 5847, 6216, 6585, 6953, 7322, 7691, 8060, 8429, 8797, 9166, 9535, 9904, 10272, 10641, 11010, 11379, 11747, 12116, 12485, 12854, 13223, 13591, 13960, 14329, 14698, 15066, 15435, 15804, 16173, 16541, 16910, 17279, 17648, 18017, 18385, 18754, 19123, 19492, 19860, 20229, 20598, 20967, 21335, 21704, 22073, 22442, 22811, 23179, 23548, 23917, 24286, 24654, 25023, 25392, 25761, 26129, 26498, 26867, 27236, 27605, 27973, 28342, 28711, 29080]
    #空中发射攻击力：<data1>%
    # data1 = [0, 3554, 3914, 4275, 4636, 4996, 5357, 5717, 6078, 6439, 6799, 7160, 7520, 7881, 8242, 8602, 8963, 9323, 9684, 10045, 10405, 10766, 11126, 11487, 11847, 12208, 12569, 12929, 13290, 13650, 14011, 14372, 14732, 15093, 15453, 15814, 16175, 16535, 16896, 17256, 17617, 17978, 18338, 18699, 19059, 19420, 19780, 20141, 20502, 20862, 21223, 21583, 21944, 22305, 22665, 23026, 23386, 23747, 24108, 24468, 24829, 25189, 25550, 25910, 26271, 26632, 26992, 27353, 27713, 28074, 28435]
    # 基础 = 3266.26
    # 成长 = 368.74
    CD = 9.0
    TP成长 = 0.10
    TP上限 = 5

class 技能10(职业主动技能):
    名称 = '光焰枪'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [0, 5253, 5786, 6319, 6852, 7385, 7918, 8451, 8984, 9517, 10050, 10583, 11116, 11649, 12182, 12715, 13248, 13781, 14314, 14846, 15379, 15912, 16445, 16978, 17511, 18044, 18577, 19110, 19643, 20176, 20709, 21242, 21775, 22308, 22841, 23374, 23907, 24440, 24973, 25506, 26039, 26572, 27105, 27638, 28171, 28704, 29237, 29770, 30303, 30836, 31369, 31901, 32434, 32967, 33500, 34033, 34566, 35099, 35632, 36165, 36698, 37231, 37764, 38297, 38830, 39363, 39896, 40429, 40962, 41495, 42028]
    # 基础 = 4720.03
    # 成长 = 532.97
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5

class 技能11(职业主动技能):
    名称 = '猎杀枪穿心'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    #旋转时攻击力：<data0>%
    data0 = [0, 404, 445, 486, 527, 568, 609, 650, 691, 732, 773, 814, 855, 896, 937, 978, 1019, 1060, 1101, 1142, 1183, 1224, 1265, 1306, 1347, 1388, 1429, 1470, 1511, 1552, 1593, 1634, 1675, 1716, 1757, 1798, 1839, 1880, 1921, 1962, 2003, 2044, 2085, 2126, 2167, 2208, 2249, 2290, 2331, 2372, 2413, 2454, 2495, 2536, 2577, 2618, 2659, 2700, 2741, 2782, 2823, 2864, 2905, 2946, 2987, 3028, 3069, 3110, 3151, 3192, 3233]
    攻击次数 = 6
    #返回时攻击力：<data1>%
    data1 = [0, 1616, 1780, 1944, 2108, 2272, 2436, 2600, 2764, 2928, 3092, 3256, 3420, 3584, 3748, 3912, 4076, 4240, 4405, 4569, 4733, 4897, 5061, 5225, 5389, 5553, 5717, 5881, 6045, 6209, 6373, 6537, 6701, 6865, 7029, 7193, 7357, 7521, 7685, 7849, 8013, 8177, 8341, 8505, 8669, 8833, 8997, 9161, 9325, 9489, 9653, 9817, 9981, 10145, 10309, 10473, 10637, 10801, 10965, 11129, 11293, 11457, 11621, 11785, 11949, 12113, 12277, 12441, 12605, 12769, 12933]
    攻击次数2 = 1
    # 基础 = 3629.97
    # 成长 = 410.03
    CD = 10.0
    TP成长 = 0.10
    TP上限 = 5

class 技能12(职业主动技能):
    名称 = '光焰囚杀'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    # 基础 = 7051.80
    # 成长 = 796.20
    #屏障多段攻击力：<data0>%
    data0 = [0, 3924, 4322, 4720, 5118, 5516, 5914, 6312, 6710, 7108, 7506, 7905, 8303, 8701, 9099, 9497, 9895, 10293, 10691, 11089, 11487, 11886, 12284, 12682, 13080, 13478, 13876, 14274, 14672, 15070, 15468, 15867, 16265, 16663, 17061, 17459, 17857, 18255, 18653, 19051, 19449, 19848, 20246, 20644, 21042, 21440, 21838, 22236, 22634, 23032, 23430, 23829, 24227, 24625, 25023, 25421, 25819, 26217, 26615, 27013, 27411, 27809, 28208, 28606, 29004, 29402, 29800, 30198, 30596, 30994, 31392]
    攻击次数 = 1
    #屏障爆炸攻击力：<data1>%
    data1 = [0, 3924, 4322, 4720, 5118, 5516, 5914, 6312, 6710, 7108, 7506, 7905, 8303, 8701, 9099, 9497, 9895, 10293, 10691, 11089, 11487, 11886, 12284, 12682, 13080, 13478, 13876, 14274, 14672, 15070, 15468, 15867, 16265, 16663, 17061, 17459, 17857, 18255, 18653, 19051, 19449, 19848, 20246, 20644, 21042, 21440, 21838, 22236, 22634, 23032, 23430, 23829, 24227, 24625, 25023, 25421, 25819, 26217, 26615, 27013, 27411, 27809, 28208, 28606, 29004, 29402, 29800, 30198, 30596, 30994, 31392]
    攻击次数2 = 1
    CD = 20.0
    TP成长 = 0.10
    TP上限 = 5

class 技能13(职业主动技能):
    名称 = '利刃收割'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    #挥击攻击力：<data0>%
    data0 = [0, 889, 979, 1069, 1159, 1250, 1340, 1430, 1520, 1611, 1701, 1791, 1881, 1971, 2062, 2152, 2242, 2332, 2422, 2513, 2603, 2693, 2783, 2874, 2964, 3054, 3144, 3234, 3325, 3415, 3505, 3595, 3685, 3776, 3866, 3956, 4046, 4137, 4227, 4317, 4407, 4497, 4588, 4678, 4768, 4858, 4949, 5039, 5129, 5219, 5309, 5400, 5490, 5580, 5670, 5760, 5851, 5941, 6031, 6121, 6212, 6302, 6392, 6482, 6572, 6663, 6753, 6843, 6933, 7023, 7114]
    攻击次数 = 4
    #击退攻击力：<data1>%
    data1 = [0, 3557, 3917, 4278, 4639, 5000, 5361, 5722, 6083, 6444, 6804, 7165, 7526, 7887, 8248, 8609, 8970, 9330, 9691, 10052, 10413, 10774, 11135, 11496, 11856, 12217, 12578, 12939, 13300, 13661, 14022, 14383, 14743, 15104, 15465, 15826, 16187, 16548, 16909, 17269, 17630, 17991, 18352, 18713, 19074, 19435, 19796, 20156, 20517, 20878, 21239, 21600, 21961, 22322, 22682, 23043, 23404, 23765, 24126, 24487, 24848, 25208, 25569, 25930, 26291, 26652, 27013, 27374, 27735, 28095, 28456]
    攻击次数2 = 1
    #上升攻击力：<data2>%
    # data2 = [0, 3560, 3922, 4283, 4644, 5005, 5366, 5728, 6089, 6450, 6811, 7173, 7534, 7895, 8256, 8618, 8979, 9340, 9701, 10063, 10424, 10785, 11146, 11508, 11869, 12230, 12591, 12952, 13314, 13675, 14036, 14397, 14759, 15120, 15481, 15842, 16204, 16565, 16926, 17287, 17649, 18010, 18371, 18732, 19094, 19455, 19816, 20177, 20538, 20900, 21261, 21622, 21983, 22345, 22706, 23067, 23428, 23790, 24151, 24512, 24873, 25235, 25596, 25957, 26318, 26680, 27041, 27402, 27763, 28124, 28486]
    # 基础 = 6394.43
    # 成长 = 721.57
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            # self.倍率 *= 1.1
            self.data1 = [(0.05*1.2*i) for i in self.data1]
            self.攻击次数2 = 20
            self.CD *= 0.9
        elif x == 1:
            # self.倍率 *= 1.19
            self.data0 = [(1.18*i) for i in self.data0]
            self.data1 = [(0.05*1.2*i) for i in self.data1]
            self.攻击次数2 = 20
            self.CD *= 0.9

class 技能14(职业主动技能):
    名称 = '鹰坠'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    # 基础 = 10325.19
    # 成长 = 1165.81
    data0 = [0, 11491, 12657, 13822, 14988, 16154, 17320, 18486, 19651, 20817, 21984, 23149, 24315, 25480, 26647, 27813, 28978, 30144, 31309, 32476, 33642, 34807, 35973, 37139, 38305, 39471, 40636, 41803, 42968, 44134, 45300, 46465, 47632, 48798, 49963, 51129, 52295, 53461, 54627, 55792, 56958, 58124, 59290, 60456, 61621, 62788, 63953, 65119, 66285, 67450, 68617, 69782, 70948, 72114, 73280, 74446, 75611, 76777, 77943, 79109, 80275, 81441, 82606, 83773, 84938, 86104, 87270, 88435, 89602, 90767, 91933]
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
  
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.1
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.19
            self.CD *= 0.9

class 技能15(职业主动技能):
    名称 = '龙鳞碎割'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    # 基础 = 16415.52
    # 成长 = 1855.48
    #魔法枪攻击力：<data0>%
    data0 = [0, 365, 402, 439, 477, 514, 551, 588, 625, 662, 699, 736, 773, 810, 848, 885, 922, 959, 996, 1033, 1070, 1107, 1144, 1181, 1219, 1256, 1293, 1330, 1367, 1404, 1441, 1478, 1515, 1553, 1590, 1627, 1664, 1701, 1738, 1775, 1812, 1849, 1886, 1924, 1961, 1998, 2035, 2072, 2109, 2146, 2183, 2220, 2257, 2295, 2332, 2369, 2406, 2443, 2480, 2517, 2554, 2591, 2628, 2666, 2703, 2740, 2777, 2814, 2851, 2888, 2925]
    攻击次数 = 20
    #终结攻击力：<data1>%
    data1 = [0, 10971, 12084, 13197, 14310, 15424, 16537, 17650, 18763, 19876, 20989, 22102, 23215, 24328, 25441, 26554, 27667, 28780, 29894, 31007, 32120, 33233, 34346, 35459, 36572, 37685, 38798, 39911, 41024, 42137, 43250, 44364, 45477, 46590, 47703, 48816, 49929, 51042, 52155, 53268, 54381, 55494, 56607, 57720, 58834, 59947, 61060, 62173, 63286, 64399, 65512, 66625, 67738, 68851, 69964, 71077, 72190, 73304, 74417, 75530, 76643, 77756, 78869, 79982, 81095, 82208, 83321, 84434, 85547, 86660, 87774]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            # self.倍率 *= 1.23
            self.攻击次数 +=25
            self.data0 = [(i*0.7) for i in self.data0]
            self.CD *= 0.9
        elif x == 1:
            # self.倍率 *= 1.23 + 0.08
            self.攻击次数 +=25
            self.data0 = [(i*0.7) for i in self.data0]
            self.data1 = [(i*1.13) for i in self.data1]
            self.CD *= 0.9

class 技能16(职业主动技能):
    名称 = '逐云灭龙杀'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    # 基础 = 37586.91
    # 成长 = 11389.97
    #直接攻击力：<data0>%
    data0 = [0, 2453, 3022, 3591, 4160, 4729, 5298, 5867, 6436, 7005, 7574, 8143, 8712, 9281, 9850, 10419, 10988, 11557, 12126, 12695, 13264, 13833, 14402, 14971, 15540, 16109, 16678, 17247, 17816, 18385, 18954, 19523, 20092, 20661, 21230, 21799, 22368, 22937, 23505, 24074, 24643, 25212, 25781, 26350, 26919, 27488, 28057, 28626, 29195, 29764, 30333, 30902, 31471, 32040, 32609, 33178, 33747, 34316, 34885, 35454, 36023, 36592, 37161, 37730, 38299, 38868, 39437, 40006, 40575, 41144, 41713]
    攻击次数 = 1
    #猎杀枪多段攻击力：<data1>%
    data1 = [0, 1717, 2115, 2514, 2912, 3310, 3709, 4107, 4505, 4903, 5302, 5700, 6098, 6497, 6895, 7293, 7691, 8090, 8488, 8886, 9285, 9683, 10081, 10479, 10878, 11276, 11674, 12073, 12471, 12869, 13267, 13666, 14064, 14462, 14861, 15259, 15657, 16055, 16454, 16852, 17250, 17649, 18047, 18445, 18843, 19242, 19640, 20038, 20437, 20835, 21233, 21631, 22030, 22428, 22826, 23225, 23623, 24021, 24419, 24818, 25216, 25614, 26013, 26411, 26809, 27207, 27606, 28004, 28402, 28801, 29199]
    攻击次数2 = 10
    #降落冲撞爆炸攻击力：<data2>%
    data2 = [0, 29444, 36272, 43100, 49927, 56755, 63583, 70411, 77239, 84066, 90894, 97722, 104550, 111377, 118205, 125033, 131861, 138688, 145516, 152344, 159172, 165999, 172827, 179655, 186483, 193310, 200138, 206966, 213794, 220621, 227449, 234277, 241105, 247932, 254760, 261588, 268416, 275244, 282071, 288899, 295727, 302555, 309382, 316210, 323038, 329866, 336693, 343521, 350349, 357177, 364004, 370832, 377660, 384488, 391315, 398143, 404971, 411799, 418626, 425454, 432282, 439110, 445937, 452765, 459593, 466421, 473249, 480076, 486904, 493732, 500560]
    攻击次数3 = 1

    CD = 145.0

class 技能17(职业主动技能):
    名称 = '天龙破'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    # 基础 = 13676.65
    # 成长 = 1544.35
    #魔法枪乱舞攻击力：<data0>%
    data0 = [0, 2283, 2515, 2746, 2978, 3210, 3441, 3673, 3905, 4136, 4368, 4600, 4831, 5063, 5295, 5526, 5758, 5990, 6221, 6453, 6685, 6916, 7148, 7380, 7611, 7843, 8075, 8306, 8538, 8770, 9001, 9233, 9465, 9697, 9928, 10160, 10392, 10623, 10855, 11087, 11318, 11550, 11782, 12013, 12245, 12477, 12708, 12940, 13172, 13403, 13635, 13867, 14098, 14330, 14562, 14793, 15025, 15257, 15488, 15720, 15952, 16183, 16415, 16647, 16878, 17110, 17342, 17573, 17805, 18037, 18268]
    攻击次数 = 4
    #地面爆炸攻击力：<data1>%
    data1 = [0, 6089, 6707, 7325, 7942, 8560, 9178, 9796, 10414, 11031, 11649, 12267, 12885, 13502, 14120, 14738, 15356, 15974, 16591, 17209, 17827, 18445, 19063, 19680, 20298, 20916, 21534, 22151, 22769, 23387, 24005, 24623, 25240, 25858, 26476, 27094, 27712, 28329, 28947, 29565, 30183, 30800, 31418, 32036, 32654, 33272, 33889, 34507, 35125, 35743, 36360, 36978, 37596, 38214, 38832, 39449, 40067, 40685, 41303, 41921, 42538, 43156, 43774, 44392, 45009, 45627, 46245, 46863, 47481, 48098, 48716]
    攻击次数2 = 1
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            # 地面形态
            self.攻击次数 = 2
            self.data0 = [(i*2.52) for i in self.data0]
            self.data1 = [(i*1.26) for i in self.data1]
            # 空中形态
            # self.攻击次数 = 0
            # self.data1 = [(i*2.25*1.26) for i in self.data1]
            # self.倍率 *= 1.26
        elif x == 1:
            # self.倍率 *= 1.348
            # 地面形态
            self.攻击次数 = 2
            self.data0 = [(i*2.52) for i in self.data0]
            self.data1 = [(i*1.48) for i in self.data1]

class 技能18(职业主动技能):
    名称 = '地龙狩'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    # 基础 = 20315.33
    # 成长 = 2293.67
    #爆炸攻击力：<data0>%
    data0 = [0, 22609, 24902, 27196, 29490, 31783, 34077, 36371, 38664, 40958, 43252, 45545, 47839, 50133, 52426, 54720, 57014, 59307, 61601, 63895, 66188, 68482, 70776, 73070, 75363, 77657, 79951, 82244, 84538, 86832, 89125, 91419, 93713, 96006, 98300, 100594, 102887, 105181, 107475, 109768, 112062, 114356, 116649, 118943, 121237, 123530, 125824, 128118, 130411, 132705, 134999, 137292, 139586, 141880, 144174, 146467, 148761, 151055, 153348, 155642, 157936, 160229, 162523, 164817, 167110, 169404, 171698, 173991, 176285, 178579, 180872]
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.17
        elif x == 1:
            self.倍率 *= 1.25
            

class 技能19(职业主动技能):
    名称 = '地龙封魔杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    # 基础 = 32961.50
    # 成长 = 3721.50
    #地面射出的魔法枪攻击力：<data0>%
    data0 = [0, 11005, 12121, 13237, 14354, 15470, 16587, 17703, 18820, 19936, 21053, 22169, 23286, 24402, 25518, 26635, 27751, 28868, 29984, 31101, 32217, 33334, 34450, 35567, 36683, 37799, 38916, 40032, 41149, 42265, 43382, 44498, 45615, 46731, 47848, 48964, 50080, 51197, 52313, 53430, 54546, 55663, 56779, 57896, 59012, 60129, 61245, 62361, 63478, 64594, 65711, 66827, 67944, 69060, 70177, 71293, 72410, 73526, 74642, 75759, 76875, 77992, 79108, 80225, 81341, 82458, 83574, 84691, 85807, 86923, 88040]
    #爆炸攻击力：<data1>%
    data1 = [0, 25678, 28283, 30888, 33493, 36098, 38703, 41308, 43913, 46518, 49123, 51729, 54334, 56939, 59544, 62149, 64754, 67359, 69964, 72569, 75174, 77779, 80384, 82989, 85594, 88199, 90804, 93409, 96015, 98620, 101225, 103830, 106435, 109040, 111645, 114250, 116855, 119460, 122065, 124670, 127275, 129880, 132485, 135090, 137695, 140301, 142906, 145511, 148116, 150721, 153326, 155931, 158536, 161141, 163746, 166351, 168956, 171561, 174166, 176771, 179376, 181981, 184587, 187192, 189797, 192402, 195007, 197612, 200217, 202822, 205427]
    攻击次数2 = 1
    CD = 40.0
    是否有护石 = 1

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33

class 技能20(职业主动技能):
    名称 = '无尽杀戮'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    #原地多段攻击攻击力：<data0>%
    data0 = [0, 1319, 1453, 1586, 1720, 1854, 1988, 2122, 2256, 2389, 2523, 2657, 2791, 2925, 3059, 3192, 3326, 3460, 3594, 3728, 3862, 3995, 4129, 4263, 4397, 4531, 4665, 4799, 4932, 5066, 5200, 5334, 5468, 5602, 5735, 5869, 6003, 6137, 6271, 6405, 6538, 6672, 6806, 6940, 7074, 7208, 7341, 7475, 7609, 7743, 7877, 8011, 8144, 8278, 8412, 8546, 8680, 8814, 8947, 9081, 9215, 9349, 9483, 9617, 9750, 9884, 10018, 10152, 10286, 10420, 10554]
    攻击次数 = 7
    #前进时多段攻击攻击力：<data1>%
    data1 = [0, 2339, 2576, 2814, 3051, 3288, 3526, 3763, 4000, 4238, 4475, 4712, 4950, 5187, 5424, 5662, 5899, 6136, 6373, 6611, 6848, 7085, 7323, 7560, 7797, 8035, 8272, 8509, 8747, 8984, 9221, 9459, 9696, 9933, 10171, 10408, 10645, 10883, 11120, 11357, 11595, 11832, 12069, 12307, 12544, 12781, 13019, 13256, 13493, 13731, 13968, 14205, 14443, 14680, 14917, 15155, 15392, 15629, 15867, 16104, 16341, 16579, 16816, 17053, 17291, 17528, 17765, 18003, 18240, 18477, 18715]
    攻击次数2 = 4
    #爆炸攻击力：<data2>%
    data2 = [0, 27934, 30768, 33602, 36436, 39270, 42103, 44937, 47771, 50605, 53439, 56273, 59107, 61941, 64775, 67609, 70443, 73277, 76111, 78944, 81778, 84612, 87446, 90280, 93114, 95948, 98782, 101616, 104450, 107284, 110118, 112951, 115785, 118619, 121453, 124287, 127121, 129955, 132789, 135623, 138457, 141291, 144125, 146959, 149792, 152626, 155460, 158294, 161128, 163962, 166796, 169630, 172464, 175298, 178132, 180966, 183800, 186633, 189467, 192301, 195135, 197969, 200803, 203637, 206471, 209305, 212139, 214973, 217807, 220640, 223474]
    攻击次数3 = 1
    # 风车这个技能没护石的状态下 段数跟站位还有怪能不能推有小关系 旋转7-8 前进可以3-4 但打桩一般是741
    # 基础 = 42988.14
    # 成长 = 4853.86
    CD = 45.0
    是否有护石 = 1

    护石选项 = ['圣痕']#CPhit：16+2
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 16
            # self.倍率 *= 1.3680134248
            self.攻击次数2 = 0
            self.data0 = [(i*1.02*1.18) for i in self.data0]
            self.攻击次数3 = 2
            self.data2 = [(i*0.58*1.18) for i in self.data2]

class 技能21(职业主动技能):
    名称 = '绝命猎杀死亡穿刺'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0=[0, 62267, 76706, 91144, 105583, 120022, 134461, 148899, 163338, 177777, 192216, 206655, 221093, 235532, 249971, 264410, 278849, 293287, 307726, 322165, 336604, 351042, 365481, 379920, 394359, 408798, 423236, 437675, 452114, 466553, 480992, 495430, 509869, 524308, 538747, 553185, 567624, 582063, 596502, 610941, 625379, 639818, 654257, 668696, 683134, 697573, 712012, 726451, 740890, 755328, 769767, 784206, 798645, 813084, 827522, 841961, 856400, 870839, 885277, 899716, 914155, 928594, 943033, 957471, 971910, 986349, 1000788, 1015227, 1029665, 1044104, 1058543]
    data1=[0, 52928, 65202, 77475, 89749, 102022, 114296, 126568, 138842, 151115, 163389, 175663, 187936, 200209, 212482, 224756, 237029, 249303, 261576, 273850, 286122, 298396, 310669, 322943, 335217, 347490, 359763, 372036, 384310, 396583, 408857, 421130, 433403, 445676, 457950, 470223, 482497, 494771, 507044, 519317, 531590, 543864, 556137, 568411, 580684, 592957, 605230, 617504, 629778, 642051, 654325, 666598, 678871, 691144, 703418, 715691, 727965, 740238, 752511, 764784, 777058, 789332, 801605, 813879, 826152, 838425, 850698, 862972, 875245, 887519, 899792]
    攻击次数2=1
    CD = 180

class 技能22(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能23(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 技能24(被动技能):
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

    实际名称 = '屠戮之魂'
    角色 = '魔枪士'
    职业 = '狩猎者'

    武器选项 = ['光枪']
    
    类型选择 = ['魔法百分比']
    
    类型 = '魔法百分比'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 1.85
   
    远古记忆 = 0
  
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(技能列表)
        self.技能序号= deepcopy(技能序号)

class 屠戮之魂(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)
