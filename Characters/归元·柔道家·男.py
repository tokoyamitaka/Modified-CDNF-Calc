from PublicReference.carry.base import *

# 武器选择
# class 主动技能(主动技能):
#     def 等效CD(self, 武器类型):
#         if 武器类型 == '臂铠':
#             return round(self.CD / self.恢复 * 1.1, 1)
#         if 武器类型 == '手套':
#             return round(self.CD / self.恢复 * 0.9, 1)
#         if 武器类型 == '东方棍':
#             return round(self.CD / self.恢复 * 1, 1)
#         if 武器类型 == '爪':
#             return round(self.CD / self.恢复 * 1, 1)

# class Buff技能(主动技能):
#	名称="暴力抓取"
#	所在等级=15
#	等级上限=20
#	基础等级=10
#	def 加成倍率(self):
#        if self.等级==0:
#            return 1.0
#        else:
#            return round(2.08,5)

class 职业主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    data0 = []
    data1 = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []

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
        if len(self.data4) >= self.等级 and len(self.data4) > 0:
            等效倍率 += self.data4[self.等级] * self.攻击次数5
        if len(self.data5) >= self.等级 and len(self.data5) > 0:
            等效倍率 += self.data5[self.等级] * self.攻击次数6
        if len(self.data6) >= self.等级 and len(self.data6) > 0:
            等效倍率 += self.data6[self.等级] * self.攻击次数7
        return 等效倍率 * (1 + self.TP成长 * self.TP等级) * self.倍率

class 技能0(职业主动技能):
    名称 = '膝击'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 50
    data0 = [int(i*1.22) for i in [0, 188, 207, 227, 246, 265, 284, 303, 322, 341, 361, 380, 399, 418, 437, 456, 475, 495, 514, 533, 552, 571, 590, 609, 629, 648, 667, 686, 705, 724, 743, 763, 782, 801, 820, 839, 858, 878, 897, 916, 935, 954, 973, 992, 1012, 1031, 1050, 1069, 1088, 1107, 1126, 1146, 1165, 1184, 1203, 1222, 1241, 1260, 1280, 1299, 1318, 1337, 1356, 1375, 1394, 1414, 1433, 1452, 1471, 1490, 1509]]
    攻击次数 = 2
    data1 = [int(i*1.22) for i in [0, 1063, 1171, 1278, 1386, 1494, 1602, 1710, 1818, 1926, 2034, 2141, 2249, 2357, 2465, 2573, 2681, 2789, 2896, 3004, 3112, 3220, 3328, 3436, 3544, 3652, 3759, 3867, 3975, 4083, 4191, 4299, 4407, 4514, 4622, 4730, 4838, 4946, 5054, 5162, 5270, 5377, 5485, 5593, 5701, 5809, 5917, 6025, 6132, 6240, 6348, 6456, 6564, 6672, 6780, 6887, 6995, 7103, 7211, 7319, 7427, 7535, 7643, 7750, 7858, 7966, 8074, 8182, 8290, 8398, 8505]]
    攻击次数2 = 1
    #冲击波 = 858.9387755
    #冲击波成长 = 97.06122449
    CD = 5.0
    TP成长 = 0.08
    TP上限 = 5


class 技能1(被动技能):
    名称 = '摔技强化'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.0 + 0.02 * self.等级, 5)


class 技能2(被动技能):
    名称 = '臂铠精通'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    关联技能 = ['无']
    冷却关联技能 = ['膝击', '抛投', '野蛮冲撞', '无情摔击', '空绞锤', '霹雳旋踢', '浮空凌云踢',
              '疾波猛坠', '地狱风火轮', '裂石破天', '彗星冲击', '武莲华', '黑震旋风', '疾风闪电', '黑震流·陨灭']

    def CD缩减倍率(self, 武器类型):
        if 武器类型 == '臂铠':
            return 0.9
        else:
            return 1.0


class 技能3(职业主动技能):
    名称 = '抛投'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 46
    data0 = [int(i*1.22) for i in [0, 871, 960, 1048, 1137, 1225, 1314, 1402, 1490, 1579, 1667, 1756, 1844, 1933, 2021, 2110, 2198, 2286, 2375, 2463, 2552, 2640, 2729, 2817, 2906, 2994, 3082, 3171, 3259, 3348, 3436, 3525, 3613, 3702, 3790, 3878, 3967, 4055, 4144, 4232, 4321, 4409, 4498, 4586, 4674, 4763, 4851, 4940, 5028, 5117, 5205, 5294, 5382, 5470, 5559, 5647, 5736, 5824, 5913, 6001, 6090, 6178, 6266, 6355, 6443, 6532, 6620, 6709, 6797, 6886, 6974]]
    攻击次数 = 1
    data1 = [int(i*1.22) for i in [0, 1374, 1513, 1653, 1792, 1932, 2071, 2211, 2350, 2490, 2628, 2769, 2907, 3048, 3186, 3326, 3465, 3605, 3744, 3884, 4023, 4163, 4302, 4442, 4581, 4721, 4860, 5000, 5139, 5279, 5418, 5558, 5697, 5837, 5976, 6116, 6254, 6395, 6533, 6674, 6812, 6952, 7091, 7231, 7370, 7510, 7649, 7788, 7928, 8067, 8207, 8346, 8486, 8625, 8765, 8904, 9044, 9182, 9323, 9461, 9602, 9740, 9880, 10019, 10159, 10298, 10438, 10577, 10717, 10856, 10996]]
    攻击次数2 = 1
    # 基础 = 782.5555556 + 1234.555556
    # 成长 = 88.44444444 + 139.4444444
    #冲击波 = 1234.555556
    #冲击波成长 = 139.4444444
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class 技能4(被动技能):
    名称 = '连环抓取'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            # 默认高阶
            return round(1.36 + 0.02 * self.等级, 5)


class 技能5(职业主动技能):
    名称 = '野蛮冲撞'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    data0 = [int(i*1.227) for i in [0, 2186, 2408, 2629, 2851, 3073, 3295, 3517, 3738, 3960, 4182, 4404, 4626, 4847, 5069, 5291, 5513, 5735, 5956, 6178, 6400, 6622, 6844, 7065, 7287, 7509, 7731, 7953, 8174, 8396, 8618, 8840, 9062, 9283, 9505, 9727, 9949, 10171, 10392, 10614, 10836, 11058, 11280, 11501, 11723, 11945, 12167, 12389, 12610, 12832, 13054, 13276, 13498, 13719, 13941, 14163, 14385, 14607, 14828, 15050, 15272, 15494, 15716, 15937, 16159, 16381, 16603, 16825, 17046, 17268, 17490]]
    攻击次数 = 1
    data1 = [int(i*1.227) for i in [0, 1311, 1444, 1577, 1711, 1844, 1977, 2110, 2243, 2376, 2509, 2642, 2775, 2908, 3041, 3174, 3307, 3441, 3574, 3707, 3840, 3973, 4106, 4239, 4372, 4505, 4638, 4771, 4904, 5038, 5171, 5304, 5437, 5570, 5703, 5836, 5969, 6102, 6235, 6368, 6501, 6634, 6768, 6901, 7034, 7167, 7300, 7433, 7566, 7699, 7832, 7965, 8098, 8231, 8365, 8498, 8631, 8764, 8897, 9030, 9163, 9296, 9429, 9562, 9695, 9828, 9961, 10095, 10228, 10361, 10494]]
    攻击次数2 = 1
    # 基础 = 1964.2 + 1177.925
    # 成长 = 221.8 + 133.075
    #冲击波 = 1177.925
    #冲击波成长 = 133.075
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5


class 技能6(职业主动技能):
    名称 = '无情摔击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    # 基础 = 2996.6
    # 成长 = 338.4
    data0 = [int(i*1.22) for i in [0, 3335, 3673, 4012, 4350, 4689, 5027, 5365, 5704, 6042, 6381, 6719, 7057, 7396, 7734, 8073, 8411, 8749, 9088, 9426, 9764, 10103, 10441, 10780, 11118, 11456, 11795, 12133, 12472, 12810, 13148, 13487, 13825, 14164, 14502, 14840, 15179, 15517, 15855, 16194, 16532, 16871, 17209, 17547, 17886, 18224, 18563, 18901, 19239, 19578, 19916, 20255, 20593, 20931, 21270, 21608, 21947, 22285, 22623, 22962, 23300, 23638, 23977, 24315, 24654, 24992, 25330, 25669, 26007, 26346, 26684]]
    #冲击波 = 2996.6
    #冲击波成长 = 338.4
    CD = 8.0
    TP成长 = 0.10
    TP上限 = 5


class 技能7(职业主动技能):
    名称 = '空绞锤'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    data0 = [int(i*1.22) for i in [0, 3061, 3371, 3682, 3992, 4303, 4613, 4924, 5234, 5545, 5855, 6166, 6476, 6787, 7098, 7408, 7719, 8029, 8340, 8650, 8961, 9271, 9582, 9892, 10203, 10513, 10824, 11135, 11445, 11756, 12066, 12377, 12687, 12998, 13308, 13619, 13929, 14240, 14551, 14861, 15172, 15482, 15793, 16103, 16414, 16724, 17035, 17345, 17656, 17966, 18277, 18588, 18898, 19209, 19519, 19830, 20140, 20451, 20761, 21072, 21382, 21693, 22003, 22314, 22625, 22935, 23246, 23556, 23867, 24177, 24488]]
    #    data1 = [0, 2754, 3034, 3313, 3593, 3872, 4152, 4431, 4711, 4990, 5270, 5549, 5829, 6108, 6388, 6667, 6947, 7226, 7506, 7785, 8065, 8344, 8624, 8903, 9183, 9462, 9742, 10021, 10301, 10580, 10860, 11139, 11418, 11698, 11977, 12257, 12536, 12816, 13095, 13375, 13654, 13934, 14213, 14493, 14772, 15052, 15331, 15611, 15890, 16170, 16449, 16729, 17008, 17288, 17567, 17847, 18126, 18406, 18685, 18965, 19244, 19524, 19803, 20083, 20362, 20642, 20921, 21200, 21480, 21759, 22039]
    #冲击波 = 2474.513514
    #冲击波成长 = 279.4864865
    CD = 7.0
    TP成长 = 0.10
    TP上限 = 5


class 技能8(职业主动技能):
    名称 = '霹雳旋踢'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    # 基础 = 4019.216216
    # 成长 = 453.7837838
    data0 = [int(i*1.192) for i in [0, 4473, 4927, 5380, 5834, 6288, 6742, 7196, 7649, 8104, 8557, 9011, 9464, 9918, 10373, 10826, 11280, 11733, 12188, 12641, 13095, 13549, 14002, 14457, 14910, 15364, 15818, 16272, 16726, 17179, 17633, 18086, 18541, 18995, 19448, 19902, 20356, 20810, 21263, 21717, 22171, 22625, 23079, 23532, 23986, 24440, 24894, 25348, 25801, 26255, 26709, 27163, 27617, 28070, 28525, 28978, 29432, 29885, 30340, 30794, 31247, 31701, 32154, 32609, 33062, 33516, 33970, 34424, 34878, 35331, 35785]]
    #冲击波 = 3617.594595
    #冲击波成长 = 408.4054054
    CD = 12.0
    TP成长 = 0.10
    TP上限 = 5


class 技能9(职业主动技能):
    名称 = '浮空凌云踢'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(i*1.22) for i in [0, 1516, 1670, 1824, 1978, 2131, 2285, 2439, 2593, 2747, 2901, 3054, 3208, 3362, 3516, 3670, 3824, 3978, 4131, 4285, 4439, 4593, 4747, 4901, 5054, 5208, 5362, 5516, 5670, 5824, 5977, 6131, 6285, 6439, 6593, 6747, 6901, 7054, 7208, 7362, 7516, 7670, 7824, 7977, 8131, 8285, 8439, 8593, 8747, 8901, 9054, 9208, 9362, 9516, 9670, 9824, 9977, 10131, 10285, 10439, 10593, 10747, 10901, 11054, 11208, 11362, 11516, 11670, 11824, 11977, 12131]]
    攻击次数 = 1
    data1 = [int(i*1.22) for i in [0, 2729, 3006, 3283, 3560, 3837, 4114, 4391, 4668, 4945, 5221, 5498, 5775, 6052, 6329, 6606, 6883, 7160, 7437, 7714, 7991, 8268, 8545, 8821, 9098, 9375, 9652, 9929, 10206, 10483, 10760, 11037, 11314, 11591, 11868, 12144, 12421, 12698, 12975, 13252, 13529, 13806, 14083, 14360, 14637, 14914, 15191, 15468, 15744, 16021, 16298, 16575, 16852, 17129, 17406, 17683, 17960, 18237, 18514, 18791, 19068, 19344, 19621, 19898, 20175, 20452, 20729, 21006, 21283, 21560, 21837]]
    攻击次数2 = 1
    data2 = [int(i*1.22) for i in [0, 1819, 2004, 2189, 2373, 2558, 2742, 2927, 3112, 3296, 3481, 3665, 3850, 4035, 4219, 4404, 4588, 4773, 4958, 5142, 5327, 5512, 5696, 5881, 6065, 6250, 6435, 6619, 6804, 6988, 7173, 7358, 7542, 7727, 7912, 8096, 8281, 8465, 8650, 8835, 9019, 9204, 9388, 9573, 9758, 9942, 10127, 10312, 10496, 10681, 10865, 11050, 11235, 11419, 11604, 11788, 11973, 12158, 12342, 12527, 12712, 12896, 13081, 13265, 13450, 13635, 13819, 14004, 14188, 14373, 14558]]
    攻击次数3 = 1
    # 基础 = 1362.142857 + 2452.085714 + 1634.371429
    # 成长 = 153.8571429 + 276.9142857 + 184.6285714
    #冲击波 = 2860.914286
    #冲击波成长 = 323.0857143
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5


class 技能10(职业主动技能):
    名称 = '疾波猛坠'
    备注 = '空中释放'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    data0 = [int(i*1.294) for i in [0, 3407, 3752, 4098, 4443, 4790, 5136, 5481, 5827, 6172, 6517, 6863, 7209, 7555, 7901, 8247, 8591, 8937, 9283, 9628, 9974, 10320, 10666, 11012, 11357, 11704, 12048, 12393, 12740, 13085, 13431, 13776, 14123, 14469, 14814, 15159, 15504, 15850, 16197, 16542, 16888, 17233, 17580, 17925, 18269, 18616, 18961, 19307, 19653, 19999, 20345, 20690, 21036, 21382, 21726, 22073, 22418, 22764, 23110, 23456, 23801]]
    data1 = [int(i*1.294) for i in [0, 429, 474, 517, 561, 603, 648, 691, 735, 778, 822, 865, 908, 954, 996, 1038, 1085, 1128, 1170, 1215, 1257, 1302, 1345, 1388, 1432, 1476, 1519, 1562, 1605, 1650, 1693, 1737, 1782, 1824, 1869, 1912, 1955, 1999, 2042, 2086, 2130, 2172, 2216, 2259, 2304, 2348, 2391, 2436, 2478, 2522, 2566, 2609, 2653, 2696, 2738, 2784, 2826, 2870, 2915, 2958, 3002]]
    攻击次数2 = 6

    # 踢击 = 3061.371429
    # 踢击成长 = 345.6285714
    # 冲击波 = 385.4
    # 冲击波成长 = 43.6
    # 冲击波次数 = 6
    # 基础 = 踢击 + 冲击波 * 冲击波次数
    # 成长 = 踢击成长 + 冲击波成长 * 冲击波次数
    CD = 15.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):  # 默认空中释放
        if x == 0:
            self.倍率 *= 1.3
            # self.踢击 *= 0
            # self.踢击成长 *= 0
            # self.冲击波 *= 2.18
            # self.冲击波成长 *= 2.18
            # self.冲击波次数 += 1
        elif x == 1:
            self.倍率 *= 1.39
            # self.踢击 *= 0
            # self.踢击成长 *= 0
            # self.冲击波 *= 2.36
            # self.冲击波成长 *= 2.36
            # self.冲击波次数 += 1


class 技能11(职业主动技能):
    名称 = '地狱风火轮'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    data0 = [int(i*1.22) for i in [0, 2055, 2263, 2472, 2680, 2889, 3097, 3306, 3514, 3723, 3931, 4140, 4348, 4557, 4765, 4974, 5182, 5391, 5599, 5808, 6016, 6225, 6433, 6642, 6850, 7059, 7267, 7476, 7684, 7893, 8101, 8310, 8518, 8726, 8935, 9143, 9352, 9560, 9769, 9977, 10186, 10394, 10603, 10811, 11020, 11228, 11437, 11645, 11854, 12062, 12271, 12479, 12688, 12896, 13105, 13313, 13522, 13730, 13939, 14147, 14356, 14564, 14773, 14981, 15190, 15398, 15607, 15815, 16024, 16232, 16441]]
    攻击次数 = 1
    data1 = [int(i*1.22) for i in [0, 1214, 1337, 1460, 1584, 1707, 1830, 1953, 2076, 2200, 2323, 2446, 2569, 2692, 2816, 2939, 3062, 3185, 3308, 3432, 3555, 3678, 3801, 3924, 4048, 4171, 4294, 4417, 4540, 4664, 4787, 4910, 5033, 5156, 5280, 5403, 5526, 5649, 5772, 5896, 6019, 6142, 6265, 6388, 6512, 6635, 6758, 6881, 7004, 7128, 7251, 7374, 7497, 7620, 7744, 7867, 7990, 8113, 8236, 8360, 8483, 8606, 8729, 8852, 8976, 9099, 9222, 9345, 9468, 9592, 9715]]
    攻击次数2 = 1
    data2 = [int(i*1.22) for i in [0, 3269, 3601, 3932, 4264, 4596, 4928, 5259, 5591, 5923, 6254, 6586, 6918, 7249, 7581, 7913, 8245, 8576, 8908, 9240, 9571, 9903, 10235, 10566, 10898, 11230, 11561, 11893, 12225, 12557, 12888, 13220, 13552, 13883, 14215, 14547, 14878, 15210, 15542, 15874, 16205, 16537, 16869, 17200, 17532, 17864, 18195, 18527, 18859, 19190, 19522, 19854, 20186, 20517, 20849, 21181, 21512, 21844, 22176, 22507, 22839, 23171, 23503, 23834, 24166, 24498, 24829, 25161, 25493, 25824, 26156]]
    攻击次数3 = 1
    data3 = [int(i*1.22) for i in [0, 2802, 3086, 3371, 3655, 3939, 4224, 4508, 4792, 5076, 5361, 5645, 5929, 6214, 6498, 6782, 7067, 7351, 7635, 7920, 8204, 8488, 8773, 9057, 9341, 9625, 9910, 10194, 10478, 10763, 11047, 11331, 11616, 11900, 12184, 12469, 12753, 13037, 13321, 13606, 13890, 14174, 14459, 14743, 15027, 15312, 15596, 15880, 16165, 16449, 16733, 17018, 17302, 17586, 17870, 18155, 18439, 18723, 19008, 19292, 19576, 19861, 20145, 20429, 20714, 20998, 21282, 21567, 21851, 22135, 22419]]
    攻击次数4 = 1

    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.data2 = [int(x*1.38) for x in self.data2]
            self.data3 = [int(x*1.38) for x in self.data3]
        elif x == 1:
            self.data2 = [int(x*1.52) for x in self.data2]
            self.data3 = [int(x*1.52) for x in self.data3]


class 技能12(职业主动技能):
    名称 = '裂石破天'
    备注 = '不可抓取'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31

    #    data0 = [0, 7526, 8290, 9053, 9817, 10580, 11344, 12108, 12871, 13635, 14398, 15162, 15926, 16689, 17453, 18216, 18980, 19743, 20507, 21271, 22034, 22798, 23561, 24325, 25088, 25852, 26616, 27379, 28143, 28906, 29670, 30433, 31197, 31961, 32724, 33488, 34251, 35015, 35778, 36542, 37306, 38069, 38833, 39596, 40360, 41124, 41887, 42651, 43414, 44178, 44941, 45705, 46469, 47232, 47996, 48759, 49523, 50286, 51050, 51814, 52577, 53341, 54104, 54868, 55631, 56395, 57159, 57922, 58686, 59449, 60213]
    data0 = [int(i*1.208) for i in [0, 4475, 4930, 5383, 5837, 6291, 6746, 7199, 7653, 8107, 8562, 9016, 9469, 9923, 10378, 10832, 11286, 11739, 12194, 12648, 13102, 13556, 14011, 14464, 14918, 15372, 15827, 16281, 16734, 17188, 17643, 18097, 18550, 19004, 19459, 19913, 20367, 20820, 21275, 21729, 22183, 22637, 23092, 23545, 23999, 24453, 24908, 25362, 25815, 26269, 26724, 27178, 27632, 28085, 28540, 28994, 29448, 29901, 30356, 30810, 31264, 31718, 32173, 32626, 33080, 33534, 33989, 34443, 34896, 35350, 35805]]
    攻击次数 = 1
    data1 = [int(i*1.208) for i in [0, 10387, 11440, 12494, 13548, 14602, 15655, 16709, 17763, 18817, 19871, 20924, 21978, 23032, 24086, 25139, 26193, 27247, 28301, 29354, 30408, 31462, 32516, 33570, 34623, 35677, 36731, 37785, 38838, 39892, 40946, 42000, 43053, 44107, 45161, 46215, 47268, 48322, 49376, 50430, 51484, 52537, 53591, 54645, 55699, 56752, 57806, 58860, 59914, 60967, 62021, 63075, 64129, 65183, 66236, 67290, 68344, 69398, 70451, 71505, 72559, 73613, 74666, 75720, 76774, 77828, 78881, 79935, 80989, 82043, 83097]]
    攻击次数2 = 1

    # 基础 = (9799.533333 + 4222.233333)/1.02
    # 成长 = (476.7666667 + 1106.466667)/1.02
    #对可抓取踢击 = 7100.233333
    #对可抓取踢击成长 = 801.7666667
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.20
        elif x == 1:
            self.倍率 *= 1.28


class 技能13(被动技能):
    名称 = '力之奥义'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.025 + 0.02 * self.等级, 5)


class 技能14(职业主动技能):
    名称 = '死亡旋律'
    备注 = '空中释放'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12

    # 基本攻击的物理攻击力：<data0>%
    # data0 = [0, 1805, 2225, 2644, 3062, 3481, 3900, 4318, 4738, 5157, 5575, 5995, 6413, 6831, 7251, 7670, 8088, 8507, 8927, 9345, 9763, 10183, 10601, 11020, 11440, 11858, 12277, 12696, 13114, 13533, 13953, 14371, 14790, 15210, 15628, 16046, 16466, 16884, 17303, 17723, 18141, 18560, 18978, 19397, 19816, 20234, 20654, 21073, 21491, 21911, 22329, 22747, 23167, 23586, 24004, 24424, 24841, 25261, 25680, 26097, 26517, 26937, 27354, 27774, 28194, 28610, 29030, 29450, 29867, 30287, 30706]
    #最终前踢攻击力：<data1>%
    # data1 = [0, 8428, 10383, 12338, 14292, 16247, 18203, 20156, 22112, 24066, 26021, 27975, 29929, 31884, 33838, 35794, 37747, 39703, 41656, 43611, 45566, 47520, 49474, 51430, 53383, 55339, 57294, 59249, 61203, 63157, 65112, 67066, 69022, 70975, 72931, 74885, 76839, 78794, 80749, 82702, 84658, 86613, 88567, 90521, 92476, 94430, 96384, 98340, 100294, 102250, 104204, 106159, 108113, 110069, 112022, 113977, 115932, 117886, 119841, 121795, 123749, 125704, 127659, 129612, 131568, 133522, 135477, 137431, 139387, 141341, 143297]
    # 空中施放时向下猛踢冲击波物理攻击力：<data2>%
    data0 = [int(i*1.22) for i in [0, 34812, 42888, 50958, 59033, 67108, 75180, 83254, 91326, 117515, 127059, 136603, 146145, 155692, 165235, 174782, 184324, 193871, 203414, 212957, 222501, 232047, 241591, 251136, 260681, 270225, 279769, 289313, 298857, 308400, 317947, 327490, 337036, 346578, 356123, 365668, 375212, 384757, 394302, 403843, 413390, 422933, 432479, 442022, 451567, 461111, 470656, 480200, 489744, 499290, 508834, 518378, 527922, 537466, 547009, 556556, 566099, 575646, 585189, 594731, 604276, 613821, 623365, 632911, 642454, 651999, 661541, 671088, 680631, 690176, 699720]]

    # 空中释放基础 = 33191.55
    # 空中释放成长 = 10021.725
    # 基础 = 空中释放基础
    # 成长 = 空中释放成长
    #地面释放基础 = 9716 + 6473.5
    #地面释放基础成长 = 2931.25 + 1954.625
    #地面释放冲击波 = 19899.55
    #地面释放冲击波成长 = 6009.1625
    CD = 145.0

    def 等效百分比(self,武器类型):
        if self.等级 >=6:
            self.data0 = [int(x*1.05) for x in self.data0]
        return super().等效百分比(武器类型)

class 技能15(职业主动技能):
    名称 = '彗星冲击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    data0 = [int(i*1.22) for i in [0, 11815, 13014, 14212, 15411, 16610, 17808, 19007, 20206, 21404, 22603, 23802, 25000, 26199, 27398, 28596, 29795, 30994, 32192, 33391, 34590, 35788, 36987, 38185, 39384, 40583, 41781, 42980, 44179, 45377, 46576, 47775, 48973, 50172, 51371, 52569, 53768, 54967, 56165, 57364, 58563, 59761, 60960, 62159, 63357, 64556, 65755, 66953, 68152, 69351, 70549, 71748, 72947, 74145, 75344, 76543, 77741, 78940, 80139, 81337, 82536, 83735, 84933, 86132, 87331, 88529, 89728, 90927, 92125, 93324, 94523]]
    CD = 25.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.CD *= 0.88
            self.倍率 *= 1
        elif x == 1:
            self.CD *= 0.88
            self.倍率 *= 1.09

class 技能16(职业主动技能):
    名称 = '武莲华'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    data0 = [int(i*1.177) for i in [0, 4868, 5361, 5856, 6349, 6842, 7338, 7831, 8325, 8821, 9314, 9806, 10301, 10794, 11288, 11784, 12276, 12769, 13263, 13759, 14253, 14747, 15241, 15735, 16229, 16722, 17216, 17709, 18203, 18697, 19193, 19687, 20179, 20675, 21166, 21661, 22156, 22649, 23142, 23636, 24130, 24625, 25119, 25613, 26108, 26601, 27094, 27589, 28082, 28576, 29070, 29564, 30056, 30551, 31046, 31541, 32034, 32527, 33023, 33514, 34008, 34503, 34997, 35489, 35984, 36480, 36975, 37467, 37961, 38455, 38949]]
    data1 = [int(i*1.177) for i in [0, 1215, 1334, 1459, 1583, 1705, 1829, 1954, 2074, 2200, 2320, 2444, 2569, 2689, 2812, 2937, 3060, 3181, 3305, 3427, 3551, 3675, 3797, 3921, 4045, 4168, 4289, 4412, 4535, 4660, 4781, 4906, 5029, 5151, 5275, 5399, 5519, 5643, 5769, 5890, 6014, 6140, 6259, 6381, 6507, 6629, 6751, 6875, 6998, 7122, 7245, 7367, 7490, 7613, 7737, 7861, 7984, 8106, 8229, 8351, 8475, 8597, 8721, 8846, 8968, 9088, 9213, 9337, 9459, 9584, 9705]]
    data2 = [int(i*1.177) for i in [0, 7299, 8041, 8781, 9523, 10263, 11003, 11743, 12485, 13226, 13965, 14705, 15447, 16187, 16928, 17668, 18411, 19152, 19891, 20634, 21374, 22116, 22856, 23597, 24336, 25078, 25818, 26559, 27299, 28040, 28780, 29522, 30261, 31003, 31743, 32485, 33224, 33965, 34706, 35446, 36186, 36928, 37667, 38408, 39149, 39889, 40631, 41369, 42111, 42852, 43592, 44333, 45074, 45817, 46557, 47299, 48038, 48779, 49520, 50260, 51001, 51742, 52481, 53222, 53963, 54705, 55445, 56183, 56925, 57666, 58409]]
    攻击次数 = 2
    攻击次数2 = 12
    攻击次数3 = 1
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石选项 = ['魔界', '圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1
            self.data0 = [int(x*1.5) for x in self.data0]
            self.攻击次数 = 4
            self.攻击次数2 = 0
            self.CD *= 0.9
        elif x == 1:
            self.倍率 *= 1.07
            self.data0 = [int(x*1.5) for x in self.data0]
            self.攻击次数 = 4
            self.攻击次数2 = 0
            self.CD *= 0.9


class 技能17(被动技能):
    名称 = '傲天之怒'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.22 + 0.02 * self.等级, 5)


class 技能18(职业主动技能):
    名称 = '黑震旋风'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 5618.6 + 10903.33333 + 14726.33333
    成长 = 3528.699999
    data0 = [int(i*1.22) for i in [0, 6253, 6887, 7522, 8156, 8790, 9425, 10059, 10694, 11328, 11962, 12597, 13231, 13866, 14500, 15134, 15769, 16403, 17038, 17672, 18306, 18941, 19575, 20210, 20844, 21478, 22113, 22747, 23382, 24016, 24650, 25285, 25919, 26554, 27188, 27822, 28457, 29091, 29726, 30360, 30994]]
    data1 = [int(i*1.22) for i in [0, 2427, 2674, 2920, 3166, 3412, 3659, 3905, 4151, 4398, 4644, 4890, 5137, 5383, 5629, 5875, 6122, 6368, 6614, 6861, 7107, 7353, 7599, 7846, 8092, 8338, 8585, 8831, 9077, 9324, 9570, 9816, 10062, 10309, 10555, 10801, 11048, 11294, 11540, 11787, 12033]]
    攻击次数2 = 5
    data2 = [int(i*1.22) for i in [0, 16389, 18051, 19714, 21377, 23039, 24702, 26365, 28027, 29690, 31353, 33015, 34678, 36341, 38003, 39666, 41329, 42993, 44654, 46318, 47981, 49642, 51306, 52969, 54631, 56294, 57957, 59619, 61282, 62945, 64607, 66270, 67933, 69595, 71258, 72921, 74583, 76246, 77909, 79571, 81234]]
    攻击次数3 = 1
    #冲击波 = 14726.33333
    #冲击波成长 = 1662.666667
    CD = 40.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.33


class 技能19(职业主动技能):
    名称 = '疾风闪电'
    备注 = '不可抓取'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    # 对建筑型敌人的物理攻击力：<int>%
    data0 = [int(i*1.21) for i in [0, 22779, 25090, 27403, 29713, 32022, 34334, 36644, 38955, 41268, 43578, 45889, 48200, 50511, 52823, 55134, 57445, 59754, 62066, 64376, 66687, 68999, 71311, 73620, 75933, 78244, 80555, 82864, 85177, 87488, 89797, 92108, 94421, 96730, 99041, 101354, 103664, 105974, 108285, 110598, 112909]]
    # 冲击波对周围无法抓取的敌人的物理攻击力：<int>%
    data1 = [int(i*1.21) for i in [0, 17993, 19817, 21642, 23468, 25293, 27119, 28942, 30768, 32593, 34419, 36245, 38069, 39896, 41721, 43549, 45370, 47199, 49023, 50848, 52672, 54499, 56321, 58149, 59973, 61801, 63623, 65450, 67276, 69100, 70925, 72752, 74577, 76401, 78227, 80054, 81878, 83704, 85529, 87353, 89180]]
    攻击次数2 = 1
    #对可抓取怪物的冲撞 = 10744.66667
    #对可抓取怪物的冲撞成长 = 1213.333333
    #准备释放最后一击 = 7163.166667
    #准备释放最后一击成长 = 808.8333333
    #最后一击 = 17911.91667
    #最后一击成长 = 2022.083333
    CD = 45.0
    是否有护石 = 1
    护石选项 = ['圣痕']

    def 装备护石(self, x):
        if x == 0:
            self.倍率 *= 1.35


class 技能20(职业主动技能):
    名称 = '一字传承：极义震天破'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    data0 = [int(i*1.22) for i in [0, 25794, 31775, 37755, 43738, 49717, 55700, 61681, 67662, 73644, 79625, 85606, 91587, 97568, 103549, 109531, 115511, 121492, 127475, 133454, 139437, 145418, 151399, 157380, 163362, 169342, 175324, 181306, 187286, 193268, 199249, 205230, 211211, 217193, 223173, 229155, 235138, 241117, 247100, 253080, 259061]]
    data1 = [int(i*1.22) for i in [0, 1984, 2442, 2904, 3363, 3824, 4285, 4744, 5206, 5664, 6126, 6585, 7045, 7505, 7965, 8426, 8884, 9345, 9805, 10266, 10726, 11185, 11646, 12105, 12565, 13026, 13486, 13945, 14406, 14867, 15325, 15787, 16246, 16708, 17167, 17627, 18088, 18547, 19007, 19467, 19928]]
    攻击次数2 = 13
    data2 = [int(i*1.22) for i in [0, 47756, 58830, 69906, 80980, 92054, 103127, 114202, 125274, 136348, 147423, 158496, 169570, 180644, 191720, 202793, 213868, 224944, 236016, 247091, 258163, 269239, 280313, 291387, 302463, 313535, 324609, 335682, 346758, 357832, 368905, 379982, 391054, 402128, 413201, 424277, 435351, 446424, 457498, 468570, 479647]]
    攻击次数3 = 1
    # 基础 = 76306.75
    # 成长 = 23035.25
    CD = 185.0


class 技能21(被动技能):
    名称 = '神怡气静'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 技能22(职业主动技能):
    名称 = '黑震流·陨灭'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 6
    data0 = [int(i*1.22) for i in [0, 3799, 4184, 4570, 4955, 5340, 5726, 6111, 6497, 6882, 7268, 7653, 8038, 8424, 8809, 9195, 9580, 9966, 10351, 10736, 11122, 11507, 11893, 12278, 12664, 13049, 13434, 13820, 14205, 14591, 14976, 15362, 15747, 16132, 16518, 16903, 17289, 17674, 18060, 18445, 18830]]
    data1 = [int(i*1.22) for i in [0, 6015, 6625, 7235, 7846, 8456, 9066, 9677, 10287, 10897, 11507, 12118, 12728, 13338, 13948, 14559, 15169, 15779, 16389, 17000, 17610, 18220, 18830, 19441, 20051, 20661, 21271, 21882, 22492, 23102, 23713, 24323, 24933, 25543, 26154, 26764, 27374, 27984, 28595, 29205, 29815]]
    攻击次数2 = 10
    data2 = [int(i*1.22) for i in [0, 12030, 13250, 14470, 15692, 16912, 18132, 19354, 20574, 21794, 23014, 24236, 25456, 26676, 27896, 29118, 30338, 31558, 32778, 34000, 35220, 36440, 37660, 38882, 40102, 41322, 42542, 43764, 44984, 46204, 47426, 48646, 49866, 51086, 52308, 53528, 54748, 55968, 57190, 58410, 59630]]
    攻击次数3 = 1
    基础 = 68271.2
    成长 = 7707.8
    CD = 60.0


class 技能23(职业主动技能):
    名称 = '黑震流·山岳崩颓'
    备注 = '无法抓取'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    # 基础 = 205707
    # 成长 = 62101
    data0 = [int(i*1.209) for i in [0, 40171, 49486, 58801, 68117, 77432, 86747, 96062, 105377, 114692, 124007, 133323, 142638, 151953, 161268, 170583, 179898, 189213, 198529, 207844, 217159, 226474, 235789, 245104, 254420, 263735, 273050, 282365, 291680, 300995, 310310, 319626, 328941, 338256, 347571, 356886, 366201, 375516, 384832, 394147, 403462]]
    data1 = [int(i*1.209) for i in [0, 13390, 16495, 19600, 22705, 25810, 28915, 32020, 35125, 38230, 41335, 44441, 47546, 50651, 53756, 56861, 59966, 63071, 66176, 69281, 72386, 75491, 78596, 81701, 84806, 87911, 91016, 94121, 97226, 100331, 103436, 106542, 109647, 112752, 115857, 118962, 122067, 125172, 128277, 131382, 134487]]
    攻击次数2 = 1
    data2 = [int(i*1.209) for i in [0, 26781, 32991, 39201, 45411, 51621, 57831, 64041, 70251, 76461, 82671, 88882, 95092, 101302, 107512, 113722, 119932, 126142, 132352, 138562, 144772, 150983, 157193, 163403, 169613, 175823, 182033, 188243, 194453, 200663, 206873, 213084, 219294, 225504, 231714, 237924, 244134, 250344, 256554, 262764, 268974]]
    攻击次数3 = 1
    data3 = [int(i*1.209) for i in [0, 53562, 65982, 78402, 90822, 103242, 115663, 128083, 140503, 152923, 165343, 177764, 190184, 202604, 215024, 227444, 239865, 252285, 264705, 277125, 289545, 301966, 314386, 326806, 339226, 351646, 364067, 376487, 388907, 401327, 413747, 426168, 438588, 451008, 463428, 475848, 488269, 500689, 513109, 525529, 537949]]
    攻击次数4 = 1
    data4 = [int(i*1.209) for i in [0, 40171, 49486, 58801, 68117, 77432, 86747, 96062, 105377, 114692, 124007, 133323, 142638, 151953, 161268, 170583, 179898, 189213, 198529, 207844, 217159, 226474, 235789, 245104, 254420, 263735, 273050, 282365, 291680, 300995, 310310, 319626, 328941, 338256, 347571, 356886, 366201, 375516, 384832, 394147, 403462]]
    攻击次数5 = 1
    data5 = [int(i*1.209) for i in [0, 93733, 115469, 137204, 158939, 180675, 202410, 224145, 245881, 267616, 289351, 311087, 332822, 354557, 376293, 398028, 419763, 441499, 463234, 484969, 506705, 528440, 550175, 571911, 593646, 615382, 637117, 658852, 680588, 702323, 724058, 745794, 767529, 789264, 811000, 832735, 854470, 876206, 897941, 919676, 941412]]
    攻击次数6 = 1

    CD = 290
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

归元·柔道家·男一觉序号 = 0
归元·柔道家·男二觉序号 = 0
归元·柔道家·男三觉序号 = 0
for i in 技能列表:
    if i.所在等级 == 50:
        归元·柔道家·男一觉序号 = 技能序号[i.名称]
    if i.所在等级 == 85:
        归元·柔道家·男二觉序号 = 技能序号[i.名称]
    if i.所在等级 == 100:
        归元·柔道家·男三觉序号 = 技能序号[i.名称]

归元·柔道家·男护石选项 = ['无']
for i in 技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        归元·柔道家·男护石选项.append(i.名称)

归元·柔道家·男符文选项 = ['无']
for i in 技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        归元·柔道家·男符文选项.append(i.名称)


class 归元·柔道家·男角色属性(角色属性):
    实际名称 = '归元·柔道家·男'
    角色 = '格斗家(男)'
    职业 = '柔道家'

    武器选项 = ['臂铠', '手套', '东方棍', '爪']

    类型选择 = ['物理百分比']

    类型 = '物理百分比'
    防具类型 = '轻甲'
    防具精通属性 = ['力量']

    主BUFF = 2.08

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(技能列表)
        self.技能序号 = deepcopy(技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['无情摔击']
                 ].被动倍率 /= self.技能栏[self.技能序号['摔技强化']].加成倍率(self.武器类型)


class 归元·柔道家·男(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 归元·柔道家·男角色属性()
        self.角色属性A = 归元·柔道家·男角色属性()
        self.角色属性B = 归元·柔道家·男角色属性()
        self.一觉序号 = 归元·柔道家·男一觉序号
        self.二觉序号 = 归元·柔道家·男二觉序号
        self.三觉序号 = 归元·柔道家·男三觉序号
        self.护石选项 = deepcopy(归元·柔道家·男护石选项)
        self.符文选项 = deepcopy(归元·柔道家·男符文选项)
