# 宠物属性部分
from PublicReference.equipment.base_item import Item

宠物列表 = [None] * 19


class 宠物18(Item):
    显示名称 = 'SD Kazan'
    名称 = 'SD Kazan'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.百分比三攻加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +30<br>'
        temp += 'Intelligence +30<br>'
        temp += 'Physical/Magical/Independent Atk +15%<br>'
        return temp
    


class 宠物17(Item):
    显示名称 = 'SD Tiamat'
    名称 = 'SD Tiamat'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.伤害增加加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +30<br>'
        temp += 'Intelligence +30<br>'
        temp += 'Attack Damage +15%<br>'
        return temp
    

class 宠物16(Item):
    显示名称 = 'SD Berias'
    名称 = 'SD Berias'

    def 城镇属性(self, 属性):
        属性.力量 += 30
        属性.智力 += 30
        属性.暴击伤害加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +30<br>'
        temp += 'Intelligence +30<br>'
        temp += 'Critical Damage +15%<br>'
        return temp
    

class 宠物15(Item):
    显示名称 = 'PMI Pet'
    名称 = 'Light Shooter Victoria'

    def 城镇属性(self, 属性):
        属性.力量 += 75
        属性.智力 += 75
        属性.所有属性强化加成(10)
        属性.技能等级加成('所有', 75, 75, 1)
        属性.百分比三攻加成(0.18)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +75<br>'
        temp += 'Intelligence +75<br>'
        temp += 'All Ele +10<br>'
        temp += 'Lv75 Passive Skill +1<br>'
        temp += 'Physical/Magical/Independent Atk +18%<br>'
        return temp


class 宠物14(Item):
    显示名称 = 'TCO [Veteran]'
    名称 = 'Circle the Solar Guardian'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.技能等级加成('所有', 75, 75, 1)
        属性.暴击伤害加成(0.18)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +65<br>'
        temp += 'Intelligence +65<br>'
        temp += 'Lv75 Passive Skill +1<br>'
        temp += 'Critical Damage +18%<br>'
        return temp


class 宠物13(Item):
    显示名称 = 'TCO [Trained]'
    名称 = 'Circle the Solar Guardian'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.所有属性强化加成(20)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +65<br>'
        temp += 'Intelligence +65<br>'
        temp += 'All Ele +20<br>'
        return temp


class 宠物12(Item):
    显示名称 = 'TCO [Normal]'
    名称 = 'Circle the Solar Guardian'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.物理攻击力 += 80
        属性.魔法攻击力 += 80
        属性.独立攻击力 += 80
        
    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +65<br>'
        temp += 'Intelligence +65<br>'
        temp += 'Physical Atk +80<br>'
        temp += 'Magical Atk +80<br>'
        temp += 'Independent Atk +80<br>'
        return temp


class 宠物11(Item):
    显示名称 = 'Puppet Theater Pet'
    名称 = 'Petite Barbie'

    def 城镇属性(self, 属性):
        属性.力量 += 75
        属性.智力 += 75
        属性.所有属性强化加成(25)
        属性.技能等级加成('所有', 50, 50, 1)
        属性.技能等级加成('所有', 85, 85, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +75<br>'
        temp += 'Intelligence +75<br>'
        temp += 'All Ele +25<br>'
        temp += 'Lv50 Active Skill +1<br>'
        temp += 'Lv85 Active Skill +1<br>'
        return temp


class 宠物10(Item):
    显示名称 = 'SD Snow White Tagor'
    名称 = 'SD Tagor'

    def 城镇属性(self, 属性):
        属性.力量 += 45
        属性.智力 += 45
        属性.最终伤害加成(0.10)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +45<br>'
        temp += 'Intelligence +45<br>'
        temp += 'All.Atk +10%<br>'
        return temp


class 宠物9(Item):
    显示名称 = 'Aeterna [No-Upgrade]'
    名称 = 'Aeterna Pet'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.所有属性强化加成(15)
        属性.最终伤害加成(0.10)
        
    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +80<br>'
        temp += 'Intelligence +80<br>'
        temp += 'All Ele +15<br>'
        temp += 'All.Atk +10%<br>'
        return temp

class 宠物8(Item):
    显示名称 = 'Aeterna [Upgrade]'
    名称 = 'Aeterna Pet'

    def 城镇属性(self, 属性):
        属性.力量 += 80
        属性.智力 += 80
        属性.所有属性强化加成(15)
        属性.最终伤害加成(0.10)
        
    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +80<br>'
        temp += 'Intelligence +80<br>'
        temp += 'All Ele +15<br>'
        temp += 'All.Atk +10%<br>'
        temp += 'Increase Character Atk by +10%<br>'
        temp += '(NEED TO CHECK PET SWAP 10% 2nd Tab)<br>'
        return temp

class 宠物7(Item):
    显示名称 = 'Masamune [KAI]'
    名称 = 'Ninja KAI'

    def 城镇属性(self, 属性):
        属性.最终伤害加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'All.Atk +15%<br>'
        return temp


class 宠物6(Item):
    显示名称 = 'Petite School Friends'
    名称 = 'Petite Friends'

    def 城镇属性(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.技能等级加成('所有', 75, 75, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +100<br>'
        temp += 'Intelligence +100<br>'
        temp += 'Lv75 Passive Skill +1<br>'
        return temp


class 宠物5(Item):
    显示名称 = 'Valhalla Creature'
    名称 = 'SD Valkyrie'

    def 城镇属性(self, 属性):
        属性.力量 += 55
        属性.智力 += 55
        属性.附加伤害加成(0.05)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +55<br>'
        temp += 'Intelligence +55<br>'
        temp += 'Bonus Damage +5%<br>'
        temp += 'Increase Character Atk by +10%<br>'
        temp += '(NEED TO CHECK PET SWAP 10% 2nd Tab)<br>'
        return temp


class 宠物4(Item):
    显示名称 = 'Far Eastern Romance'
    名称 = 'Runa the Traveler'

    def 城镇属性(self, 属性):
        属性.力量 += 60
        属性.智力 += 60
        属性.物理攻击力 += 30
        属性.魔法攻击力 += 30
        属性.独立攻击力 += 30
        属性.附加伤害加成(0.05)
        属性.技能等级加成('所有', 1, 45, 1)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +60<br>'
        temp += 'Intelligence +60<br>'
        temp += 'Physical Atk +30<br>'
        temp += 'Magical Atk +30<br>'
        temp += 'Independent Atk +30<br>'
        temp += 'Bonus.Dmg 5%<br>'
        temp += 'Lv 1-45 All Skill +1<br>'
        return temp


class 宠物3(Item):
    显示名称 = 'SD Elonse [Tenacious]'
    名称 = 'SD Elonse'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.最终伤害加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +65<br>'
        temp += 'Intelligence +65<br>'
        temp += 'All.Atk +15%<br>'
        return temp


class 宠物2(Item):
    显示名称 = 'SD Elonse [Brave]'
    名称 = 'SD Elonse'

    def 城镇属性(self, 属性):
        属性.力量 += 50
        属性.智力 += 50
        属性.所有属性强化加成(20)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +50<br>'
        temp += 'Intelligence +50<br>'
        temp += 'All Ele +20<br>'
        return temp


class 宠物1(Item):
    显示名称 = 'SD Elonse & Alonse'
    名称 = 'Elonse & Alonse'

    def 城镇属性(self, 属性):
        属性.力量 += 65
        属性.智力 += 65
        属性.最终伤害加成(0.15)

    def 装备描述(self, 属性):
        temp = ''
        temp += 'Strength +65<br>'
        temp += 'Intelligence +65<br>'
        temp += 'All.Atk +15%<br>'
        temp += 'Increase Character Atk by +10%<br>'
        temp += '(NEED TO CHECK PET SWAP 10% 2nd Tab)<br>'
        return temp


class 宠物0(Item):
    显示名称 = 'None'
    名称 = 'None'

    def 城镇属性(self, 属性):
        pass

    def 触发属性(self, 属性):
        pass

    def 装备描述(self, 属性):
        temp = ''
        return temp


for i in range(len(宠物列表)):
    exec('宠物列表[{}] = 宠物{}()'.format(len(宠物列表) - i - 1, i))

宠物序号 = dict()
for i in range(len(宠物列表)):
    宠物序号[宠物列表[i].名称] = i
