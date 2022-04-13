# coding:utf-8
import random


class Tree:
    objs = dict()

    def __new__(cls, tree_type):
        obj = cls.objs.get(tree_type)
        if not obj:
            obj = object.__new__(cls)
            cls.objs[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age):
        print(f"树木：{self.tree_type} 的年龄是 {age}")


def main():
    for _ in range(3):
        t1 = Tree("苹果树")
        t1.render(random.randint(1, 10))
    for _ in range(3):
        t2 = Tree("橘子树")
        t2.render(random.randint(1, 10))

    print(f"实际创建了{len(Tree.objs)}棵树")


if __name__ == '__main__':
    main()
