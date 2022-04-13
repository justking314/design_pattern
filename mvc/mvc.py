# coding:utf-8

note = ["螽斯羽，诜诜兮。宜尔子孙，振振兮",
        "天接云涛连晓雾，星河欲转千帆舞",
        "噫吁戏，危乎高哉",
        "人成各，今非昨，病魂常似秋千索",
        "枯藤老树昏鸦，小桥流水人家",
        "山一程，水一程，身向榆关那畔行。故园无此声",
        "说什么黄泉无店宿忠魂，争道这青山有幸埋芳洁"
        ]


class NoteModel:
    def get_note(self, n):
        try:
            v = note[n]
        except IndexError:
            v = "没有找到"
        return v


class View:
    def show(self, n):
        print(f"句子是：{n}")

    def error(self, msg):
        print(f"Error:{msg}")

    def select(self):
        return input("请输入索引:")


class Controller:
    def __init__(self):
        self.model = NoteModel()
        self.view = View()

    def run(self):
        tag = False
        while not tag:
            try:
                n = self.view.select()
                n = int(n)
                tag = True
            except ValueError:
                self.view.error("错误的索引")
        user_note = self.model.get_note(n)
        self.view.show(user_note)


if __name__ == '__main__':
    c = Controller()
    while 1:
        c.run()
