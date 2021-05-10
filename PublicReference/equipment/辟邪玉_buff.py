# 辟邪玉属性部分


class 辟邪玉():
    名称 = ''
    最小值 = -5
    最大值 = 5
    间隔 = 0.1
    当前值 = 0

    def 穿戴属性(self, 属性):
        pass


class 辟邪玉0(辟邪玉):
    名称 = '无'
    最小值 = 0
    最大值 = 0


class 辟邪玉1(辟邪玉):
    名称 = 'BUFF三攻增加'
    最小值 = -5
    最大值 = 5
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.BUFF物攻 += self.当前值
        属性.BUFF魔攻 += self.当前值
        属性.BUFF独立 += self.当前值
        pass


class 辟邪玉2(辟邪玉):
    名称 = 'BUFF三攻增加量增加'

    def 穿戴属性(self, 属性):
        属性.BUFF物攻per += self.当前值 / 100
        属性.BUFF魔攻per += self.当前值 / 100
        属性.BUFF独立per += self.当前值 / 100


class 辟邪玉3(辟邪玉):
    名称 = 'BUFF力智增加'
    最小值 = -25
    最大值 = 25
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.BUFF力量 += self.当前值
        属性.BUFF智力 += self.当前值


class 辟邪玉4(辟邪玉):
    名称 = 'BUFF力智增加量增加'

    def 穿戴属性(self, 属性):
        属性.BUFF力量per += self.当前值 / 100
        属性.BUFF智力per += self.当前值 / 100


class 辟邪玉5(辟邪玉):
    名称 = '一觉力智增加'
    最小值 = -100
    最大值 = 100
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.一觉力智 += self.当前值


class 辟邪玉6(辟邪玉):
    名称 = '一觉力智增加量增加'

    def 穿戴属性(self, 属性):
        属性.一觉力智per += self.当前值 / 100


class 辟邪玉7(辟邪玉):
    名称 = '10~15技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 10, 15, self.当前值)
        pass


class 辟邪玉8(辟邪玉):
    名称 = '20~25技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 20, 25, self.当前值)
        pass


class 辟邪玉9(辟邪玉):
    名称 = '30~35技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 30, 35, self.当前值)
        pass


class 辟邪玉10(辟邪玉):
    名称 = '40~45技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 40, 45, self.当前值)
        pass


class 辟邪玉11(辟邪玉):
    名称 = '55~60技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 55, 60, self.当前值)
        pass


class 辟邪玉12(辟邪玉):
    名称 = '65~70技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 65, 70, self.当前值)
        pass


class 辟邪玉13(辟邪玉):
    名称 = '75~80技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 75, 80, self.当前值)
        pass


class 辟邪玉14(辟邪玉):
    名称 = '1次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 50, 50, self.当前值)
        pass


class 辟邪玉15(辟邪玉):
    名称 = '2次觉醒技能Lv增加'
    最小值 = 1
    最大值 = 1
    间隔 = 1

    def 穿戴属性(self, 属性):
        属性.技能等级加成('所有', 85, 85, self.当前值)
        pass


辟邪玉列表 = ()
for i in range(16):
    exec('辟邪玉列表 += (辟邪玉' + str(i) + '(),)')

辟邪玉序号 = dict()
for i in range(len(辟邪玉列表)):
    辟邪玉序号[辟邪玉列表[i].名称] = i
