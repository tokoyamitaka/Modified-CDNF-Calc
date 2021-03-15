from PublicReference.base import *

等级 = 100 + 5

class 主动技能(主动技能):
    def 等效CD(self, 武器类型,输出类型):
        return round(self.CD  / self.恢复, 1)

class 技能0(主动技能):
    名称 = '天诛'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 447, 501, 559, 612, 666, 718, 773, 828, 882, 935, 991, 1044, 1100, 1154, 1205, 1263, 1316, 1367, 1424,1477, 1532, 1586, 1640, 1696, 1747, 1800, 1858, 1909, 1965, 2019, 2073, 2128, 2181, 2235, 2290, 2345, 2400,2451, 2505, 2562, 2614, 2670, 2723, 2775, 2833, 2887, 2938, 2993, 3046, 3104, 3156, 3210, 3265, 3319, 3372,3427, 3479, 3537, 3591, 3642, 3698, 3752, 3808, 3860, 3914, 3969, 4021, 4075, 4133, 4184]
    攻击次数1 = 2
    数据2 = [0, 1871, 2097, 2324, 2551, 2771, 3000, 3224, 3453, 3677, 3904, 4126, 4354, 4580, 4804, 5030, 5257, 5482,5709, 5930, 6159, 6383, 6613, 6835, 7063, 7286, 7515, 7738, 7964, 8191, 8418, 8646, 8866, 9095, 9319, 9548,9771, 9997, 10221, 10448, 10675, 10900, 11124, 11353, 11577, 11804, 12027, 12254, 12480, 12704, 12930, 13157,13382, 13609, 13833, 14060, 14286, 14513, 14733, 14962, 15189, 15415, 15642, 15865, 16092, 16318, 16546,16766, 16995, 17219, 17448]
    攻击次数2 = 1
    CD = 6.3
    攻击倍率 = 1.101
    TP成长 = 0.08
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能1(主动技能):
    名称 = '割喉'
    所在等级 = 15
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1501, 1654, 1806, 1960, 2113, 2263, 2418, 2567, 2722, 2876, 3026, 3179, 3332, 3484, 3636, 3788, 3942, 4096,4246, 4398, 4551, 4703, 4856, 5010, 5162, 5314, 5465, 5620, 5773, 5923, 6076, 6229, 6381, 6534, 6685, 6837,6991, 7143, 7296, 7447, 7600, 7753, 7908, 8058, 8210, 8362, 8516, 8669, 8821, 8974, 9125, 9278, 9432, 9585,9735, 9888, 10040, 10193, 10344, 10498, 10650, 10802, 10957, 11107, 11259, 11412, 11566, 11719, 11869, 12021]
    攻击次数1 = 1
    数据2 = [0, 751, 827, 904, 981, 1057, 1133, 1208, 1285, 1362, 1437, 1513, 1590, 1666, 1742, 1818, 1895, 1970, 2047,2124, 2198, 2274, 2352, 2428, 2504, 2580, 2656, 2732, 2809, 2887, 2961, 3037, 3114, 3190, 3268, 3344, 3420,3496, 3572, 3649, 3723, 3802, 3875, 3953, 4030, 4105, 4181, 4256, 4334, 4411, 4486, 4563, 4639, 4715, 4792,4868, 4944, 5021, 5097, 5172, 5250, 5325, 5401, 5477, 5554, 5630, 5707, 5782, 5858, 5935, 6011]
    攻击次数2 = 1
    CD = 5.4
    攻击倍率 = 1.151
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能2(被动技能):
    名称 = '暗杀教义'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.185 + 0.015 * self.等级, 5)

class 技能3(主动技能):
    名称 = '夺魂'
    所在等级 = 20
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 1464, 1613, 1761, 1911, 2059, 2207, 2356, 2504, 2654, 2803, 2950, 3098, 3248, 3396, 3544, 3694, 3842, 3991,4139, 4287, 4437, 4586, 4733, 4882, 5032, 5178, 5328, 5476, 5625, 5774, 5923, 6073, 6220, 6368, 6517, 6665,6815, 6964, 7111, 7259, 7410, 7558, 7706, 7856, 8003, 8152, 8301, 8449, 8598, 8747, 8894, 9045, 9193, 9340,9489, 9638, 9786, 9936, 10082, 10230, 10381, 10529, 10679, 10828, 10976, 11125, 11272, 11421, 11571, 11719]
    攻击次数 = 1
    CD = 2.7
    攻击倍率 = 1.119
    TP成长 = 0.1
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能4(被动技能):
    名称 = '暗杀之匕首精通'
    所在等级 = 20
    等级上限 = 30
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 20:
                return round(1.0 + 0.015 * self.等级, 5)
            else:
                return round(1.3 + 0.025 * (self.等级 - 20), 5)


    def 物理攻击力倍率(self, 武器类型):
        return self.加成倍率(武器类型)

class 技能5(主动技能):
    名称 = '穿心'
    所在等级 = 25
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 2486, 2737, 2992, 3245, 3496, 3750, 4000, 4253, 4505, 4757, 5011, 5263, 5514, 5765, 6020, 6271, 6524, 6775,7027, 7285, 7534, 7787, 8039, 8292, 8543, 8796, 9047, 9300, 9555, 9806, 10057, 10309, 10561, 10812, 11067,11320, 11569, 11823, 12074, 12328, 12581, 12834, 13089, 13339, 13591, 13843, 14096, 14345, 14602, 14851,15104, 15357, 15608, 15862, 16113, 16365, 16616, 16871, 17122, 17374, 17630, 17880, 18134, 18386, 18638,18890, 19141, 19394, 19647, 19900]
    攻击次数1 = 1
    数据2 = [0, 1242, 1370, 1496, 1621, 1748, 1875, 2001, 2126, 2253, 2378, 2504, 2632, 2758, 2884, 3010, 3138, 3263,3387, 3515, 3641, 3766, 3893, 4021, 4146, 4272, 4399, 4524, 4649, 4777, 4900, 5029, 5155, 5283, 5408, 5534,5660, 5785, 5912, 6038, 6162, 6291, 6417, 6543, 6668, 6795, 6922, 7046, 7174, 7300, 7428, 7552, 7680, 7805,7930, 8057, 8183, 8308, 8434, 8562, 8687, 8814, 8942, 9067, 9191, 9319, 9445, 9571, 9696, 9824, 9951]
    攻击次数2 = 1
    攻击倍率 = 1.112
    CD = 7.2
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率


class 技能6(主动技能):
    名称 = '追命'
    所在等级 = 30
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 3093, 3405, 3721, 4035, 4348, 4659, 4975, 5288, 5601, 5915, 6230, 6543, 6856, 7171, 7486, 7796, 8111, 8424,8741, 9054, 9368, 9682, 9995, 10310, 10622, 10936, 11250, 11563, 11877, 12190, 12507, 12818, 13133, 13448,13758, 14072, 14387, 14702, 15015, 15329, 15642, 15957, 16271, 16584, 16900, 17211, 17525, 17837, 18151,18467, 18779, 19096, 19406, 19722, 20034, 20348, 20664, 20977, 21291, 21604, 21918, 22230, 22544, 22858,23172, 23487, 23799, 24114, 24428, 24741]
    攻击次数 = 1
    攻击倍率 = 1.5 * 1.121
    CD = 9.0
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * self.攻击倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率


class 技能7(主动技能):
    名称 = '潜影刺击'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 990, 1091, 1192, 1290, 1393, 1494, 1593, 1693, 1795, 1894, 1996, 2096, 2196, 2297, 2397, 2496, 2598, 2700,2799, 2899, 3001, 3100, 3201, 3304, 3404, 3503, 3604, 3705, 3805, 3906, 4007, 4107, 4208, 4308, 4407, 4509,4611, 4710, 4810, 4912, 5011, 5111, 5213, 5312, 5414, 5514, 5615, 5715, 5817, 5915, 6018, 6118, 6217, 6318,6419, 6519, 6620, 6721, 6821, 6922, 7022, 7121, 7223, 7325, 7425, 7524, 7626, 7728, 7825, 7927]
    攻击次数1 = 2
    数据2 = [0, 4756, 5239, 5720, 6203, 6687, 7170, 7650, 8136, 8619, 9101, 9583, 10066, 10550, 11030, 11513, 11997,12480, 12961, 13444, 13927, 14411, 14891, 15374, 15858, 16338, 16822, 17305, 17788, 18270, 18752, 19235,19719, 20201, 20685, 21168, 21651, 22132, 22615, 23098, 23579, 24062, 24546, 25029, 25509, 25993, 26476,26960, 27440, 27923, 28407, 28888, 29370, 29855, 30337, 30819, 31302, 31785, 32270, 32750, 33233, 33717,34200, 34681, 35164, 35647, 36129, 36611, 37095, 37578, 38059]
    攻击次数2 = 1
    攻击倍率 = 1.11
    CD = 13.5
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率  * self.攻击倍率

class 技能8(主动技能):
    名称 = '刃舞（打满）'
    所在等级 = 35
    等级上限 = 1
    #1学习间隔 = 2
    #等级精通 = 50
    基础等级 = 1
    数据1 = [0, 237, 261, 288, 312, 337, 361, 384, 408, 435, 456, 482, 503, 529, 554, 579, 603, 627, 649, 675, 698, 724,749, 773, 796, 821, 846, 868, 894, 918, 941, 966, 991, 1013, 1040, 1062, 1087, 1110, 1136, 1157, 1185, 1210,1233, 1258, 1280, 1304, 1330, 1354, 1378, 1403, 1427, 1450, 1473, 1500, 1522, 1548, 1571, 1595, 1620, 1645,1669, 1692, 1718, 1741, 1768, 1790, 1815, 1839, 1862, 1885, 1911]
    攻击次数1 = 18
    数据2 = [0, 4061, 4473, 4885, 5297, 5709, 6121, 6533, 6942, 7354, 7766, 8177, 8589, 9003, 9415, 9826, 10238, 10650,11062, 11473, 11887, 12299, 12711, 13122, 13534, 13949, 14357, 14769, 15182, 15594, 16005, 16418, 16830,17241, 17652, 18064, 18477, 18890, 19301, 19713, 20125, 20537, 20948, 21360, 21773, 22184, 22594, 23008,23418, 23830, 24244, 24656, 25066, 25478, 25892, 26304, 26716, 27128, 27540, 27952, 28361, 28773, 29188,29600, 30010, 30422, 30834, 31246, 31657, 32072, 32484]
    攻击次数2 = 1
    CD = 13.5
    攻击倍率 = 1.11
    #TP成长 = 0.10
    #TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率  * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 18 * 2 * 0.62 * 1.16
            self.攻击次数2 = 1
        elif x == 1:
            self.攻击次数1 = 18 * 2 * (0.62 * 1.3)
            self.攻击次数2 *= 1.26

class 技能9(主动技能):
    名称 = '刃舞（2hit+终结）'
    所在等级 = 35
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 237, 261, 288, 312, 337, 361, 384, 408, 435, 456, 482, 503, 529, 554, 579, 603, 627, 649, 675, 698, 724,749, 773, 796, 821, 846, 868, 894, 918, 941, 966, 991, 1013, 1040, 1062, 1087, 1110, 1136, 1157, 1185, 1210,1233, 1258, 1280, 1304, 1330, 1354, 1378, 1403, 1427, 1450, 1473, 1500, 1522, 1548, 1571, 1595, 1620, 1645,1669, 1692, 1718, 1741, 1768, 1790, 1815, 1839, 1862, 1885, 1911]
    攻击次数1 = 2
    数据2 = [0, 4061, 4473, 4885, 5297, 5709, 6121, 6533, 6942, 7354, 7766, 8177, 8589, 9003, 9415, 9826, 10238, 10650,11062, 11473, 11887, 12299, 12711, 13122, 13534, 13949, 14357, 14769, 15182, 15594, 16005, 16418, 16830,17241, 17652, 18064, 18477, 18890, 19301, 19713, 20125, 20537, 20948, 21360, 21773, 22184, 22594, 23008,23418, 23830, 24244, 24656, 25066, 25478, 25892, 26304, 26716, 27128, 27540, 27952, 28361, 28773, 29188,29600, 30010, 30422, 30834, 31246, 31657, 32072, 32484]
    攻击次数2 = 1
    CD = 13.5
    攻击倍率 = 1.11
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 2 * 2 * 0.62 * 1.16
            self.攻击次数2 = 1
        elif x == 1:
            self.攻击次数1 = 2 * 2 * (0.62 * 1.3)
            self.攻击次数2 *= 1.26

class 技能10(主动技能):
    名称 = '影戮'
    所在等级 = 40
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1634, 1803, 1963, 2131, 2299, 2466, 2627, 2794, 2961, 3125, 3292, 3457, 3626, 3788, 3954, 4121, 4287,4450, 4617, 4784, 4948, 5115, 5283, 5450, 5611, 5777, 5944, 6112, 6273, 6440, 6607, 6775, 6938, 7106, 7273, 7434, 7600, 7767, 7935, 8096, 8263, 8431, 8598, 8759, 8929, 9096, 9257, 9423, 9591, 9758, 9921, 10088, 10254,10421, 10582, 10751, 10918, 11080, 11246, 11415, 11581, 11745, 11911, 12078, 12247, 12408, 12574, 12741,12903, 13069]
    攻击次数1 = 4
    数据2 = [0, 5872, 6471, 7065, 7662, 8257, 8854, 9448, 10046, 10642, 11235, 11832, 12428, 13027, 13620, 14217, 14814,15406, 16002, 16601, 17195, 17792, 18387, 18984, 19578, 20176, 20773, 21370, 21962, 22558, 23157, 23751,24347, 24944, 25536, 26134, 26730, 27327, 27922, 28518, 29114, 29708, 30305, 30903, 31500, 32092, 32688,33286, 33879, 34477, 35074, 35670, 36264, 36860, 37456, 38052, 38648, 39244, 39840, 40435, 41031, 41630,42224, 42821, 43416, 44012, 44608, 45204, 45800, 46394, 46991]
    攻击次数2 = 1
    CD = 22.5
    攻击倍率 = 1.11
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率  * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = (4 + 3) * 0.74 * 1.13
            self.攻击次数2 = 1
        elif x == 1:
            self.攻击次数1 = (4 + 3) * 0.74 * 1.26
            self.攻击次数2 = 1

class 技能11(主动技能):
    名称 = '瞬杀'
    所在等级 = 45
    等级上限 = 60
    学习间隔 = 2
    等级精通 = 50
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 20129, 22172, 24214, 26257, 28301, 30341, 32386, 34426, 36470, 38510, 40555, 42598, 44638, 46680, 48722,50765, 52807, 54850, 56892, 58931, 60975, 63018, 65060, 67105, 69145, 71186, 73230, 75271, 77314, 79356,81401, 83440, 85485, 87526, 89569, 91612, 93654, 95696, 97735, 99779, 101821, 103863, 105907, 107950, 109989,112033, 114075, 116118, 118160, 120204, 122243, 124290, 126330, 128371, 130416, 132457, 134496, 136539,138584, 140626, 142668, 144712, 146754, 148794, 150836, 152878, 154920, 156964, 159004, 161047]
    攻击次数 = 1
    CD = 40.5
    攻击倍率 = 1.176
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * self.攻击次数 * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.2
        elif x == 1:
            self.倍率 *= 1.2 + 0.09


class 技能12(被动技能):
    名称 = '暗杀之心'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 20:
                return round(1.03 + 0.02 * self.等级, 5)
            else:
                return round(1.43 + 0.021 * (self.等级 - 20), 5)

class 技能13(主动技能):
    名称 = '影斩·乱舞'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    数据1 = [0, 1248, 1536, 1826, 2114, 2404, 2693, 2983, 3273, 3561, 3850, 4139, 4429, 4719, 5008, 5297, 5585, 5875, 6165,6454, 6744, 7032, 7321, 7610, 7900, 8190, 8479, 8768, 9056, 9346, 9636, 9925, 10215, 10503, 10792, 11082,11371, 11661, 11951, 12239, 12527, 12817, 13107, 13396, 13686, 13975, 14264, 14553, 14842, 15132, 15422,15710, 16000, 16288, 16578, 16868, 17157, 17446, 17735, 18025, 18313, 18603, 18893, 19181, 19471, 19761,20049, 20339, 20628, 20917, 21206]
    攻击次数1 = 21
    数据2 = [0, 19603, 24148, 28693, 33239, 37786, 42330, 46877, 51421, 55968, 60514, 65059, 69605, 74150, 78696, 83242,87787, 92332, 96879, 101424, 105969, 110515, 115061, 119606, 124152, 128697, 133243, 137790, 142334, 146881,151427, 155972, 160518, 165063, 169609, 174155, 178700, 183245, 187792, 192337, 196882, 201428, 205973,210519, 215065, 219610, 224156, 228702, 233247, 237794, 242338, 246885, 251431, 255976, 260520, 265068,269613, 274158, 278704, 283250, 287795, 292341, 296886, 301432, 305978, 310523, 315069, 319615, 324160,328706, 333251]
    攻击次数2 = 1
    攻击倍率2 = 1.1
    攻击倍率 = 1.14
    CD = 130.5

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能14(主动技能):
    名称 = '绝命飞刃'
    所在等级 = 60
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 1172, 1291, 1409, 1530, 1648, 1768, 1885, 2003, 2123, 2243, 2360, 2480, 2598, 2717, 2835, 2955, 3077, 3193,3314, 3430, 3551, 3669, 3788, 3906, 4026, 4144, 4264, 4383, 4501, 4621, 4741, 4858, 4977, 5097, 5214, 5335,5451, 5571, 5691, 5809, 5928, 6047, 6166, 6286, 6404, 6522, 6642, 6761, 6880, 6998, 7115, 7236, 7355, 7473,7592, 7712, 7831, 7949, 8067, 8190, 8306, 8423, 8543, 8664, 8783, 8902, 9020, 9139, 9257, 9377]
    攻击次数1 = 1
    数据2 = [0, 4689, 5165, 5638, 6116, 6589, 7067, 7542, 8017, 8492, 8967, 9443, 9918, 10395, 10872, 11348, 11823, 12298,12773, 13248, 13723, 14200, 14676, 15151, 15626, 16101, 16578, 17054, 17529, 18006, 18482, 18956, 19432,19907, 20382, 20860, 21334, 21812, 22285, 22760, 23236, 23712, 24187, 24663, 25138, 25617, 26090, 26566,27041, 27518, 27993, 28468, 28943, 29419, 29894, 30370, 30846, 31322, 31799, 32272, 32750, 33225, 33700,34175, 34652, 35127, 35602, 36077, 36552, 37030, 37505]
    攻击次数2 = 1
    数据3 = [0, 9377, 10327, 11279, 12229, 13181, 14133, 15083, 16033, 16985, 17937, 18886, 19840, 20791, 21742, 22692,23645, 24595, 25548, 26498, 27450, 28400, 29350, 30301, 31254, 32206, 33154, 34106, 35060, 36010, 36960,37913, 38862, 39816, 40766, 41718, 42668, 43618, 44571, 45523, 46474, 47424, 48375, 49325, 50278, 51230,52182, 53130, 54083, 55035, 55987, 56936, 57887, 58839, 59789, 60742, 61692, 62645, 63595, 64546, 65498, 66452, 67399, 68352, 69302, 70252, 71205, 72157, 73107, 74057, 75010]
    攻击次数3 = 1
    CD = 27.0
    攻击倍率 = 1.233
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数3 = 1 * 1.44
        elif x == 1:
            self.攻击次数3 = 1 * (1.44 + 0.14)

class 技能15(主动技能):
    名称 = '八荒影杀'
    所在等级 = 70
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 2301, 2535, 2769, 3004, 3237, 3471, 3703, 3938, 4172, 4406, 4638, 4869, 5105, 5338, 5574, 5805, 6038,6273, 6507, 6741, 6973, 7206, 7440, 7674, 7909, 8141, 8376, 8608, 8843, 9077, 9309, 9542, 9777, 10009, 10246,10478, 10712, 10945, 11179, 11412, 11643, 11878, 12112, 12346, 12579, 12812, 13048, 13281, 13514, 13748,13980, 14214, 14448, 14683, 14914, 15149, 15382, 15617, 15850, 16085, 16315, 16550, 16783, 17018, 17250,17484, 17719, 17952, 18187, 18420]
    攻击次数1 = 1
    数据2 = [0, 2301, 2535, 2769, 3004, 3237, 3471, 3703, 3938, 4172, 4406, 4638, 4869, 5105, 5338, 5574, 5805, 6038,6273, 6507, 6741, 6973, 7206, 7440, 7674, 7909, 8141, 8376, 8608, 8843, 9077, 9309, 9542, 9777, 10009, 10246,10478, 10712, 10945, 11179, 11412, 11643, 11878, 12112, 12346, 12579, 12812, 13048, 13281, 13514, 13748,13980, 14214, 14448, 14683, 14914, 15149, 15382, 15617, 15850, 16085, 16315, 16550, 16783, 17018, 17250,17484, 17719, 17952, 18187, 18420]
    攻击次数2 = 8
    数据3 = [0, 9209, 10143, 11079, 12010, 12946, 13882, 14814, 15749, 16683, 17618, 18553, 19485, 20421, 21354, 22287,23224, 24157, 25091, 26026, 26959, 27895, 28828, 29763, 30697, 31634, 32566, 33501, 34435, 35368, 36304,37240, 38172, 39107, 40039, 40975, 41911, 42842, 43778, 44711, 45646, 46580, 47514, 48450, 49383, 50318,51253, 52184, 53120, 54054, 54988, 55923, 56857, 57791, 58724, 59660, 60595, 61528, 62463, 63397, 64333,65266, 66201, 67135, 68066, 69002, 69938, 70872, 71805, 72739, 73673]
    攻击次数3 = 1
    CD = 45.0
    攻击倍率 = 1.11
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 + self.数据3[self.等级] * self.攻击次数3) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['魔界', '圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数1 = 1 * 2.46
            self.攻击次数2 = (8 - 1) * 1.476  # bug
            self.攻击次数3 = 1 * 1.23
        elif x == 1:
            self.攻击次数1 = 1 * (2.46 + 0.15)
            self.攻击次数2 = (8 - 1) * (1.23 + 0.09) * 1.2 # 1.2为bug加成
            self.攻击次数3 = 1 * (1.23 + 0.09)


class 技能16(主动技能):
    名称 = '死亡连舞（不可抓取）'
    所在等级 = 75
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据1 = [0, 2607, 2870, 3136, 3398, 3663, 3927, 4191, 4457, 4720, 4986, 5250, 5514, 5777, 6042, 6306, 6570, 6837,7099, 7367, 7627, 7892, 8156, 8423, 8687, 8952, 9217, 9480, 9743, 10008, 10273, 10537, 10802, 11065, 11331,11593, 11859, 12122, 12388, 12651, 12916, 13180, 13444, 13708, 13973, 14240, 14501, 14768, 15030, 15298,15559, 15825, 16089, 16353, 16616, 16882, 17147, 17410, 17676, 17939, 18203, 18468, 18732, 18997, 19261,19526, 19789, 20053, 20318, 20583, 20847]
    攻击次数1 = 3
    数据2 = [0, 30888, 34025, 37156, 40290, 43422, 46556, 49692, 52824, 55957, 59094, 62230, 65360, 68495, 71627, 74761,77898, 81029, 84164, 87294, 90429, 93561, 96696, 99826, 102967, 106098, 109234, 112364, 115500, 118634,121765, 124902, 128035, 131168, 134300, 137434, 140568, 143699, 146833, 149969, 153107, 156241, 159373,162506, 165638, 168773, 171908, 175039, 178175, 181304, 184441, 187572, 190706, 193842, 196978, 200114,203246, 206379, 209510, 212646, 215779, 218912, 222047, 225181, 228314, 231444, 234579, 237714, 240846,243983, 247120]
    攻击次数2 = 1
    CD = 36.0
    攻击倍率 = 1.133
    是否有护石 = 1
    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率  * self.攻击倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.攻击次数2 *= (1.2 + 0.2)
            self.CD *= 0.9

class 技能17(被动技能):
    名称 = '潜行暗杀'
    所在等级 = 75
    等级上限 = 20
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能18(主动技能):
    名称 = '剜心'
    所在等级 = 80
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔) + 1, 等级精通)
    数据 = [0, 67876, 74761, 81648, 88531, 95418, 102305, 109193, 116078, 122961, 129850, 136735, 143622, 150510, 157396,164279, 171168, 178051, 184939, 191825, 198710, 205596, 212481, 219369, 226256, 233138, 240025, 246912,253797, 260685, 267571, 274455, 281341, 288227, 295114, 301999, 308887, 315772, 322659, 329546, 336433,343317, 350203, 357089, 363975, 370859, 377745, 384632, 391517, 398405, 405291, 412175, 419063, 425949,432837, 439724, 446605, 453492, 460379, 467266, 474153, 481036, 487921, 494809, 501695, 508581, 515466,522352, 529237, 536127, 543011]
    CD = 40.5
    攻击倍率 = 1.11
    是否有护石 = 1

    def 等效百分比(self, 武器类型):
        return self.数据[self.等级] * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

    护石选项 = ['圣痕']
    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.24

class 技能19(主动技能):
    名称 = '锁链'
    所在等级 = 85
    等级上限 = 1
    #学习间隔 = 5
    #等级精通 = 30
    基础等级 = 1
    数据1 = [0, 2671, 2942, 3213, 3484, 3756, 4027, 4298, 4569, 4840, 5111, 5382, 5653, 5924, 6195, 6466, 6737, 7008,7279, 7550, 7821, 8092, 8363, 8634, 8906, 9177, 9448, 9719, 9990, 10261, 10532, 10803, 11074, 11345, 11616,11887, 12158, 12429, 12700, 12971, 13242, 13513, 13784, 14056, 14327, 14598, 14869, 15140, 15411, 15682,15953, 16224, 16495, 16766, 17037, 17308, 17579, 17850, 18121, 18392, 18663, 18934, 19206, 19477, 19748,20019, 20290, 20561, 20832, 21103, 21374]
    攻击次数1 = 1
    数据2 = [0, 10686, 11770, 12854, 13938, 15022, 16106, 17190, 18274, 19359, 20443, 21527, 22611, 23695, 24779, 25863,26947, 28031, 29116, 30200, 31284, 32368, 33452, 34536, 35620, 36704, 37788, 38873, 39957, 41041, 42125,43209, 44293, 45377, 46461, 47545, 48629, 49714, 50798, 51882, 52966, 54050, 55134, 56218, 57302, 58386,59471, 60555, 61639, 62723, 63807, 64891, 65975, 67059, 68143, 69228, 70312, 71396, 72480, 73564, 74648,75732, 76816, 77900, 78985, 80069, 81153, 82237, 83321, 84405, 85489]
    攻击次数2 = 1
    攻击倍率 = 1.057
    CD = 1

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2) * (1 + self.TP成长 * self.TP等级) * self.倍率 * self.攻击倍率

class 技能20(主动技能):
    名称 = '幽冥链狱：索命'
    备注 = '(不可抓取)'
    所在等级 = 85
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    数据1 = [0, 2671, 2942, 3213, 3484, 3756, 4027, 4298, 4569, 4840, 5111, 5382, 5653, 5924, 6195, 6466, 6737, 7008,7279, 7550, 7821, 8092, 8363, 8634, 8906, 9177, 9448, 9719, 9990, 10261, 10532, 10803, 11074, 11345, 11616,11887, 12158, 12429, 12700, 12971, 13242, 13513, 13784, 14056, 14327, 14598, 14869, 15140, 15411, 15682,15953, 16224, 16495, 16766, 17037, 17308, 17579, 17850, 18121, 18392, 18663, 18934, 19206, 19477, 19748,20019, 20290, 20561, 20832, 21103, 21374]
    攻击次数1 = 1
    攻击倍率1 = 1.057
    #数据2 = [0, 10686, 11770, 12854, 13938, 15022, 16106, 17190, 18274, 19359, 20443, 21527, 22611, 23695, 24779, 25863,26947, 28031, 29116, 30200, 31284, 32368, 33452, 34536, 35620, 36704, 37788, 38873, 39957, 41041, 42125,43209, 44293, 45377, 46461, 47545, 48629, 49714, 50798, 51882, 52966, 54050, 55134, 56218, 57302, 58386,59471, 60555, 61639, 62723, 63807, 64891, 65975, 67059, 68143, 69228, 70312, 71396, 72480, 73564, 74648,75732, 76816, 77900, 78985, 80069, 81153, 82237, 83321, 84405, 85489]
    #攻击次数2 = 1
    数据2 = [0, 91534, 112758, 133985, 155208, 176433, 197658, 218887, 240110, 261334, 282560, 303786, 325014, 346236,367460, 388689, 409912, 431135, 452358, 473589, 494812, 516038, 537263, 558487, 579712, 600937, 622166,643391, 664614, 685840, 707065, 728289, 749517, 770740, 791968, 813191, 834416, 855643, 876867, 898092,919319, 940543, 961765, 982990, 1004218, 1025445, 1046668, 1067894, 1089118, 1110343, 1131571, 1152795,1174021, 1195245, 1216471, 1237696, 1258920, 1280146, 1301373, 1322596, 1343823, 1365046, 1386274, 1407498,1428722, 1449949, 1471175, 1492395, 1513625, 1534851, 1556076]
    攻击次数2 = 1
    攻击倍率2 = 1.191
    CD = 162

    def 等效百分比(self, 武器类型):
        return (self.数据1[self.等级] * self.攻击次数1 * self.攻击倍率1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率2) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能21(被动技能):
    名称 = '暗影禁忌'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 3
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 技能22(主动技能):
    名称 = '影缚追魂锁'
    所在等级 = 95
    等级上限 = 40
    学习间隔 = 2
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 5338.2
    成长 = 602.8
    攻击次数 = 4
    基础2 = 85426.2
    成长2 = 9644.8
    攻击次数2 = 1
    CD = 54.0

    #def 等效百分比(self, 武器类型):
        #return (self.数据1[self.等级] * self.攻击次数1 + self.数据2[self.等级] * self.攻击次数2 * self.攻击倍率) * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能23(主动技能):
    名称 = '无间影狱·噬灭'
    所在等级 = 100
    等级上限 = 40
    学习间隔 = 5
    等级精通 = 30
    基础等级 = min(int((等级 - 所在等级) / 学习间隔 + 1), 等级精通)
    基础 = 8030
    成长 = 2424
    攻击次数 = 3
    基础2 = 48180 + 96361 
    成长2 = 14544.9 + 29090
    攻击次数2 = 1
    基础3 = 24089.45
    成长3 = 7272.55
    攻击次数3 = 3
    CD = 261.0

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
    实际名称 = '隐夜·影舞者'
    角色 = '暗夜使者'
    职业 = '影舞者'

    武器选项 = ['匕首']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '皮甲'
    防具精通属性 = ['力量']

    主BUFF = 2.03

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[8].等级 = self.技能栏[9].等级
        self.技能栏[8].TP等级 = self.技能栏[9].TP等级
        self.技能栏[19].等级 = self.技能栏[20].等级
      
class 隐夜·影舞者(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 职业属性()
        self.角色属性A = 职业属性()
        self.角色属性B = 职业属性()
        self.一觉序号 = 一觉序号
        self.二觉序号 = 二觉序号
        self.三觉序号 = 三觉序号
        self.护石选项 = deepcopy(护石选项)
        self.符文选项 = deepcopy(符文选项)