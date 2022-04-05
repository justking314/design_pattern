# coding:utf-8

class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"player name: {self.name}"

    def play(self):
        return "player is playing"


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"computer name: {self.name}"

    def execute(self):
        return 'executes a program'


class Cook:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"cook name: {self.name}"

    def cook(self):
        return "厨师正在做菜"


class Adapter:
    def __init__(self, obj, adapter_methods):
        self.obj = obj
        self.__dict__.update(adapter_methods)

    def __str__(self):
        return str(self.obj)

    @property
    def name(self):
        return self.obj.name


def main():
    objs = [Player("苏神")]
    c_obj = Computer("联想")
    objs.append(Adapter(c_obj, dict(play=c_obj.execute)))
    cook_obj = Cook("范厨师")
    objs.append(Adapter(cook_obj, dict(play=cook_obj.cook)))
    for i in objs:
        print(i.play())
        print(i.name)


if __name__ == '__main__':
    main()
