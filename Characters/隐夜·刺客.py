from PublicReference.base import *

# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '匕首':
#             return round(self.CD / self.恢复  * 0.9, 1)
#         if 武器类型 == '双剑':
#             return round(self.CD / self.恢复  * 1.1, 1)

class 技能0(主动技能):
    名称 = '终结追击'
    所在等级 = 15
    等级上限 = 30
    基础等级 = 20
    是否有伤害 = 0
    def 终结追击倍率(self):
        if self.等级 == 0:
            return 0.0
        else:
            return round(0.79 + 0.02 * self.等级, 5)

class 技能1(被动技能):
    名称 = '匕首精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    data1 = [0, 36, 53, 70, 87, 104, 121, 138, 155, 172, 189, 206, 223, 240, 257, 274, 291, 308, 325, 342, 359, 387, 415, 443, 471, 499, 527, 555, 583, 611, 639, 667, 695, 723, 751, 779, 807, 835, 863, 891, 919, 947, 975, 1003, 1031, 1059, 1087, 1115, 1143, 1171, 1199, 1227, 1255, 1283, 1311, 1339, 1367, 1395, 1423, 1451, 1479, 1507, 1535, 1563, 1591, 1619, 1647, 1675, 1703, 1731, 1759]
    data2 = [0, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67, 70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100, 103, 106, 109, 112, 115, 118, 121, 124, 127, 130, 133, 136, 139, 142, 145, 148, 151, 154, 157, 160, 163, 166, 169, 172, 175, 178, 181, 184, 187, 190, 193, 196, 199, 202, 205, 208, 211, 214, 217]
    def 加成倍率(self, 武器类型):
        if 武器类型 != '匕首':
            return 1.0
        else:
            return round(1 + self.data1[self.等级] / 1000, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    冷却关联技能 = ['所有']
    def CD缩减倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '匕首':
            return 1.0
        else:
            return round(1 - self.data2[self.等级] / 1000, 5)

class 技能2(被动技能):
    名称 = '双剑精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20
    data1 = [0, 36, 53, 70, 87, 104, 121, 138, 155, 172, 189, 206, 223, 240, 257, 274, 291, 308, 325, 342, 359, 387, 415, 443, 471, 499, 527, 555, 583, 611, 639, 667, 695, 723, 751, 779, 807, 835, 863, 891, 919, 947, 975, 1003, 1031, 1059, 1087, 1115, 1143, 1171, 1199, 1227, 1255, 1283, 1311, 1339, 1367, 1395, 1423, 1451, 1479, 1507, 1535, 1563, 1591, 1619, 1647, 1675, 1703, 1731, 1759]
    data2 = [0, 22, 23, 25, 26, 27, 28, 29, 31, 32, 33, 34, 36, 37, 38, 39, 40, 42, 43, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 59, 60, 61, 62, 63, 65, 66, 67, 68, 69, 71, 72, 73, 74, 75, 77, 78, 79, 80, 82, 83, 84, 85, 86, 88, 89, 90, 91, 92, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 106]

    def 加成倍率(self, 武器类型):
        if self.等级 == 0 or 武器类型 != '双剑':
            return 1.0
        else:
            return round(1 + self.data1[self.等级] / 1000, 5)

    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

    def 终结追击倍率(self):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + self.data2[self.等级] / 100, 5)

class 技能3(被动技能):
    名称 = '月弧'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.095 + 0.02 * self.等级, 5)

class 技能4(被动技能):
    名称 = '极限追击'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)
            
    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

class 技能5(主动技能):
    名称 = '双刃穿刺'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据=[0, 461, 507, 554, 601, 648, 694, 741, 788, 835, 881, 928, 975, 1022, 1068, 1115, 1162, 1209, 1255, 1302, 1349, 1395, 1442, 1489, 1537, 1582, 1629, 1677, 1724, 1769, 1817, 1864, 1911, 1957, 2004, 2051, 2098, 2144, 2191, 2238, 2285, 2331, 2378, 2425, 2472, 2518, 2565, 2612, 2659, 2705, 2752, 2799, 2845, 2892, 2939, 2986, 3032, 3079, 3126, 3174, 3219, 3267, 3314, 3361, 3407, 3454, 3501, 3548, 3594, 3641, 3688]
    数据1=[0, 691, 761, 831, 901, 971, 1041, 1111, 1183, 1253, 1323, 1393, 1463, 1533, 1603, 1673, 1743, 1814, 1884, 1954, 2024, 2094, 2164, 2234, 2304, 2374, 2445, 2515, 2585, 2655, 2725, 2796, 2866, 2936, 3006, 3077, 3147, 3217, 3287, 3357, 3427, 3497, 3567, 3637, 3708, 3778, 3848, 3918, 3988, 4058, 4128, 4198, 4268, 4340, 4410, 4480, 4550, 4620, 4690, 4760, 4830, 4900, 4971, 5041, 5111, 5181, 5251, 5321, 5391, 5461, 5531]
    数据2=[0, 922, 1015, 1109, 1202, 1296, 1389, 1483, 1576, 1670, 1763, 1857, 1950, 2044, 2137, 2232, 2324, 2419, 2512, 2606, 2699, 2793, 2886, 2980, 3073, 3167, 3260, 3354, 3447, 3541, 3634, 3729, 3822, 3916, 4009, 4103, 4196, 4290, 4383, 4477, 4570, 4664, 4757, 4851, 4944, 5039, 5131, 5226, 5319, 5413, 5506, 5600, 5693, 5787, 5880, 5974, 6067, 6161, 6254, 6348, 6441, 6536, 6629, 6723, 6816, 6910, 7003, 7097, 7190, 7284, 7377]
    数据3=[0, 414, 457, 499, 541, 583, 625, 667, 709, 751, 793, 835, 877, 919, 961, 1003, 1046, 1088, 1130, 1172, 1214, 1256, 1298, 1340, 1382, 1424, 1466, 1509, 1551, 1593, 1636, 1678, 1720, 1762, 1804, 1846, 1888, 1930, 1972, 2014, 2056, 2098, 2140, 2182, 2225, 2267, 2309, 2351, 2393, 2435, 2477, 2519, 2561, 2603, 2645, 2687, 2729, 2771, 2815, 2857, 2899, 2941, 2983, 3025, 3067, 3109, 3151, 3193, 3235, 3277, 3319]
    攻击次数2 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级]+self.数据1[self.等级]+self.数据2[self.等级]) * self.攻击次数 + self.数据3[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.162

class 技能6(主动技能):
    名称 = '绝杀斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据=[0, 1918, 2112, 2307, 2502, 2697, 2892, 3086, 3280, 3475, 3670, 3865, 4059, 4254, 4449, 4643, 4838, 5033, 5227, 5422, 5617, 5811, 6006, 6200, 6395, 6590, 6785, 6979, 7174, 7368, 7563, 7758, 7953, 8148, 8341, 8536, 8731, 8926, 9121, 9316, 9509, 9704, 9899, 10094, 10289, 10482, 10677, 10872, 11067, 11262, 11457, 11650, 11845, 12040, 12235, 12430, 12624, 12818, 13013, 13208, 13403, 13598, 13792, 13986, 14181, 14376, 14571, 14765, 14960, 15154, 15349]
    数据1=[0, 58, 63, 68, 75, 80, 86, 92, 98, 103, 110, 115, 122, 127, 133, 139, 144, 150, 156, 162, 167, 174, 179, 186, 191, 198, 203, 209, 215, 221, 226, 232, 238, 243, 250, 255, 262, 267, 273, 279, 285, 290, 297, 302, 307, 314, 319, 326, 331, 337, 343, 349, 354, 361, 366, 373, 378, 385, 390, 395, 402, 407, 413, 419, 425, 430, 437, 442, 449, 454, 460]
    数据2=[0, 109, 119, 129, 141, 152, 164, 174, 186, 196, 208, 218, 229, 241, 251, 263, 273, 285, 296, 306, 318, 328, 340, 351, 362, 373, 383, 395, 405, 417, 428, 439, 450, 460, 472, 483, 494, 505, 517, 527, 539, 549, 560, 572, 582, 594, 604, 616, 627, 637, 649, 659, 671, 681, 693, 704, 714, 726, 736, 748, 759, 770, 781, 791, 803, 814, 825, 836, 848, 858, 870]
    攻击次数2 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数 + (self.数据1[self.等级] + self.数据2[self.等级] * 3) * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.148

class 技能7(主动技能):
    名称 = '旋舞斩'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    数据=[0, 1819, 2004, 2188, 2373, 2557, 2742, 2927, 3111, 3296, 3480, 3665, 3850, 4034, 4219, 4403, 4588, 4773, 4957, 5142, 5326, 5511, 5696, 5880, 6065, 6249, 6434, 6619, 6803, 6988, 7172, 7357, 7542, 7726, 7911, 8095, 8280, 8465, 8649, 8834, 9018, 9203, 9388, 9572, 9757, 9943, 10127, 10312, 10497, 10681, 10866, 11050, 11235, 11420, 11604, 11789, 11973, 12158, 12343, 12527, 12712, 12896, 13081, 13266, 13450, 13635, 13819, 14004, 14189, 14373, 14558]
    数据1=[0, 364, 400, 437, 474, 511, 548, 585, 622, 659, 696, 733, 770, 807, 843, 880, 917, 954, 991, 1028, 1065, 1102, 1139, 1176, 1213, 1250, 1287, 1323, 1360, 1397, 1434, 1471, 1508, 1545, 1582, 1619, 1656, 1693, 1730, 1766, 1803, 1840, 1877, 1914, 1951, 1988, 2025, 2062, 2099, 2136, 2173, 2210, 2246, 2283, 2320, 2357, 2394, 2431, 2468, 2505, 2542, 2579, 2616, 2653, 2689, 2726, 2763, 2800, 2837, 2874, 2911]
    攻击次数3 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 7.0

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数 + self.数据1[self.等级] * self.攻击次数3) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.147


class 技能8(主动技能):
    名称 = '旋刃'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    数据=[0, 206, 228, 249, 270, 291, 311, 333, 354, 375, 397, 418, 438, 459, 480, 502, 523, 543, 564, 585, 607, 628, 649, 669, 691, 712, 733, 754, 774, 796, 817, 838, 859, 881, 901, 922, 943, 965, 986, 1007, 1027, 1048, 1070, 1091, 1112, 1132, 1153, 1175, 1196, 1217, 1238, 1259, 1280, 1301, 1322, 1344, 1364, 1385, 1406, 1427, 1449, 1470, 1490, 1511, 1532, 1554, 1575, 1596, 1616, 1638, 1659]
    数据1=[0, 285, 314, 343, 372, 400, 429, 459, 488, 517, 545, 574, 603, 633, 662, 691, 719, 748, 777, 806, 836, 864, 893, 922, 951, 980, 1008, 1038, 1067, 1096, 1125, 1153, 1182, 1212, 1241, 1270, 1299, 1327, 1356, 1385, 1415, 1444, 1472, 1501, 1530, 1559, 1588, 1618, 1646, 1675, 1704, 1733, 1761, 1791, 1820, 1849, 1878, 1907, 1935, 1964, 1994, 2023, 2052, 2080, 2109, 2138, 2168, 2197, 2226, 2254, 2283]
    数据2=[0, 389, 428, 468, 507, 547, 585, 626, 666, 704, 744, 783, 823, 862, 902, 941, 981, 1021, 1060, 1100, 1138, 1178, 1217, 1257, 1297, 1336, 1376, 1415, 1455, 1494, 1534, 1573, 1613, 1653, 1691, 1731, 1770, 1810, 1849, 1889, 1929, 1968, 2008, 2047, 2087, 2125, 2165, 2204, 2244, 2284, 2323, 2363, 2402, 2442, 2481, 2521, 2560, 2600, 2640, 2678, 2718, 2757, 2797, 2836, 2876, 2916, 2955, 2995, 3034, 3074, 3112]
    数据3=[0, 176, 194, 212, 230, 248, 266, 284, 301, 319, 337, 355, 373, 391, 409, 427, 445, 462, 480, 498, 516, 534, 552, 570, 588, 606, 624, 641, 659, 677, 695, 713, 731, 749, 767, 785, 803, 821, 839, 857, 874, 892, 910, 928, 946, 964, 982, 1000, 1017, 1035, 1053, 1071, 1089, 1107, 1125, 1143, 1161, 1178, 1196, 1214, 1232, 1250, 1268, 1286, 1304, 1321, 1339, 1357, 1375, 1393, 1411]
    攻击次数2 = 1
    TP成长 = 0.1
    TP上限 = 5
    CD = 8.0

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] * 3 + self.数据1[self.等级] * 3 +self.数据2[self.等级] * 3) * self.攻击次数 + self.数据3[self.等级] * 3 * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.161

class 技能9(主动技能):
    名称 = '剑刃风暴'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    数据=[0, 427, 471, 513, 557, 600, 644, 688, 731, 774, 817, 860, 905, 948, 990, 1034, 1077, 1120, 1165, 1208, 1251, 1294, 1337, 1382, 1425, 1468, 1511, 1554, 1599, 1642, 1685, 1729, 1771, 1814, 1859, 1902, 1945, 1989, 2031, 2075, 2119, 2162, 2206, 2248, 2292, 2336, 2379, 2422, 2466, 2508, 2552, 2596, 2639, 2682, 2726, 2769, 2813, 2856, 2899, 2943, 2987, 3029, 3073, 3116, 3159, 3203, 3247, 3290, 3333, 3376, 3420]
    数据1=[0, 855, 940, 1028, 1115, 1200, 1288, 1375, 1463, 1548, 1635, 1723, 1808, 1895, 1983, 2069, 2155, 2242, 2330, 2415, 2502, 2590, 2676, 2762, 2850, 2936, 3023, 3110, 3197, 3283, 3371, 3457, 3543, 3631, 3717, 3803, 3891, 3978, 4065, 4151, 4238, 4326, 4411, 4498, 4585, 4671, 4758, 4845, 4933, 5018, 5105, 5193, 5278, 5365, 5453, 5538, 5625, 5713, 5800, 5885, 5973, 6060, 6145, 6233, 6320, 6406, 6493, 6580, 6668, 6754, 6840]
    旋转次数 = 8
    攻击次数2 = 1
    CD = 12.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.旋转次数 * self.攻击次数 + self.数据1[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.05


class 技能10(主动技能):
    名称 = '螺旋穿刺'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据=[0, 576, 635, 694, 753, 811, 871, 928, 987, 1045, 1105, 1163, 1222, 1279, 1338, 1397, 1456, 1514, 1573, 1633, 1690, 1748, 1807, 1867, 1925, 1984, 2041, 2100, 2159, 2218, 2276, 2335, 2393, 2452, 2510, 2569, 2629, 2687, 2746, 2803, 2861, 2921, 2980, 3038, 3097, 3155, 3214, 3272, 3331, 3390, 3449, 3508, 3565, 3623, 3683, 3742, 3800, 3859, 3917, 3975, 4034, 4093, 4152, 4211, 4268, 4327, 4385, 4445, 4503, 4562, 4621]
    数据1=[0, 2021, 2227, 2431, 2635, 2841, 3046, 3251, 3457, 3662, 3867, 4071, 4277, 4482, 4687, 4893, 5098, 5303, 5508, 5713, 5918, 6124, 6328, 6532, 6737, 6943, 7148, 7353, 7559, 7764, 7968, 8174, 8379, 8584, 8789, 8995, 9200, 9405, 9610, 9815, 10020, 10226, 10429, 10634, 10839, 11045, 11250, 11455, 11661, 11866, 12070, 12276, 12481, 12686, 12892, 13097, 13302, 13506, 13712, 13917, 14122, 14328, 14531, 14736, 14942, 15147, 15352, 15558, 15763, 15967, 16172]
    数据2=[0, 1213, 1335, 1459, 1581, 1705, 1827, 1951, 2074, 2197, 2320, 2443, 2566, 2688, 2812, 2936, 3058, 3182, 3304, 3428, 3550, 3674, 3797, 3920, 4043, 4166, 4289, 4412, 4535, 4658, 4781, 4905, 5027, 5151, 5273, 5397, 5519, 5643, 5766, 5889, 6012, 6135, 6258, 6380, 6503, 6628, 6749, 6873, 6995, 7119, 7241, 7365, 7489, 7611, 7734, 7857, 7980, 8103, 8226, 8350, 8472, 8596, 8718, 8842, 8964, 9088, 9212, 9334, 9458, 9580, 9704]
    攻击次数2 = 1
    旋转次数 = 1
    旋转倍率 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.旋转倍率 = 2.25
        elif x == 1:
            self.旋转倍率 = 2.91

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] * self.旋转次数 * self.旋转倍率 + self.数据1[self.等级]) * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.141

class 技能11(主动技能):
    名称 = '雷光刃影'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    数据=[0, 4565, 5030, 5493, 5955, 6418, 6883, 7346, 7809, 8272, 8736, 9199, 9662, 10125, 10589, 11052, 11515, 11978, 12442, 12905, 13368, 13831, 14295, 14758, 15221, 15684, 16148, 16611, 17074, 17537, 18001, 18464, 18927, 19390, 19855, 20318, 20780, 21243, 21708, 22171, 22634, 23097, 23560, 24024, 24487, 24950, 25413, 25877, 26340, 26803, 27266, 27730, 28193, 28656, 29119, 29583, 30046, 30509, 30972, 31436, 31899, 32362, 32825, 33289, 33752, 34215, 34678, 35143, 35605, 36068, 36531] 
    数据1=[0, 3044, 3353, 3661, 3970, 4279, 4588, 4897, 5206, 5514, 5823, 6132, 6442, 6750, 7059, 7367, 7676, 7985, 8295, 8603, 8912, 9221, 9529, 9838, 10148, 10456, 10765, 11074, 11382, 11691, 12001, 12310, 12618, 12927, 13236, 13544, 13854, 14163, 14471, 14780, 15089, 15397, 15706, 16016, 16324, 16633, 16942, 17250, 17559, 17869, 18178, 18486, 18795, 19104, 19412, 19722, 20031, 20339, 20648, 20957, 21265, 21575, 21884, 22193, 22501, 22810, 23118, 23428, 23737, 24046, 24354]
    数据2=[0, 1521, 1676, 1830, 1984, 2139, 2294, 2449, 2603, 2757, 2912, 3066, 3220, 3374, 3529, 3683, 3837, 3992, 4147, 4302, 4456, 4610, 4765, 4919, 5073, 5228, 5382, 5536, 5691, 5845, 6000, 6155, 6309, 6463, 6618, 6772, 6926, 7081, 7235, 7389, 7544, 7698, 7852, 8008, 8162, 8317, 8471, 8625, 8780, 8934, 9088, 9242, 9397, 9551, 9705, 9861, 10015, 10170, 10324, 10478, 10633, 10787, 10941, 11096, 11250, 11404, 11559, 11714, 11868, 12023, 12177]
    攻击次数2 = 1
    CD = 15.0
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] + self.数据1[self.等级]) * self.攻击次数 + self.数据2[self.等级]* self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级)


class 技能12(主动技能):
    名称 = '疾风乱舞'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    数据=[0, 654, 720, 787, 853, 919, 986, 1053, 1119, 1185, 1252, 1318, 1384, 1451, 1517, 1584, 1650, 1717, 1783, 1849, 1915, 1982, 2048, 2115, 2182, 2248, 2314, 2380, 2447, 2513, 2579, 2646, 2713, 2779, 2845, 2912, 2978, 3044, 3110, 3178, 3244, 3310, 3377, 3443, 3509, 3575, 3643, 3709, 3775, 3841, 3908, 3974, 4040, 4108, 4174, 4240, 4306, 4373, 4439, 4505, 4571, 4639, 4705, 4771, 4838, 4904, 4970, 5036, 5104, 5170, 5236]
    数据1=[0, 651, 717, 784, 850, 916, 982, 1048, 1114, 1180, 1246, 1312, 1378, 1444, 1510, 1576, 1643, 1709, 1775, 1841, 1907, 1974, 2040, 2106, 2172, 2238, 2305, 2371, 2437, 2503, 2569, 2635, 2701, 2767, 2833, 2899, 2965, 3031, 3098, 3164, 3230, 3296, 3362, 3428, 3494, 3560, 3626, 3692, 3758, 3824, 3890, 3958, 4024, 4090, 4156, 4222, 4288, 4354, 4420, 4486, 4552, 4619, 4685, 4751, 4817, 4883, 4949, 5015, 5081, 5147, 5213]
    数据2=[0, 1171, 1290, 1409, 1527, 1646, 1765, 1884, 2002, 2122, 2241, 2359, 2478, 2597, 2716, 2834, 2954, 3073, 3191, 3310, 3429, 3548, 3666, 3785, 3905, 4023, 4142, 4261, 4380, 4498, 4617, 4737, 4855, 4974, 5093, 5212, 5330, 5449, 5568, 5686, 5806, 5925, 6044, 6162, 6281, 6400, 6520, 6638, 6757, 6876, 6994, 7113, 7232, 7351, 7469, 7589, 7708, 7826, 7945, 8064, 8183, 8301, 8420, 8540, 8658, 8777, 8896, 9015, 9133, 9252, 9372]
    数据3=[0, 2195, 2418, 2640, 2863, 3086, 3308, 3531, 3754, 3977, 4198, 4421, 4644, 4868, 5089, 5312, 5535, 5757, 5980, 6203, 6426, 6648, 6871, 7094, 7317, 7539, 7762, 7985, 8207, 8430, 8653, 8876, 9098, 9321, 9544, 9767, 9989, 10212, 10435, 10657, 10880, 11103, 11326, 11547, 11771, 11994, 12217, 12438, 12661, 12884, 13106, 13329, 13552, 13775, 13997, 14220, 14443, 14666, 14888, 15111, 15334, 15557, 15779, 16002, 16225, 16447, 16670, 16893, 17116, 17338, 17561]
    攻击次数2 = 1
    CD = 25.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    乱舞数 = 11
    分身乱舞数 = 4
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.分身乱舞数 *= 2.1
            self.攻击次数2 *= 1.08
            self.CD *= 0.9
        elif x == 1:
            self.分身乱舞数 *= 2.88
            self.攻击次数2 *= 1.08
            self.CD *= 0.9

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级]*self.乱舞数 + self.数据1[self.等级] * self.分身乱舞数 + self.数据2[self.等级]) * self.攻击次数 + self.数据3[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.05


class 技能13(主动技能):
    名称 = '绝命瞬狱杀'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    数据=[0, 1598, 1759, 1922, 2084, 2245, 2408, 2570, 2732, 2894, 3057, 3218, 3381, 3542, 3705, 3867, 4028, 4191, 4353, 4515, 4677, 4840, 5001, 5164, 5326, 5487, 5650, 5812, 5974, 6136, 6299, 6460, 6623, 6785, 6947, 7109, 7270, 7433, 7595, 7757, 7919, 8082, 8243, 8406, 8568, 8729, 8892, 9055, 9216, 9378, 9541, 9702, 9865, 10027, 10189, 10351, 10514, 10675, 10837, 11000, 11161, 11324, 11485, 11648, 11810, 11972, 12134, 12297, 12458, 12620, 12783]
    数据1=[0, 2396, 2640, 2882, 3126, 3369, 3612, 3855, 4099, 4341, 4585, 4828, 5070, 5314, 5557, 5801, 6043, 6287, 6529, 6773, 7016, 7260, 7502, 7746, 7989, 8232, 8475, 8719, 8961, 9205, 9448, 9691, 9934, 10178, 10420, 10664, 10907, 11149, 11393, 11636, 11879, 12122, 12366, 12608, 12852, 13095, 13339, 13581, 13825, 14068, 14311, 14554, 14798, 15040, 15284, 15527, 15770, 16013, 16257, 16499, 16742, 16986, 17228, 17472, 17715, 17958, 18201, 18445, 18687, 18931, 19174]
    数据2=[0, 3195, 3519, 3843, 4168, 4492, 4816, 5141, 5465, 5789, 6114, 6437, 6761, 7085, 7410, 7734, 8058, 8383, 8707, 9031, 9356, 9680, 10003, 10328, 10652, 10976, 11300, 11625, 11949, 12273, 12598, 12922, 13245, 13570, 13894, 14218, 14542, 14867, 15191, 15515, 15840, 16164, 16487, 16812, 17136, 17460, 17785, 18109, 18433, 18757, 19082, 19406, 19729, 20054, 20378, 20702, 21027, 21351, 21675, 22000, 22324, 22648, 22971, 23297, 23620, 23944, 24269, 24593, 24917, 25242, 25566]
    数据3=[0, 3994, 4400, 4805, 5210, 5615, 6020, 6426, 6831, 7236, 7642, 8047, 8452, 8857, 9262, 9668, 10073, 10478, 10884, 11289, 11694, 12099, 12504, 12910, 13315, 13721, 14126, 14531, 14936, 15341, 15747, 16152, 16557, 16963, 17368, 17773, 18178, 18583, 18989, 19394, 19800, 20205, 20610, 21015, 21420, 21825, 22231, 22636, 23042, 23447, 23852, 24257, 24662, 25068, 25473, 25878, 26284, 26689, 27094, 27499, 27904, 28310, 28715, 29121, 29526, 29931, 30336, 30741, 31146, 31552, 31957]
    数据4=[0, 2237, 2463, 2690, 2917, 3144, 3371, 3598, 3825, 4052, 4279, 4506, 4733, 4959, 5186, 5413, 5640, 5867, 6095, 6322, 6549, 6776, 7003, 7230, 7457, 7683, 7910, 8137, 8364, 8591, 8818, 9045, 9272, 9499, 9726, 9953, 10179, 10406, 10633, 10860, 11087, 11314, 11541, 11768, 11995, 12222, 12450, 12677, 12902, 13129, 13357, 13584, 13811, 14038, 14265, 14492, 14719, 14946, 15173, 15400, 15626, 15853, 16080, 16307, 16534, 16761, 16988, 17215, 17442, 17669, 17896]
    攻击次数2 = 1
    CD = 45.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= 1.4805
        elif x== 1:
            self.攻击次数2 *= 1.6356
    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] + self.数据1[self.等级] + self.数据2[self.等级] + self.数据3[self.等级]) * self.攻击次数 + self.数据4[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.132



class 技能14(主动技能):
    名称 = '月轮舞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 40326
    成长 = 12177
    数据=[0, 10501, 12936, 15372, 17807, 20243, 22679, 25114, 27548, 29983, 32420, 34855, 37290, 39726, 42162, 44596, 47031, 49467, 51902, 54338, 56774, 59209, 61643, 64078, 66515, 68950, 71385, 73821, 76257, 78691, 81126, 83562, 85997, 88433, 90869, 93304, 95738, 98173, 100610, 103045, 105480]
    攻击次数 = 5
    CD = 145
    def 等效百分比(self,武器类型):
        return self.数据[self.等级] * self.攻击次数 * self.倍率 * 1.179
    def 等效CD(self, 武器类型,输出类型):
        if 武器类型 == '双剑':
            return round(self.CD  / self.恢复, 1)
        else:
            return round(self.CD  / self.恢复 * 武器冷却惩罚(武器类型,输出类型,self.版本), 1)


class 技能15(主动技能):
    名称 = '旋刃冲击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    数据=[0, 415, 457, 499, 541, 583, 626, 668, 710, 752, 794, 836, 878, 921, 963, 1005, 1047, 1089, 1131, 1173, 1216, 1258, 1300, 1342, 1384, 1426, 1468, 1511, 1553, 1595, 1637, 1679, 1721, 1763, 1805, 1848, 1890, 1932, 1974, 2016, 2058, 2100, 2143, 2185, 2227, 2269, 2311, 2353, 2395, 2438, 2480, 2522, 2564, 2606, 2648, 2690, 2733, 2775, 2817, 2859, 2901, 2943, 2985, 3028, 3070, 3112, 3154, 3196, 3238, 3280, 3323]
    数据1=[0, 465, 512, 559, 606, 653, 701, 748, 795, 842, 889, 936, 983, 1032, 1079, 1126, 1173, 1220, 1267, 1314, 1362, 1409, 1456, 1503, 1550, 1597, 1644, 1692, 1739, 1786, 1833, 1880, 1928, 1975, 2022, 2070, 2117, 2164, 2211, 2258, 2305, 2352, 2400, 2447, 2494, 2541, 2588, 2635, 2682, 2731, 2778, 2825, 2872, 2919, 2966, 3013, 3061, 3108, 3155, 3202, 3249, 3296, 3343, 3391, 3438, 3485, 3532, 3580, 3627, 3674, 3722]
    攻击次数 = 29
    攻击次数2 = 5
    攻击次数4 = 0
    CD = 30.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 = 35
            self.攻击次数2 *= 0.2
            self.攻击次数4 = 30
            self.CD *= 0.89
        elif x == 1:
            self.攻击次数 = 37.45
            self.攻击次数2 *= 0.214
            self.攻击次数4 = 32.1
            self.CD *= 0.89

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * self.攻击次数 + self.数据1[self.等级] * self.攻击次数2 + self.数据[self.等级] * self.攻击次数4) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.155


class 技能16(主动技能):
    名称 = '陨落螺旋刺'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    数据=[0, 1990, 2193, 2394, 2596, 2797, 3000, 3202, 3403, 3606, 3808, 4009, 4212, 4413, 4615, 4817, 5019, 5221, 5423, 5625, 5827, 6028, 6231, 6433, 6634, 6837, 7039, 7240, 7442, 7645, 7846, 8048, 8251, 8452, 8654, 8857, 9058, 9260, 9461, 9664, 9866, 10067, 10270, 10472, 10673, 10876, 11078, 11279, 11482, 11684, 11885, 12087, 12290, 12491, 12693, 12895, 13097, 13299, 13501, 13703, 13905, 14106, 14309, 14510, 14712, 14915, 15116, 15318, 15521, 15722, 15924]
    数据1=[0, 13933, 15348, 16761, 18175, 19588, 21001, 22415, 23828, 25243, 26657, 28070, 29483, 30897, 32310, 33724, 35137, 36552, 37965, 39379, 40792, 42206, 43619, 45033, 46446, 47861, 49274, 50688, 52101, 53515, 54928, 56342, 57755, 59170, 60583, 61997, 63410, 64824, 66237, 67650, 69065, 70479, 71892, 73305, 74719, 76132, 77546, 78959, 80374, 81787, 83201, 84614, 86028, 87441, 88855, 90268, 91683, 93096, 94510, 95923, 97337, 98750, 100164, 101577, 102992, 104405, 105819, 107232, 108646, 110059, 111472]
    数据2=[0, 3981, 4385, 4788, 5193, 5596, 6000, 6404, 6808, 7212, 7615, 8019, 8424, 8827, 9231, 9634, 10039, 10443, 10846, 11251, 11654, 12058, 12463, 12866, 13270, 13675, 14078, 14482, 14885, 15290, 15694, 16097, 16501, 16905, 17309, 17713, 18116, 18521, 18924, 19328, 19733, 20136, 20540, 20943, 21348, 21752, 22155, 22560, 22964, 23367, 23772, 24175, 24579, 24983, 25387, 25791, 26194, 26598, 27003, 27406, 27810, 28213, 28618, 29022, 29425, 29830, 30233, 30637, 31042, 31445, 31849]
    倍率1 = 1
    倍率2 = 1
    攻击次数2 = 1
    CD = 50.0
    TP成长 = 0.1
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率1 = 0
            self.倍率2 = 2.04
        elif x == 1:
            self.倍率1 = 0
            self.倍率2 = 2.27

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] * 3 * self.倍率1 + self.数据1[self.等级] * self.倍率2) * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * (1 + self.TP成长 * self.TP等级) * 1.142


class 技能17(主动技能):
    名称 = '乱空杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    数据=[0, 2284, 2648, 3013, 3377, 3741, 4106, 4470, 4834, 5199, 5563, 5927, 6292, 6656, 7020, 7385, 7749, 8113, 8476, 8840, 9205, 9569, 9933, 10298, 10662, 11026, 11391, 11755, 12119, 12484, 12848, 13212, 13577, 13941, 14305, 14670, 15034, 15398, 15763, 16127, 16491]
    数据1=[0, 9139, 10596, 12054, 13511, 14968, 16424, 17881, 19339, 20796, 22253, 23711, 25166, 26624, 28081, 29538, 30996, 32453, 33909, 35366, 36824, 38281, 39738, 41196, 42653, 44109, 45566, 47023, 48481, 49938, 51395, 52851, 54308, 55766, 57223, 58680, 60138, 61593, 63051, 64508, 65966]
    数据2=[0, 4569, 5298, 6027, 6755, 7484, 8211, 8940, 9669, 10397, 11126, 11855, 12583, 13312, 14041, 14769, 15498, 16227, 16954, 17682, 18411, 19140, 19868, 20597, 21326, 22054, 22783, 23512, 24240, 24969, 25698, 26425, 27153, 27882, 28611, 29339, 30068, 30797, 31525, 32254, 32983]
    攻击次数2 = 1
    CD = 30.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.17
            self.攻击次数2 *= 1.17
            self.CD *= 0.89

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] * 6 + self.数据1[self.等级]) * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 *1.158


class 技能18(主动技能):
    名称 = '月影突袭'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    数据=[0, 3340, 3680, 4019, 4357, 4696, 5035, 5374, 5714, 6052, 6391, 6730, 7069, 7407, 7746, 8086, 8425, 8764, 9102, 9441, 9780, 10120, 10459, 10797, 11136, 11475, 11814, 12152, 12492, 12831, 13170, 13509, 13847, 14186, 14526, 14865, 15204, 15542, 15881, 16220, 16559]
    数据1=[0, 6681, 7360, 8037, 8715, 9393, 10071, 10748, 11427, 12105, 12782, 13460, 14138, 14816, 15493, 16172, 16850, 17527, 18206, 18883, 19561, 20240, 20917, 21595, 22272, 22951, 23628, 24306, 24985, 25662, 26340, 27018, 27696, 28373, 29052, 29730, 30407, 31086, 31763, 32441, 33118]
    攻击次数2 = 1
    CD = 50.0
    是否有护石 = 1
    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数 *= 1.35
            self.攻击次数2 *= 1.35

    def 等效百分比(self, 武器类型):
        return (self.数据[self.等级] * 10 * self.攻击次数 + self.数据1[self.等级] * self.攻击次数2) * self.倍率 * 1.156


class 技能19(主动技能):
    名称 = '天渊星狱'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    数据=[0, 296, 364, 433, 501, 571, 639, 708, 776, 845, 914, 983, 1051, 1120, 1189, 1258, 1326, 1395, 1464, 1533, 1601, 1669, 1738, 1808, 1876, 1944, 2013, 2082, 2151, 2219, 2288, 2357, 2426, 2494, 2563, 2631, 2701, 2769, 2838, 2906, 2976, 3044, 3112, 3181, 3249, 3319, 3387, 3456, 3524, 3594, 3662, 3731, 3799, 3869, 3937, 4006, 4074, 4143, 4212, 4281, 4349, 4417, 4487, 4556, 4624, 4692, 4761, 4830, 4899, 4967, 5036]
    数据1=[0, 68441, 84311, 100182, 116053, 131922, 147793, 163664, 179534, 195405, 211275, 227146, 243017, 258886, 274757, 290628, 306498, 322369, 338240, 354110, 369981, 385850, 401721, 417592, 433462, 449333, 465204, 481073, 496944, 512814, 528685, 544556, 560426, 576297, 592168, 608037, 623908, 639778, 655649, 671520, 687390, 703261, 719132, 735001, 750872, 766743, 782613, 798484, 814354, 830224, 846095, 861965, 877836, 893707, 909577, 925448, 941317, 957188, 973059, 988929, 1004800, 1020671, 1036541, 1052412, 1068281, 1084152, 1100023, 1115893, 1131764, 1147635, 1163504]
    数据2=[0, 14221, 17519, 20817, 24114, 27412, 30709, 34007, 37305, 40603, 43901, 47199, 50496, 53794, 57092, 60390, 63688, 66986, 70284, 73581, 76878, 80176, 83474, 86771, 90069, 93367, 96665, 99963, 103261, 106559, 109856, 113154, 116452, 119750, 123048, 126344, 129642, 132940, 136238, 139536, 142834, 146131, 149429, 152727, 156025, 159323, 162621, 165919, 169216, 172514, 175812, 179109, 182406, 185704, 189002, 192300, 195598, 198896, 202194, 205491, 208789, 212087, 215385, 218683, 221981, 225278, 228576, 231873, 235171, 238469, 241766]
    攻击次数2 = 1
    CD = 180

    def 等效百分比(self, 武器类型):
        return ((self.数据[self.等级] * 8 + self.数据1[self.等级]) * self.攻击次数 + self.数据2[self.等级] * self.攻击次数2) * self.倍率 * 1.169


class 技能20(被动技能):
    名称 = '死亡风暴'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 22
    关联技能 = ['无']
    数据=[0, 364, 401, 438, 477, 514, 552, 589, 627, 666, 703, 741, 778, 816, 854, 891, 928, 966, 1003, 1041, 1079, 1117, 1154, 1192, 1229, 1268, 1306, 1342, 1379, 1417, 1454, 1493, 1531, 1568, 1606, 1643, 1682, 1719, 1757, 1794, 1831, 1868, 1907, 1944, 1982, 2019, 2057, 2096, 2133, 2171, 2208, 2246, 2282, 2321, 2358, 2396, 2433, 2471, 2510, 2547, 2585, 2622, 2660, 2698, 2736, 2772, 2810, 2847, 2885, 2923, 2961]
    匕首数量 = 30
    倍率 = 1
    def 额外百分比(self):
            return self.数据[self.等级] * self.匕首数量 * 1.152 * self.倍率

class 技能21(被动技能):
    名称 =  '绝命时刻'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能22(主动技能):
    名称 = '幻灭瞬杀'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    基础 = 12277.8
    成长 = 1397.2
    攻击次数 = 5
    基础1 = 12277.8
    成长1 = 1397.2    
    攻击次数2 = 1
    CD = 60

    def 等效百分比(self, 武器类型):
        return ((self.基础 + self.成长*self.等级) * self.攻击次数 + (self.基础1 + self.成长1*self.等级) * self.攻击次数2) * self.倍率

class 技能23(主动技能):
    名称 = '影·万古星辰'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    基础 = 12680
    成长 = 3829
    攻击次数 = 13
    基础1 = 32971
    成长1 = 9954
    攻击次数2 = 1
    CD = 290

    def 等效百分比(self, 武器类型):
        return ((self.基础 + self.成长*self.等级) * self.攻击次数 + (self.基础1 + self.成长1*self.等级) * self.攻击次数2) * self.倍率
    
    关联技能 = ['无']
    def 加成倍率(self, 武器类型):
        return 0.0

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

    实际名称 = '隐夜·刺客'
    角色 = '暗夜使者'
    职业 = '刺客'

    武器选项 = ['匕首', '双剑']
    
    类型选择 = ['物理百分比']
    
    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 1.77
   
    def __init__(self):
        基础属性输入(self)
        self.技能栏= deepcopy(技能列表)
        self.技能序号= deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        for i in self.技能栏:
            if i.是否有伤害 == 1:
                i.攻击次数2 *= self.技能栏[0].终结追击倍率()
                i.攻击次数3 *= self.技能栏[0].终结追击倍率()
        if self.武器类型 == '双剑':
            self.技能栏[1].关联技能 = ['无']
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    i.攻击次数2 *= self.技能栏[2].终结追击倍率() * 3.25
                    i.攻击次数3 *= self.技能栏[2].终结追击倍率()
                    if self.装备栏[11] == '血色舞会':
                        i.攻击次数2 *= 1.4
                        i.攻击次数3 *= 1.4
            if self.装备栏[11] == '一叶障目':
                self.技能栏[self.技能序号['死亡风暴']].倍率 *= 1.32
        elif self.武器类型 == '匕首':
            self.技能栏[2].关联技能 = ['无']
            for i in self.技能栏:
                if i.是否有伤害 == 1:
                    i.攻击次数2 *= 4.25

    def 数据计算(self, x = 0, y = -1):
        self.预处理()
        #初步计算
        技能释放次数 = self.技能释放次数计算()
        技能单次伤害 = self.技能单次伤害计算(y)
        技能总伤害 = self.技能总伤害计算(技能释放次数, 技能单次伤害)

        #死亡风暴伤害
        if 技能总伤害[self.技能序号['剑刃风暴']] != 0:
            技能释放次数[self.技能序号['死亡风暴']] = 1
            技能总伤害[self.技能序号['死亡风暴']] = 技能总伤害[self.技能序号['剑刃风暴']] * self.技能栏[self.技能序号['死亡风暴']].额外百分比() / self.技能栏[self.技能序号['剑刃风暴']].等效百分比(self.武器类型)

        #返回结果
        return self.数据返回(x, 技能释放次数, 技能总伤害)
      
class 隐夜·刺客(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)

    def 界面(self):
        super().界面()
        self.收招选择 = []
        self.打桩展示 = QPushButton('打桩展示(25S)',self.main_frame2)
        self.打桩展示.setStyleSheet(按钮样式)
        self.打桩展示.resize(100,25)
        self.打桩展示.move(990, self.height() - 100)
        self.打桩展示.clicked.connect(lambda state, index = 0: QDesktopServices.openUrl(QUrl('https://www.bilibili.com/video/BV1454y1t71Y')))
        count = 0
        for i in self.初始属性.技能栏:
            if i.是否有伤害 == 1:
                if i.攻击次数2 != 0:
                    self.收招选择.append(QCheckBox(i.名称 + '-收招',self.main_frame2))
                    self.收招选择[count].resize(120,20)
                    self.收招选择[count].move(335 + 135 * int(count / 7),440 + 26 * (count % 7))
                    self.收招选择[count].setStyleSheet(复选框样式)
                    self.收招选择[count].setChecked(True)
                    count += 1

        self.旋舞斩收招次数=MyQComboBox(self.main_frame2)
        for i in range(8):
            self.旋舞斩收招次数.addItem('旋舞斩收招次数:'+str(i))
        self.旋舞斩收招次数.resize(170,20)
        self.旋舞斩收招次数.move(600,470)
        self.旋舞斩收招次数.setToolTip('匕首最高7次，双剑最高6次')

        self.剑刃风暴旋转次数=MyQComboBox(self.main_frame2)
        for i in range(1,11):
            self.剑刃风暴旋转次数.addItem('剑刃风暴旋转次数:'+str(i))
        self.剑刃风暴旋转次数.resize(170,20)
        self.剑刃风暴旋转次数.move(600,498)
        self.剑刃风暴旋转次数.setToolTip('旋转次数最高10次')
        self.剑刃风暴旋转次数.setCurrentIndex(8)

        self.螺旋穿刺旋转次数=MyQComboBox(self.main_frame2)
        for i in range(7):
            self.螺旋穿刺旋转次数.addItem('螺旋穿刺旋转次数:'+str(i))
        self.螺旋穿刺旋转次数.resize(170,20)
        self.螺旋穿刺旋转次数.move(600,526)
        self.螺旋穿刺旋转次数.setToolTip('旋转次数最高6次，护石旋转次数为3倍')

        self.死亡风暴攻击次数=MyQComboBox(self.main_frame2)
        for i in range(1,31):
            self.死亡风暴攻击次数.addItem('死亡风暴攻击次数:'+str(i))
        self.死亡风暴攻击次数.resize(170,20)
        self.死亡风暴攻击次数.move(600,554)
        self.死亡风暴攻击次数.setToolTip('最高30次')
        self.死亡风暴攻击次数.setCurrentIndex(27)

    def 载入配置(self, path='set'):
        super().载入配置(path)
        try:
            setfile = open('./ResourceFiles/' + self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'r',encoding='utf-8').readlines()
            count = 0
            for item in self.收招选择:
                item.setChecked(True if int(setfile[count].replace('\n', ''))==1 else False)
                count +=1
            self.旋舞斩收招次数.setCurrentIndex(int(setfile[count].replace('\n', '')))
            self.剑刃风暴旋转次数.setCurrentIndex(int(setfile[count+1].replace('\n', '')))
            self.螺旋穿刺旋转次数.setCurrentIndex(int(setfile[count+2].replace('\n', '')))
            self.死亡风暴攻击次数.setCurrentIndex(int(setfile[count+3].replace('\n', '')))

        except:
            pass

    def 保存配置(self, path='set'):
        if self.禁用存档.isChecked():
            return
        super().保存配置(path)
        try:
            setfile = open('./ResourceFiles/'+self.角色属性A.实际名称 + '/' + path + '/skill5.ini', 'w', encoding='utf-8')
            for item in self.收招选择:
                setfile.write('1\n' if item.isChecked() else '0\n')
            setfile.write(str(self.旋舞斩收招次数.currentIndex())+'\n')
            setfile.write(str(self.剑刃风暴旋转次数.currentIndex())+'\n')
            setfile.write(str(self.螺旋穿刺旋转次数.currentIndex())+'\n')
            setfile.write(str(self.死亡风暴攻击次数.currentIndex())+'\n')
        except:
            pass


    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性, x)
        count = 0
        for i in 属性.技能栏:
            if i.是否有伤害 == 1:
                if i.攻击次数2 != 0:
                    if not self.收招选择[count].isChecked():
                        i.攻击次数2 = 0
                        i.攻击次数4 = 0
                    count += 1
        
        属性.技能栏[属性.技能序号['旋舞斩']].攻击次数3 = self.旋舞斩收招次数.currentIndex()
        属性.技能栏[属性.技能序号['剑刃风暴']].旋转次数 = self.剑刃风暴旋转次数.currentIndex() + 1
        属性.技能栏[属性.技能序号['螺旋穿刺']].旋转次数 = self.螺旋穿刺旋转次数.currentIndex()
        属性.技能栏[属性.技能序号['死亡风暴']].匕首数量 = self.死亡风暴攻击次数.currentIndex() + 1