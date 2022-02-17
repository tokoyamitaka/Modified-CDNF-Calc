# 选项设置属性部分  0-6默认勾选


class 选项设置0():
    名称 = 'Undiluted STR'

    def 适用效果(self, 属性):
        属性.进图力量 += 175


class 选项设置1():
    名称 = 'Undiluted INT'

    def 适用效果(self, 属性):
        属性.进图智力 += 175


class 选项设置2():
    名称 = 'Warlord`s Cry'

    def 适用效果(self, 属性):
        属性.斗神之吼秘药 = True


class 选项设置3():
    名称 = 'Mind Stim'

    def 适用效果(self, 属性):
        属性.技能冷却缩减(1, 100, 0.20)

class 选项设置4():
    名称 = 'Title Trigger'

    def 适用效果(self, 属性):
        属性.称号触发 = True
        
class 选项设置5():
    名称 = 'CDNF'

    def 适用效果(self, 属性):
        属性.进图属强 += 0

class 选项设置6():
    名称 = 'CDNF'

    def 适用效果(self, 属性):
        属性.进图属强 += 0        

class 选项设置7():
    名称 = '[Adventure]Ele Pot'

    def 适用效果(self, 属性):
        属性.进图属强 += 10


class 选项设置8():
    名称 = 'Pet Swap (10%)'

    def 适用效果(self, 属性):
        属性.年宠技能 = True


class 选项设置9():
    名称 = 'Marbas (20%)'

    def 适用效果(self, 属性):
        属性.白兔子技能 = True


选项设置列表 = ()
for i in range(10):
    exec('选项设置列表 += (选项设置' + str(i) + '(),)')

选项设置序号 = dict()
for i in range(len(选项设置列表)):
    选项设置序号[选项设置列表[i].名称] = i
