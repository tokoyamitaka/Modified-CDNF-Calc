##选项设置属性部分  0-6默认勾选

class 选项设置0():
    名称 = '顶级力量灵药'
    def 适用效果(self, 属性):
        属性.进图力量+=175

class 选项设置1():
    名称 = '顶级智力灵药'
    def 适用效果(self, 属性):
        属性.进图智力+=175

class 选项设置2():
    名称 = '斗神之吼秘药'
    def 适用效果(self, 属性):
        属性.斗神之吼秘药 = True

class 选项设置3():
    名称 = '赛丽亚的特调酷饮'
    def 适用效果(self, 属性):
        属性.进图属强 += 5

class 选项设置4():
    名称 = '魔界战力释放秘药'
    def 适用效果(self, 属性):
        属性.进图力量+=150
        属性.进图智力+=150

class 选项设置5():
    名称 = '宠物次数适用(10%)'
    def 适用效果(self, 属性):
        属性.年宠技能 = True

class 选项设置6():
    名称 = '称号效果触发'
    def 适用效果(self, 属性):
        属性.称号触发 = True

class 选项设置7():
    名称 = '精神刺激灵药'
    def 适用效果(self, 属性):
        属性.技能冷却缩减(1,100,0.20)

class 选项设置8():
    名称 = '虚祖皇家能量秘药'
    def 适用效果(self, 属性):
        属性.进图力量+=100
        属性.进图智力+=100
        属性.进图属强 += 5

class 选项设置9():
    名称 = '武者的精神秘药'
    def 适用效果(self, 属性):
        属性.加算冷却缩减 += 0.30

class 选项设置10():
    名称 = '黄金羊毛'
    def 适用效果(self, 属性):
        属性.进图力量+=60
        属性.进图智力+=60

class 选项设置11():
    名称 = '白兔子(20%全程)'
    def 适用效果(self, 属性):
        属性.白兔子技能 = True

class 选项设置12():
    名称 = '雷米迪亚蛋糕'
    def 适用效果(self, 属性):
        属性.百分比力智+=0.20

class 选项设置13():
    名称 = '特权网吧BUFF'
    def 适用效果(self, 属性):
        属性.力量 += 100
        属性.智力 += 100
        属性.技能等级加成('所有',1,85,1)
        属性.加算冷却缩减 += 0.10

class 选项设置14():
    名称 = '系统奶BUFF'
    def 适用效果(self, 属性):
        属性.系统奶 = True

class 选项设置15():
    名称 = '奶系BUFF(6W/3K)'
    def 适用效果(self, 属性):
        属性.进图力量 += 60000
        属性.进图智力 += 60000
        属性.进图物理攻击力 += 3000
        属性.进图魔法攻击力 += 3000
        属性.进图独立攻击力 += 3000  

class 选项设置16():
    名称 = '战术之王'
    def 适用效果(self, 属性):
        属性.进图力量 += 620
        属性.进图智力 += 620
        属性.进图物理攻击力 += 80
        属性.进图魔法攻击力 += 80
        属性.进图独立攻击力 += 80  
        属性.进图属强 += 20        
        属性.战术技能BUFF = True

class 选项设置17():
    名称 = '兵法全套(10+改造)'
    def 适用效果(self, 属性):
        #兵法之神
        属性.兵法技攻BUFF = True
        #流逝轮回的记忆
        属性.百分比减防 += 0.02  #5% BOSS减半向下取整 
        if not 属性.战术技能BUFF:
            属性.进图力量 += 100
            属性.进图智力 += 100
        #无相轮回的希望
        属性.进图属强 += 10 
        if not 属性.战术技能BUFF:
            属性.进图物理攻击力 += 50
            属性.进图魔法攻击力 += 50
            属性.进图独立攻击力 += 50
            属性.进图属强 += 10  

class 选项设置18():
    名称 = '鲜红血纹'
    def 适用效果(self, 属性):
        属性.百分比三攻 += 0.15

class 选项设置19():
    名称 = '先贤的馈赠'
    def 适用效果(self, 属性):
        if not 属性.兵法技攻BUFF:
            属性.技能攻击力加成(0.05)

class 选项设置20():
    名称 = '未三觉希洛克buff'
    def 适用效果(self, 属性):
        属性.希洛克BUFF = True

class 选项设置21():
    名称 = '屏蔽三觉'
    def 适用效果(self, 属性):
        属性.屏蔽三觉 = True

选项设置列表 = []
for i in range(22):
    exec('选项设置列表.append(选项设置'+str(i)+'())')

选项设置序号 = dict()
for i in range(len(选项设置列表)):
    选项设置序号[选项设置列表[i].名称] = i
