import random

lists = [[1,2],[2,3,4],[5,6,7]]
lists2 = [[i for i in range(random.randint(1,100000))] for j in range(1000)]
from time import time


def time_costing(func):
    def core():
        start = time()
        ret = func()
        result = 'number: ' + str(ret) + ' time costing: ' + str(time() - start)
        # print(result)
    return core


@time_costing
def run():
    number = 0
    for i in range(1, 101):
        number += i
    return number


run()

@time_costing
def demo1():
    print(sum(lists2,[]))

@time_costing
def demo2():
    ret = []
    for i in lists2:
        ret.extend(i)
    print(ret)


if __name__ == '__main__':
    demo1()
    demo2()