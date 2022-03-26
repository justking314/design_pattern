from enum import Enum

BaoZiProgress = Enum("BaoZiProgress", "queued preparation ready")
BaoZiDough = Enum("BaoZiDough", "ferment unferment")
BaoZiStuffing = Enum("BaoZiStuffing", "pork beef")
BaoZiMethod = Enum("BaoZiMethod", "steam freeze")


# BaoZiDough = Enum("BaoZiDough", "发酵 死面")
# BaoZiStuffing = Enum("BaoZiStuffing", "猪肉 牛肉")
# BaoZiMethod = Enum("BaoZiMethod", "蒸熟 速冻")

class BaoZi:
    def __init__(self, name):
        self.name = name
        self.dough = None
        self.stuffing = None
        self.method = None

    def __str__(self):
        return self.name

    def prepare_dough(self, dough):
        self.dough = dough
        print(f"在为你的 {self.name} 准备 {dough.name} 面团")


class PorkBaoZiBuilder:
    def __init__(self):
        self.baozi = BaoZi("猪肉包子")
        self.progress = BaoZiProgress.queued

    def prepare_dough(self):
        self.progress = BaoZiProgress.preparation
        self.baozi.prepare_dough(BaoZiDough.ferment)

    def add_stuffing(self):
        print("往里加猪肉馅了~")
        self.baozi.stuffing = BaoZiStuffing.pork
        print("猪肉馅放好了~")

    def choose_method(self):
        print("直接给你蒸了哈~")
        self.baozi.method = BaoZiMethod.steam
        print("猪肉馅包子蒸熟了")

    def deliver(self):
        self.progress = BaoZiProgress.ready
        print("猪肉馅包子出餐了~自取还是送餐？你自取吧~")


class BeefBaoZiBuilder:
    def __init__(self):
        self.baozi = BaoZi("牛肉包子")
        self.progress = BaoZiProgress.queued

    def prepare_dough(self):
        self.progress = BaoZiProgress.preparation
        self.baozi.prepare_dough(BaoZiDough.unferment)

    def add_stuffing(self):
        print("往里加牛肉馅了~")
        self.baozi.stuffing = BaoZiStuffing.beef
        print("牛肉馅放好了~")

    def choose_method(self):
        print("牛肉馅包子只能速冻了~")
        self.baozi.method = BaoZiMethod.freeze
        print("牛肉馅包子速冻好了~")

    def deliver(self):
        self.progress = BaoZiProgress.ready
        print("牛肉包子出餐了~自取还是送餐？你自取吧~")


class Waiter:
    def __init__(self):
        self.builder = None

    def construct_baozi(self, builder):
        self.builder = builder
        [step() for step in (builder.prepare_dough, builder.add_stuffing,
                             builder.choose_method, builder.deliver)]

    @property
    def baozi(self):
        return self.builder.baozi


def validate_style(builders):
    try:
        baozi_style = input('想要什么包子？ [p]猪肉 or [b]牛肉? ')
        builder = builders[baozi_style]()
    except KeyError as err:
        print('Sorry, only margarita (key m) and creamy bacon (key c) are available')
        return (False, None)
    return (True, builder)


"""
实现的最后一部分是main()函数。main()函数实例化一个包子建造者，然后指挥者Waiter
使用包子建造者来准备包子。创建好的包子可在稍后的时间点交付给客户端。
"""


def main():
    builders = dict(p=PorkBaoZiBuilder, b=BeefBaoZiBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    print("-" * 20)
    waiter = Waiter()
    waiter.construct_baozi(builder)
    baozi = waiter.baozi
    print("-" * 20)
    print('好好吃你的 {} 吧!'.format(baozi))


if __name__ == '__main__':
    main()
