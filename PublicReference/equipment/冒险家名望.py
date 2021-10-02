import itertools
称号名望 = {1:315,2:397,3:491,4:601,5:731,100:783,101:849,102:934,103:1044,250:10000}
宠物名望 = {1: 315, 315: 2, 2: 397, 397: 3, 3: 491, 491: 4, 4: 601, 601: 5, 5: 731, 731: 100, 100: 752, 752: 101, 101: 778, 778: 102, 102: 805, 805: 103, 103: 832, 832: 104, 104: 860, 860: 105, 105: 889, 889: 106, 106: 919, 919: 107, 107: 949, 949: 108, 108: 980, 980: 109, 109: 1012, 1012: 110, 110: 1044, 1044: 111, 111: 1055}
附魔名望 = {1: 56, 56: 2, 2: 69, 69: 3, 3: 86, 86: 4, 4: 106, 106: 5, 5: 130, 130: 6, 6: 138, 138: 7, 7: 147, 147: 8, 8: 158, 158: 100, 100: 139, 139: 101, 101: 153, 153: 102, 102: 168, 168: 103, 103: 185}
宠物附魔名望 = {100: 139, 139: 101, 101: 148, 148: 102, 102: 159, 159: 103, 103: 170, 170: 104, 104: 185, 185: 200, 200: 116}
称号附魔名望 = {1: 93, 93: 2, 2: 107, 107: 3, 3: 130, 130: 100, 100: 139, 139: 101, 101: 153, 153: 102, 102: 168, 168: 103, 103: 185}
武器装扮名望 = {1:72,100:94}
光环名望 = {1: 140, 140: 2, 2: 170, 170: 3, 3: 209, 209: 4, 4: 260, 260: 5, 5: 325, 325: 100, 100: 464}
皮肤名望 = {1: 21, 21: 100, 100: 30, 30: 101, 101: 41, 41: 102, 102: 54, 54: 103, 103: 69}
巨龙名望 = {1:795, 2:530, 3:265}
快捷栏装备名望 = {1:20, 2:40}
锻造名望={1: 2, 2: 4,3:7,4:8,5:10,6:11,7:12,8:13}
改造名望={1: 4, 4: 10, 2: 6, 6: 14, 3: 8, 8: 18, 10: 21, 5: 12, 12: 23, 14: 25, 7: 16, 16: 27, 18: 29, 9: 20, 20: 31, 21: 11, 11: 22, 22: 12, 23: 13, 13: 24, 24: 14, 25: 15, 15: 26, 26: 16, 27: 17, 17: 28, 28: 18, 29: 19, 19: 30, 30: 20}
融合名望= {1: [46, 23, 46, 23], 2: [61, 31, 46, 23], 3: [77, 39, 46, 23], 4: [46, 23, 46, 23], 5: [61, 31, 46, 23], 6: [77, 39, 46, 23], 7: [46, 23, 61, 31], 8: [61, 31, 61, 31], 9: [77, 39, 61, 31], 10: [46, 23, 61, 31], 11: [61, 31, 61, 31], 12: [77, 39, 61, 31], 13: [46, 23, 77, 39], 14: [61, 31, 77, 39], 15: [77, 39, 77, 39], 16: [46, 23, 77, 39], 17: [61, 31, 77, 39], 18: [77, 39, 77, 39]}
辟邪玉名望 = {0:0, 1: 30, 2: 45, 3:67, 4:93}
装扮名望 = {"神器": 116, "稀有":88 ,"高级":69}

称号表 = {'明日-春华':3,'圣殿之巅': 5, '桃园结义 [义]': 100, '三英雄 [义]': 5, '荣耀贵族': 4,
'骑士王的荣耀': 4, '海洋霸主': 4, '龙之挑战': 5, '龙之威仪': 5, '兽人守护神': 5,
'天选之人': 100, '秘境迷踪': 5, '神选之英杰': 102, '超越极限者': 100,
'使徒降临': 101, '伟大的意志': 103, 'DPL专属称号 (输出)': 5, '安徒恩的烈焰': 100,
'卢克的创造': 100, '伊希斯的天空': 100, '希洛克的悲鸣': 100, '信念之启示': 100,
'隐忍之启示': 100, '勇气之启示': 100, '希望之启示':100, '神之试炼': 100, '永恒追猎': 101, '永恒判罪': 101, '永恒战吼': 101, '穿越星空的祈愿': 103}

# 100级，史诗
强化名望 = [3,5,8,10,12,15,17,29,32,45,89,142,154,166,178,190,202,213,225,237,249,261,273,284,296,308,320,332,344,355,367]
武器强化名望 = [8,15,23,30,37,45,52,89,100,141,276,443,480,517,554,591,628,664,701,738,775,812,849,886,923,960,996,1033,1070,1107,1144]

装备列 = {
    "上衣": 0,
    "下装": 1,
    "头肩": 2,
    "腰带": 3,
    "鞋": 4,
    "手镯": 5,
    "项链": 6,
    "戒指": 7,
    "左槽": 8,
    "右槽": 9,
    "耳环": 10,
    "武器": 11,
    "称号": 12,
    "光环": 13,
    "武器装扮": 14,
    "皮肤": 15,
    "时装": 16,
}


细节列 = {
    "收集箱" : 6,
    "勋章" : 7,
    "宠物装备红" : 11,
    "宠物装备蓝" : 12,
    "宠物装备绿" : 13,
    "宠物附魔" : 14
    }


def 强化名望计算(装备等级, 品质, 强化等级):
    if 装备等级 == 100:
        if 品质 == "史诗":
            return 强化名望[强化等级]
        if 品质 == "神话":
            return 神话强化名望[强化等级]
    return -1


def 武器强化名望计算(装备等级, 品质, 强化等级):
    if 装备等级 == 100:
        if 品质 == "史诗":
            return 武器强化名望[强化等级]
    return -1


# 强化等级
# 是否增幅
# 改造等级

def 细节收集(部位名称, 属性设置输入):
    目标列 = 细节列[部位名称]
    result = []
    for i in range(6):
        result.append(int(属性设置输入[i][目标列].text()))
    return result

def 收集箱名望计算(角色属性):
    属性设置输入 = 角色属性.属性设置输入
    收集箱 = 细节收集("收集箱",属性设置输入)
    力量 = 收集箱[0]
    智力 = 收集箱[1]
    物攻 = 收集箱[2]
    魔攻 = 收集箱[3]
    独立 = 收集箱[4]
    属强 = 收集箱[5]
    if 属强 == 10:
        return 160 # 春节套, 2021-12-31
    elif 属强 == 5:
        return 80 # 夏日套, 2022-06-30
    else:
        return -99999

def 勋章名望计算(角色属性):
    细节选项输入 = 角色属性.细节选项输入
    勋章强化等级 = 细节选项输入[0][7].currentIndex()
    基础名望 = 232
    if 勋章强化等级 == 0:
        return 基础名望 + 0
    else:
        return 基础名望 + int(((勋章强化等级 - 8) / 2))

def 徽章部位名望计算(角色属性, 部位):
    def 徽章名望组合():
        def 排列组合(徽章字典):
            idx = list(徽章字典.keys())
            target = [i for i in range(len(idx))]
            comb = itertools.combinations_with_replacement(target,2)
            result = {}
            for i in comb:
                key = idx[i[0]]+idx[i[1]]
                value = 徽章字典[idx[i[0]]] + 徽章字典[idx[i[1]]]
                result[key] = value
            return result
        徽章四维名望 = {
            17: 30,
            25: 36,
            35: 46,
            20: 46
        }
        黄绿特殊徽章 = {
            10: 30,
            15: 36,
            20: 46
        }
        徽章三攻名望 = {
            10: 30,
            15: 36,
            20: 46,
        }
        return 排列组合(徽章四维名望), 排列组合(徽章三攻名望), 排列组合(黄绿特殊徽章)

    属性设置输入, 细节选项输入 = 角色属性.属性设置输入, 角色属性.细节选项输入
    部位列 = 装备列[部位]
    力智值 = 属性设置输入[9][部位列].text()
    三攻 = 属性设置输入[10][部位列].text()
    if 力智值 == "" and 三攻 == "": return 0
    力智表, 三攻表, 特殊徽章表 = 徽章名望组合()
    try:
        if 部位 in ["头肩", "项链", "上衣", "下装"]:
            力智表 = 特殊徽章表
        if 部位 in ["左槽", "右槽"]:
            if 力智值 != "":
                力智值 = int(力智值)
                if 力智值 == 8:
                    技能 = 细节选项输入[2][8+["左槽", "右槽"].index(部位)].currentText()
                    if 技能 != "无":
                        return 232
                    else:
                        return 109
                else:
                    return -99999
        if 力智值 != "":
            if 三攻 != "":
                return -99999
            力智值 = int(力智值)
            return 力智表.get(力智值, -99999)
        if 三攻 != "":
            三攻 = int(三攻)
        return 三攻表.get(三攻, -99999)
    except Exception as e:
        print(e)
        return -99999

def 徽章名望计算(角色属性):
    徽章 = {}
    for 部位 in 装备列:
        部位名望 = 徽章部位名望计算(角色属性, 部位)
        徽章[部位] = 部位名望
    return 徽章

def 称号名望计算(角色属性):
    称号名称 = 角色属性.角色属性B.称号

def 时装名望计算(角色属性):
    所有时装 = [时装选项.currentText() for 时装选项 in 角色属性.时装选项]
    所有时装 = 所有时装[:-1]  # [8]是 所有选项
    最终时装名望 = sum(装扮名望[时装] for 时装 in 所有时装)
    return 最终时装名望

def 辟邪玉名望计算(角色属性):
    辟邪玉等级 = sum(1 for 辟邪玉词条 in 角色属性.辟邪玉选择 if 辟邪玉词条.currentIndex() != 0)
    return 辟邪玉名望[辟邪玉等级]

def 护石名望计算(角色属性):
    护石名望 = {"圣痕": 185, "魔界": 120}
    护石等级 = [护石.currentText() for 护石 in 角色属性.护石类型选项]
    护石最终名望 = sum(护石名望[护石等级_] for 护石等级_ in 护石等级)
    return 护石最终名望

def 符文名望计算(角色属性):
    符文名望 = {0: 0, 1: 46, 2: 21, 3:18, 4:15}
    最终符文名望 = sum(符文名望[int(符文.currentIndex()/4)+1] for 符文 in 角色属性.符文效果 if 符文.currentIndex() != 0)
    return 最终符文名望

def 获取人物名望(角色属性):
    # 名望 = 装备 + 增幅/强化/锻造 + 附魔 +
    #        徽章 + 装扮 + 称号 + 宠物 +
    #        宠物装备 + 护石 + 符文 + 勋章 + 辟邪玉 + 收集箱

    # 装备 开始
    所有装备 = 角色属性.角色属性B.装备栏

    # 增幅/强化/锻造 开始

    # 附魔 开始

    徽章名望 = 徽章名望计算(角色属性)
    时装名望 = 时装名望计算(角色属性)
    护石名望 = 护石名望计算(角色属性)
    符文名望 = 符文名望计算(角色属性)
    勋章名望 = 勋章名望计算(角色属性)
    辟邪玉名望 = 辟邪玉名望计算(角色属性)
    收集箱名望 = 收集箱名望计算(角色属性)

    print(徽章名望, 时装名望, 护石名望, 符文名望, 勋章名望, 辟邪玉名望, 收集箱名望)
