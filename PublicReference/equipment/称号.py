import re
from PublicReference.equipment.base_item import Item

# 称号属性部分

称号列表 = [None] * 26


class 称号25(Item):
    显示名称 = 'Midsummer Lv 80'
    名称 = 'Midsummer Lv 80'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(80, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Atk.Dmg +15%<br>'
        temp += 'Lv 80 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'STR +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号24(Item):
    显示名称 = 'Midsummer Lv 75'
    名称 = 'Midsummer Lv 75'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(75, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.75 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号23(Item):
    显示名称 = 'Midsummer Lv 70'
    名称 = 'Midsummer Lv 70'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(70, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.70 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号22(Item):
    显示名称 = 'Midsummer Lv 45'
    名称 = 'Midsummer Lv 45'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(45, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.45 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号21(Item):
    显示名称 = 'Midsummer Lv 40'
    名称 = 'Midsummer Lv 40'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(40, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.40 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号20(Item):
    显示名称 = 'Midsummer Lv 35'
    名称 = 'Midsummer Lv 35'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(35, 0.10)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.35 Skill Atk 10%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号19(Item):
    显示名称 = 'Midsummer Lv 30'
    名称 = 'Midsummer Lv 30'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.技能倍率加成(30, 0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'Lv.30 Skill Atk 15%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号18(Item):
    显示名称 = 'A Midsummer Night'
    名称 = 'A Midsummer Night'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp
    
    
class 称号17(Item):
    显示名称 = 'Monster Cosplay'
    名称 = 'Bearer of Destiny'

    def 城镇属性(self, 属性):
        属性.力量 += 45
        属性.智力 += 45
        属性.伤害增加加成 (0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +45<br>'
        temp += 'Intelligence +45<br>'
        temp += 'Attack Damage +15%<br>'
        return temp


class 称号16(Item):
    显示名称 = 'Serene Dawn'
    名称 = 'Serene Dawn'

    def 城镇属性(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.物理攻击力 += 100
        属性.魔法攻击力 += 100
        属性.独立攻击力 += 100

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +100<br>'
        temp += 'Intelligence +100<br>'
        temp += 'Physical Atk +100<br>'
        temp += 'Magical Atk +100<br>'
        temp += 'Independent Atk +100<br>'
        return temp


class 称号15(Item):
    显示名称 = 'Warm Morning'
    名称 = 'Warm Morning'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.所有属性强化加成(30)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'All Ele +30<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号14(Item):
    显示名称 = 'Theather Puppet'
    名称 = 'Theater Puppet'

    def 城镇属性(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.伤害增加加成 (0.10)
        属性.技能等级加成('所有', 50, 50, 1)
        属性.技能等级加成('所有', 85, 85, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +100<br>'
        temp += 'Intelligence +100<br>'
        temp += 'Attack Damage +10%<br>'
        temp += 'Lv 50 Active Skill +1<br>'
        temp += 'Lv 85 Active Skill +1<br>'
        return temp


class 称号13(Item):
    显示名称 = 'Aeterna'
    名称 = 'Aeterna Hunter'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 30
        属性.附加伤害加成(0.10)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Physical Atk +30<br>'
        temp += 'Magical Atk +30<br>'
        temp += 'Independent Atk +30<br>'
        temp += 'Bonus Damage +10%<br>'
        return temp


class 称号12(Item):
    显示名称 = 'Welcome to Harlem [Return]'
    名称 = 'Return of Harlem'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.所有属性强化加成(5)
        属性.最终伤害加成(0.10)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'All Ele +5<br>'
        temp += 'All.Atk +10%<br>'
        return temp


class 称号11(Item):
    显示名称 = 'Arad Pass S1'
    名称 = 'Arad Pass S1'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成 (0.15)
        属性.所有属性强化加成(5)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'Attack Damage +15%<br>'
        temp += 'All Ele +4<br>'
        temp += '<font color="#00A2E8">Chance Option:</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp
    

class 称号10(Item):
    显示名称 = 'Awakened All in One'
    名称 = 'All-in-One 2nd'

    def 城镇属性(self, 属性):
        属性.技能等级加成('主动', 15, 35, 2)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Lv 15-35 Active Skill +2<br>'
        return temp


class 称号9(Item):
    显示名称 = 'Ex: Doppelganger'
    名称 = 'Ex: Doppelganger'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.所有属性强化加成(10)
        属性.最终伤害加成(0.15)
        属性.物理攻击力 += 20
        属性.魔法攻击力 += 20
        属性.独立攻击力 += 20

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'All Ele +10<br>'
        temp += 'All.Atk +15%<br>'
        temp += 'Physical Atk +20<br>'
        temp += 'Magical Atk +20<br>'
        temp += 'Independent Atk +20<br>'
        return temp


class 称号8(Item):
    显示名称 = 'Limit Breaker'
    名称 = 'Limit Breaker'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.最终伤害加成(0.10)
        属性.技能等级加成('所有', 85, 85, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +30<br>'
        temp += 'Intelligence +30<br>'
        temp += 'All.Atk +10%<br>'
        temp += 'Lv.85 Active Skill +1<br>'
        return temp


class 称号7(Item):
    显示名称 = 'Limit Contender'
    名称 = 'Limit Contender'

    def 城镇属性(self, 属性):
        属性.力量 += 125
        属性.智力 += 125
        属性.技能等级加成('所有', 50, 50, 1)
        属性.技能等级加成('所有', 85, 85, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +125<br>'
        temp += 'Intelligence +125<br>'
        temp += 'Lv.50 Active Skill +1<br>'
        temp += 'Lv.85 Active Skill +1<br>'
        return temp


class 称号6(Item):
    显示名称 = 'Limit Conqueror'
    名称 = 'Limit Conqueror'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.最终伤害加成(0.15)
        属性.技能等级加成('所有', 85, 85, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +40<br>'
        temp += 'Intelligence +40<br>'
        temp += 'All.Atk +15%<br>'
        temp += 'Lv.85 Active Skill +1<br>'
        return temp


class 称号5(Item):
    显示名称 = 'Hot Summer 2019'
    名称 = 'Pink Dolphin'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.所有属性强化加成(22)

    def 触发属性(self, 属性):
        属性.进图力量 += 25
        属性.进图智力 += 25

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +30<br>'
        temp += 'Intelligence +30<br>'
        temp += 'All Ele +22<br>'
        temp += '<font color="#00A2E8">Chance Option：</font><br>'
        temp += 'Strength +25<br>'
        temp += 'Intelligence +25<br>'
        return temp


class 称号4(Item):
    显示名称 = 'Heroes of Ethos [Bronze]'
    名称 = 'Heroes of Ethos [Bronze]'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成(0.05)
        属性.附加伤害加成(0.05)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Attack Damage +5%<br>'
        temp += 'Bonus Damage +5%<br>'
        return temp


class 称号3(Item):
    显示名称 = 'Heroes of Ethos [Silver]'
    名称 = 'Heroes of Ethos [Silver]'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.暴击伤害加成(0.05)
        属性.附加伤害加成(0.05)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Critical Damage +5%<br>'
        temp += 'Bonus Damage +5%<br>'
        return temp


class 称号2(Item):
    显示名称 = 'Heroes of Ethos [Obsidian]'
    名称 = 'Heroes of Ethos [Obsidian]'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成(0.05)
        属性.暴击伤害加成(0.05)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Attack Damage +5%<br>'
        temp += 'Critical Damage +5%<br>'
        return temp


class 称号1(Item):
    显示名称 = 'Heroes of Ethos [Gold]'
    名称 = 'Heroes of Ethos [Gold]'

    def 城镇属性(self, 属性):
        属性.力量 += 40
        属性.智力 += 40
        属性.伤害增加加成(0.05)
        属性.暴击伤害加成(0.05)
        属性.附加伤害加成(0.05)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Attack Damage +5%<br>'
        temp += 'Critical Damage +5%<br>'
        temp += 'Bonus Damage +5%<br>'
        return temp


class 称号0(Item):
    pass


for i in range(len(称号列表)):
    exec('称号列表[{}] = 称号{}()'.format(len(称号列表) - i - 1, i))

称号序号 = dict()
for i in range(len(称号列表)):
    称号序号[称号列表[i].名称] = i
