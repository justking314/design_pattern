# coding:utf-8

class Bee:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f"{self} see {obstacle} and {obstacle.action()}")


class Flower:
    def __str__(self):
        return "a flower"

    def action(self):
        return "make honey"


class BeeWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t-------Bee World--------"

    def make_character(self):
        return Bee(self.player_name)

    def make_action(self):
        return Flower()


class DNF:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def interact_with(self, obstacle):
        print(f"{self} against {obstacle} and {obstacle.action()}")


class BadMan:
    def __str__(self):
        return "a bad man"

    def action(self):
        return "kill him"


class DNFWorld:
    def __init__(self, name):
        print(self)
        self.player_name = name

    def __str__(self):
        return "\n\n\t-------DNF World--------"

    def make_character(self):
        return DNF(self.player_name)

    def make_action(self):
        return BadMan()


class GameEnv:
    def __init__(self, factory):
        self.hero = factory.make_character()
        self.obstacle = factory.make_action()

    def play(self):
        self.hero.interact_with(self.obstacle)


def validate_age(name):
    try:
        age = input(f"welcome {name}. how old are you?")
        age = int(age)
    except ValueError as e:
        print(f"age {age} error!")
        return False, age
    return True, age


def main():
    name = input("请输入用户名：")
    valid_input = False
    while not valid_input:
        valid_input, age = validate_age(name)
    game = BeeWorld if age < 18 else DNFWorld
    environment = GameEnv(game(name))
    environment.play()


if __name__ == '__main__':
    main()
