# coding:utf-8
import functools

def memo(f):
    a = dict()

    def inner(*args):
        if args not in a:
            a[args] = f(*args)
        return a[args]
    return inner

@memo
def fib(n):
    assert(n >=0), "n要大于等于0"
    return n if n in [0,1] else fib(n-1) + fib(n-2)

if __name__ == '__main__':
    from timeit import Timer
    t = Timer("fib(10)", "from  __main__ import fib")
    print(t.timeit())

