import itertools

from PublicReference.equipment.equ_list import equ
from PublicReference.utils.constant import *

称号名望 = {1: 315, 2: 397, 3: 491, 4: 601, 5: 731, 100: 783, 101: 849, 102: 934, 103: 1044, 250: 10000}
宠物名望表 = {1: 315, 2: 397, 3: 491, 4: 601, 5: 731, 100: 752, 101: 778, 102: 805, 103: 832, 104: 860, 105: 889, 106: 919,
        107: 949, 108: 980, 109: 1012, 110: 1044, 111: 1055}
附魔名望 = {1: 56, 2: 69, 3: 86, 4: 106, 5: 130, 6: 138, 7: 147, 8: 158, 100: 139, 101: 153, 102: 168, 103: 185}
宠物附魔名望 = {100: 139, 101: 148, 102: 159, 103: 170, 104: 185, 200: 116}
称号附魔名望 = {1: 93, 2: 107, 3: 130, 100: 139, 101: 153, 102: 168, 103: 185}
武器装扮名望 = {1: 72, 100: 94}
光环名望 = {1: 140, 2: 170, 3: 209, 4: 260, 5: 325, 100: 464}
宠物装备名望 = {1: 21, 100: 30, 101: 41, 102: 54, 103: 69}
巨龙名望 = {1: 795, 2: 530, 3: 265}
快捷栏装备名望 = {1: 20, 2: 40}
锻造名望 = {1: 2, 2: 4, 3: 7, 4: 8, 5: 10, 6: 11, 7: 12, 8: 13}
改造名望 = {1: 4, 2: 6, 3: 8, 4: 10, 5: 12, 6: 14, 7: 16, 8: 18, 9: 20, 10: 21, 11: 22, 12: 23, 13: 24, 14: 25, 15: 26,
        16: 27, 17: 28, 18: 29, 19: 30, 20: 31}
融合名望 = {1: [46, 23, 46, 23], 2: [61, 31, 46, 23], 3: [77, 39, 46, 23], 4: [46, 23, 46, 23], 5: [61, 31, 46, 23],
        6: [77, 39, 46, 23], 7: [46, 23, 61, 31], 8: [61, 31, 61, 31], 9: [77, 39, 61, 31], 10: [46, 23, 61, 31],
        11: [61, 31, 61, 31], 12: [77, 39, 61, 31], 13: [46, 23, 77, 39], 14: [61, 31, 77, 39], 15: [77, 39, 77, 39],
        16: [46, 23, 77, 39], 17: [61, 31, 77, 39], 18: [77, 39, 77, 39]}
辟邪玉名望 = {0: 0, 1: 30, 2: 45, 3: 67, 4: 93}
装扮名望 = {"神器": 116, "稀有": 88, "高级": 69}
#守护珠名望 = {1:46*4, 2:36*4, 3:29*4}

附魔名望选项 = {
    "上衣": list(附魔名望.values()),
    "下装": list(附魔名望.values()),
    "头肩": list(附魔名望.values()),
    "腰带": list(附魔名望.values()),
    "鞋": list(附魔名望.values()),
    "手镯": list(附魔名望.values()),
    "项链": list(附魔名望.values()),
    "戒指": list(附魔名望.values()),
    "辅助装备": list(附魔名望.values()),
    "魔法石": list(附魔名望.values()),
    "耳环": list(附魔名望.values()),
    "武器": list(附魔名望.values()),
    "称号附魔": list(称号附魔名望.values()),
    "光环": list(光环名望.values()),
    "武器装扮": list(武器装扮名望.values()),
    "宠物装备红": list(宠物装备名望.values()),
    "宠物装备蓝": list(宠物装备名望.values()),
    "宠物装备绿": list(宠物装备名望.values()),
    #    "宠物": list(宠物名望.values()),
    "宠物附魔": list(宠物附魔名望.values()),
    "皮肤": list(附魔名望.values()),
   # "守护珠": list(守护珠名望.values()),
    "时装": [0],
}

附魔名望默认选项 = {
    "上衣": 130,
    "下装": 130,
    "头肩": 168,
    "腰带": 168,
    "鞋": 168,
    "手镯": 130,
    "项链": 130,
    "戒指": 130,
    "辅助装备": 168,
    "魔法石": 158,
    "耳环": 130,
    "武器": 130,
    #    "称号": 185,
    "称号附魔": 185,
    "光环": 464,
    "武器装扮": 94,
    "宠物装备红": 69,
    "宠物装备蓝": 69,
    "宠物装备绿": 69,
    "宠物附魔": 185,
    #    "宠物": 1055,
    "皮肤": 69
}

称号名望表 = {'明日-春华': 3, '圣殿之巅': 5, '桃园结义[义]': 100, '三英雄[义]': 5, '荣耀贵族': 4,
         '骑士王的荣耀': 4, '海洋霸主': 4, '龙之挑战': 5, '龙之威仪': 5, '兽人守护神': 5,
         '天选之人': 100, '秘境迷踪': 5, '神选之英杰': 102, '超越极限者': 100,
         '使徒降临': 101, '伟大的意志': 103, 'DPL专属称号·输出': 5, '安徒恩的烈焰': 100,
         '卢克的创造': 100, '伊希斯的天空': 100, '希洛克的悲鸣': 100, '信念之启示': 100,
         '隐忍之启示': 100, '勇气之启示': 100, '希望之启示': 100, '神之试炼': 100, '永恒追猎': 101, '永恒判罪': 101, '永恒战吼': 101, '穿越星空的祈愿': 103}

内置宠物名望表 = {"火神的化身": 111, "骑士/精灵使": 107, "比拉谢尔号": 106, "夏日之恋莱森德": 5, "夏日之恋赫米雅": 5, "暴风圣女": 110, "神迹·莱恩": 108, "神官": 106,
         "莱恩": 102, "蒂雅": 100, "克里斯": 5, "关羽": 1, "墨仙雪莲": 1}

# 100级，史诗
装备强化名望 = [0, 3, 5, 8, 10, 12, 15, 17, 29, 32, 45, 89, 142, 154, 166, 178, 190, 202, 213, 225, 237, 249, 261, 273, 284, 296,
          308, 320, 332, 344, 355, 367]
装备增幅名望 = [0, 3, 6, 8, 11, 14, 16, 19, 32, 36, 50, 99, 158, 171, 185, 198, 211, 224, 237, 250, 263, 276, 289, 302, 315, 328,
          341, 354, 369, 382, 395, 408]

装备改造名望 = [0, 11, 16, 32, 50, 158, 185, 211, 237, 263, 277, 290, 303, 316, 329, 342, 355, 369, 382, 395, 408, 408, 408, 408,
          408, 408, 408, 408, 408, 408, 408, 408]
武器改造名望 = [0, 33, 50, 99, 156, 492, 574, 656, 738, 820, 861, 902, 943, 984, 1025, 1066, 1107, 1148, 1189, 1230, 1271, 1271,
          1271, 1271, 1271, 1271, 1271, 1271, 1271, 1271, 1271, 1271]
神话装备强化名望 = [0, 3, 6, 9, 12, 15, 18, 21, 36, 40, 57, 111, 178, 193, 208, 222, 237, 252, 267, 282, 296, 311, 326, 341, 355,
            370, 385, 400, 415, 429, 444, 459]
神话装备增幅名望 = [0, 4, 7, 10, 14, 17, 20, 24, 40, 45, 63, 123, 198, 214, 231, 247, 263, 280, 296, 313, 329, 346, 362, 378, 395,
            411, 428, 444, 461, 477, 493, 510]
武器强化名望 = [0, 8, 15, 23, 30, 37, 45, 52, 89, 100, 141, 276, 443, 480, 517, 554, 591, 628, 664, 701, 738, 775, 812, 849, 886,
          923, 960, 996, 1033, 1070, 1107, 1144]
武器增幅名望 = [0, 9, 17, 25, 33, 41, 50, 58, 99, 111, 156, 307, 492, 533, 574, 615, 656, 697, 738, 779, 820, 861, 902, 943, 984,
          1025, 1066, 1107, 1148, 1189, 1230, 1271]

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
    "收集箱": 6,
    "勋章": 7,
    "宠物装备红": 11,
    "宠物装备蓝": 12,
    "宠物装备绿": 13,
    "宠物附魔": 14
}


# 强化等级
# 是否增幅
# 改造等级

def 细节收集(部位名称, 属性设置输入):
    目标列 = 细节列[部位名称]
    result = []
    for i in range(6):
        s = 属性设置输入[i][目标列].text()
        if len(s) != 0:
            s = int(s)
        else:
            s = 0
        result.append(s)
    return result


def 收集箱名望计算(人物设置):
    属性设置输入 = 人物设置.属性设置输入
    收集箱 = 细节收集("收集箱", 属性设置输入)
    力量 = 收集箱[0]
    智力 = 收集箱[1]
    物攻 = 收集箱[2]
    魔攻 = 收集箱[3]
    独立 = 收集箱[4]
    属强 = 收集箱[5]
    if 属强 == 10:
        return 175  # 春节套, 2021-12-31
    elif 属强 == 5:
        return 80  # 夏日套, 2022-06-30
    else:
        return -99999


def 勋章名望计算(人物设置):
    细节选项输入 = 人物设置.细节选项输入
    勋章强化等级 = 细节选项输入[0][7].currentIndex()
    基础名望 = 232 + 46*4
    if 勋章强化等级 == 0:
        return 基础名望 + 0
    else:
        return 基础名望 + int(((勋章强化等级 - 8) / 2))


def 徽章部位名望计算(角色属性, 部位):
    def 徽章名望组合():
        def 排列组合(徽章字典):
            idx = list(徽章字典.keys())
            target = [i for i in range(len(idx))]
            comb = itertools.combinations_with_replacement(target, 2)
            result = {}
            for i in comb:
                key = idx[i[0]] + idx[i[1]]
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
                    技能 = 细节选项输入[2][8 + ["左槽", "右槽"].index(部位)].currentText()
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


def 徽章名望计算(人物设置):
    徽章 = {}
    for 部位 in 装备列:
        部位名望 = 徽章部位名望计算(人物设置, 部位)
        徽章[部位] = 部位名望
    徽章.pop("耳环")
    徽章.pop("武器")
    徽章.pop("称号")
    徽章.pop("时装")
    return 徽章


def 称号名望计算(人物设置):
    称号名称 = 人物设置.称号.currentText()[7:]
    称号基础名望 = 称号名望[称号名望表[称号名称]]
    return 称号基础名望


def 时装名望计算(人物设置):
    所有时装 = [时装选项.currentText() for 时装选项 in 人物设置.时装选项]
    所有时装 = 所有时装[:-1]  # [8]是 所有选项
    最终时装名望 = sum(装扮名望[时装] for 时装 in 所有时装)
    return 最终时装名望


def 辟邪玉名望计算(人物设置):
    辟邪玉等级 = sum(1 for 辟邪玉词条 in 人物设置.辟邪玉选择 if 辟邪玉词条.currentIndex() != 0)
    return 辟邪玉名望[辟邪玉等级]


def 护石名望计算(人物设置):
    护石名望 = {"圣痕": 185, "魔界": 120}
    护石等级 = [护石.currentText() for 护石 in 人物设置.护石类型选项]
    护石最终名望 = sum(护石名望[护石等级_] for 护石等级_ in 护石等级)
    return 护石最终名望


def 符文名望计算(人物设置):
    符文名望 = {0: 0, 1: 46, 2: 21, 3: 18, 4: 15}
    最终符文名望 = sum(符文名望[int(符文.currentIndex() / 4) + 1] for 符文 in 人物设置.符文效果 if 符文.currentIndex() != 0)
    return 最终符文名望


def 宠物名望计算(人物设置):
    宠物名称 = 人物设置.宠物.currentText()
    宠物名称 = 宠物名称[7:]
    最终宠物名望 = 宠物名望表.get(内置宠物名望表[宠物名称],0)

    return 最终宠物名望


def 装备基础名望计算(角色属性):
    所有装备 = 角色属性.装备栏
    改造数目 = sum(1 for 装备 in 所有装备 if equ.get_equ_by_name(装备).所属套装 == "智慧产物")
    改造基础名望 = 632 * 改造数目
    史诗基础名望 = 464 * (11 - 改造数目)
    套装基础名望 = len(角色属性.套装栏) * 265
    return 改造基础名望 + 史诗基础名望 + 套装基础名望


def 装备打造名望计算(角色属性):
    所有装备 = 角色属性.装备栏[:-1]  # 去掉武器
    打造名望 = {}
    for i in range(len(所有装备)):
        装备 = equ.get_equ_by_name(所有装备[i])
        单件装备打造名望 = 0
        if 装备.品质 not in ["史诗", "神话"]:
            单件装备打造名望 = -99999
        else:
            if 装备.所属套装 == "智慧产物":
                改造等级 = 角色属性.改造等级[i]
                单件装备打造名望 = 装备改造名望[改造等级]
            else:
                打造等级 = 角色属性.强化等级[i]
                if 角色属性.是否增幅[i]:
                    if 装备.品质 == "史诗":
                        单件装备打造名望 = 装备增幅名望[打造等级]
                    else:
                        单件装备打造名望 = 神话装备增幅名望[打造等级]
                else:
                    if 装备.品质 == "史诗":
                        单件装备打造名望 = 装备强化名望[打造等级]
                    else:
                        单件装备打造名望 = 神话装备强化名望[打造等级]
        打造名望[装备.部位] = 单件装备打造名望
    return 打造名望


def 武器名望计算(角色属性):
    武器 = equ.get_equ_by_name(角色属性.装备栏[-1])
    if 武器.品质 != "史诗":
        return -99999
    武器最终计算名望 = 0
    武器基础名望 = 464
    武器打造名望 = 0
    if 武器.所属套装 == "智慧产物":
        武器基础打造 = 角色属性.改造等级[-1]
    else:
        武器基础打造 = 角色属性.强化等级[-1]
    武器增幅 = 角色属性.是否增幅[-1]
    if 武器增幅:
        武器打造名望 = 武器增幅名望[武器基础打造]
    else:
        武器打造名望 = 武器强化名望[武器基础打造]
    if "固伤" in 角色属性.类型:
        if 角色属性.角色属性B.武器锻造等级 != 8:
            武器打造名望 = -99999
        else:
            武器打造名望 = max(480, 武器最终计算名望)

    return 武器基础名望 + 武器打造名望


def 附魔名望计算():
    附魔名望 = store.get("/fame/selection")
    if 附魔名望 == None:
        附魔名望 = 附魔名望默认选项
    else:
        for 名望 in 附魔名望:
            附魔名望[名望] = int(附魔名望[名望])
    return 附魔名望


# 黑鸦
# https://dnf.qq.com/cp/a20210325version/page3.html

def 黑鸦名望计算(人物设置, 改造部位):
    黑鸦词条 = 人物设置.黑鸦词条
    黑鸦名望表 = {0: 69, 1: 83, 2: 98, 3: 116}
    黑鸦总名望 = {}
    黑鸦选项表 = {0: "武器", 1: "戒指", 2: "辅助装备", 3: "下装"}
    for i in range(len(黑鸦词条)):
        黑鸦选项 = 黑鸦词条[i]
        部位 = 黑鸦选项表[i]
        if 部位 in 改造部位: continue
        选项 = 黑鸦选项[0].currentIndex()
        品级 = 黑鸦选项[2].currentIndex()
        if 选项 == 0:
            黑鸦总名望[部位] = 0
        elif 选项 == 1:
            黑鸦总名望[部位] = 黑鸦名望表[3]  # 计算最高
        else:
            黑鸦总名望[部位] = 黑鸦名望表[品级]

    return 黑鸦总名望


def 改造升级黑鸦名望计算(人物设置, 角色属性):
    改造升级名望 = {}
    属性1名望 = {0: 91, 1: 71, 2: 54}
    属性2名望 = {0: 15, 1: 12, 2: 9}
    属性3名望 = {0: 10, 1: 8, 2: 6}
    if not 人物设置.智慧产物升级.isChecked():
        return {}

    所有装备 = 角色属性.装备栏  #
    改造产物 = []
    改造名称 = []
    for i in range(len(所有装备)):
        装备 = equ.get_equ_by_name(所有装备[i])
        if 装备.所属套装 == "智慧产物":
            装备.改造等级 = 角色属性.改造等级[i]
            改造产物.append(装备)
            改造名称.append(装备.名称)

    count2 = 0
    for i in equ.get_equ_list():
        if i.所属套装 == '智慧产物':
            if i.名称 in 改造名称:
                i.属性1选择 = 人物设置.改造产物选项[count2 * 4 + 0]
                i.属性2选择 = 人物设置.改造产物选项[count2 * 4 + 1]
                i.属性3选择 = 人物设置.改造产物选项[count2 * 4 + 2]
                i.属性4选择 = 人物设置.改造产物选项[count2 * 4 + 3]
            count2 += 1

    for 装备 in 改造产物:
        名望 = 属性1名望[装备.属性1选择.currentIndex()]
        if 装备.改造等级 >= 6: 名望 += 属性2名望[装备.属性2选择.currentIndex()]
        if 装备.改造等级 >= 7: 名望 += 属性3名望[装备.属性3选择.currentIndex()]
        改造升级名望[装备.部位] = 名望

    return 改造升级名望


def 希洛克融合名望计算(人物设置):
    希洛克选择状态 = 人物设置.希洛克选择状态
    希洛克件数 = sum(希洛克选择状态)
    希洛克选择状态 = [希洛克选择状态[i:i + 3] for i in range(0, len(希洛克选择状态), 3)]
    希洛克成套 = sum(list(map(lambda x: sum(x), 希洛克选择状态)))
    词条1名望 = {0: 46, 1: 61, 2: 77}
    词条2名望 = {0: 23, 1: 31, 2: 39}
    残香状态 = 人物设置.希洛克武器词条[0].currentIndex()  # 2: 自选词条数值
    希洛克融合名望 = {}
    if 残香状态 == 0:
        残香名望 = 0
    else:
        if 残香状态 == 2:
            词条1 = 人物设置.希洛克武器词条[3].currentIndex()
            词条2 = 人物设置.希洛克武器词条[4].currentIndex()
        elif 残香状态 == 1:
            词条1 = 2
            词条2 = 2
        词条1适用名望 = 词条1名望[词条1]
        词条2适用名望 = 词条2名望[词条2]

        if 希洛克成套 == 3:
            残香名望 = 词条1适用名望 + 词条2适用名望
        else:
            残香名望 = 词条1适用名望

    希洛克融合名望 = {"残香名望": 残香名望, "希洛克融合名望": 116 * 希洛克件数}
    return 希洛克融合名望


def 奥兹玛融合名望计算(人物设置):
    奥兹玛选择状态 = 人物设置.奥兹玛选择状态
    奥兹玛件数 = sum(奥兹玛选择状态)

    return 奥兹玛件数 * 116

def 获取人物名望(角色属性, 人物设置):
    # 名望 = 装备 + 增幅/强化/锻造 + 附魔  + 称号 + 宠物 +
    #        宠物装备 + 徽章 + 时装 + 护石 + 符文 + 勋 章 + 辟邪玉 + 收集箱

    # 装备 开始

    装备名望 = 装备基础名望计算(角色属性)
    打造名望 = 装备打造名望计算(角色属性)
    附魔名望 = 附魔名望计算()
    称号名望 = 称号名望计算(人物设置)
    宠物名望 = 宠物名望计算(人物设置)
    武器名望 = 武器名望计算(角色属性)
    # 宠物装备名望 = 宠物装备名望计算(附魔名望默认选项) (并入附魔名望)
    徽章名望 = 徽章名望计算(人物设置)
    时装名望 = 时装名望计算(人物设置)
    护石名望 = 护石名望计算(人物设置)
    符文名望 = 符文名望计算(人物设置)
    勋章名望 = 勋章名望计算(人物设置)
    辟邪玉名望 = 辟邪玉名望计算(人物设置)
    收集箱名望 = 收集箱名望计算(人物设置)
    改造升级名望 = 改造升级黑鸦名望计算(人物设置, 角色属性)
    黑鸦名望 = 黑鸦名望计算(人物设置, 改造部位=list(改造升级名望.keys()))
    希洛克融合名望 = 希洛克融合名望计算(人物设置)
    奥兹玛融合名望 = 奥兹玛融合名望计算(人物设置)

    名望详情 = {
        "基础装备名望": 装备名望,
        "增幅/强化/锻造/改造名望": 打造名望,
        "武器名望": 武器名望,
        "附魔名望": 附魔名望,
        "称号名望": 称号名望,
        "宠物名望": 宠物名望,
        "徽章名望": 徽章名望,
        "时装名望": 时装名望,
        "护石名望": 护石名望,
        "符文名望": 符文名望,
        "勋章名望": 勋章名望,
        "辟邪玉名望": 辟邪玉名望,
        "收集箱名望": 收集箱名望,
        "黑鸦名望": 黑鸦名望,
        "改造升级名望": 改造升级名望,
        "希洛克融合名望": 希洛克融合名望,
        "奥兹玛融合名望": 奥兹玛融合名望
    }

    总名望 = 0
    for 部位 in 名望详情:
        print(部位, 名望详情[部位], 总名望)

        if isinstance(名望详情[部位], dict):
            总名望 += sum(list(名望详情[部位].values()))
        elif isinstance(名望详情[部位], list):
            总名望 += sum(名望详情[部位].values())
        else:
            总名望 += 名望详情[部位]

    # 时装页
    时装页名望 = {
        "武器装扮": 附魔名望["武器装扮"] + 徽章名望["武器装扮"],
        "光环": 附魔名望["光环"] + 徽章名望["光环"],
        "时装": 时装名望,
        "皮肤": 附魔名望["皮肤"] + 徽章名望["皮肤"],
        "宠物": 宠物名望 + 附魔名望["宠物附魔"],
        "宠物装备": 附魔名望["宠物装备红"] + 附魔名望["宠物装备蓝"] + 附魔名望["宠物装备绿"]
    }
    护石页名望 = {
        "护石": 护石名望,
        "符文": 符文名望,
    }

    print(时装页名望)
    print(护石页名望)
    print(总名望)
