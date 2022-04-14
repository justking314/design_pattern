# coding:utf-8

class Inner:
    def __init__(self):
        self.users = ["张三", "李四"]

    def read(self):
        print(f'用户列表：{", ".join(self.users)}')

    def add(self, user):
        self.users.append(user)
        print("添加用户成功")


class Proxy:
    def __init__(self):
        self.protected = Inner()
        self.pwd = "123"

    def read(self):
        self.protected.read()

    def add(self, user):
        pwd = input("请输入密码:")
        self.protected.add(user) if pwd == self.pwd else print("密码错误")


def main():
    p = Proxy()
    while True:
        print("选择功能：1 读取； 2 添加用户； 3 退出")
        key = input("请输入序号：")
        if key == '1':
            p.read()
        elif key == '2':
            name = input("请输入要添加的用户名：")
            p.add(name)
        elif key == '3':
            break
        else:
            print("错误的序号")


if __name__ == '__main__':
    main()
