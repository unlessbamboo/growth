x = 10


def f1():
    print(x)


def f2(func):
    x = 20
    func()


f2(f1)
