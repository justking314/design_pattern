# coding:utf-8

from enum import Enum
from abc import ABCMeta, abstractmethod

State = Enum("State", "new running sleep restart zombie")

class Server(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self):
        pass
    def __str__(self):
        return self.name
    @abstractmethodgit

    def boot(self):
        pass

    @abstractmethod
    def kill(self, restart=True):
        pass

class FileServer(Server):
    def __init__(self):
        self.name = "文件服务"
        self.state = State.new
    def boot(self):
        print(f"正在启动 {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"正在杀死 {self}")
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name):
        print(f"正在为{user}尝试创建文件{name}")


class NetServer(Server):
    def __init__(self):
        self.name = "网络服务"
        self.state = State.new

    def boot(self):
        print(f"正在启动 {self}")
        self.state = State.running

    def kill(self, restart=True):
        print(f"正在杀死 {self}")
        self.state = State.restart if restart else State.zombie

    def change_net(self, user, net):
        print(f"正在为用户{user}切换为{net}网络")

class OperatingSystem:
    """外观"""
    def __init__(self):
        self.ns = NetServer()
        self.fs = FileServer()

    def start(self):
        [i.boot() for i in (self.fs,self.ns)]

    def create_file(self, user, name):
        return self.fs.create_file(user, name)

    def change_net(self, user, net):
        return self.ns.change_net(user,net)

def main():
    o = OperatingSystem()
    o.start()
    o.create_file("管理员", "月统计报表")
    o.change_net("用户a", "移动")

if __name__ == '__main__':
    main()


