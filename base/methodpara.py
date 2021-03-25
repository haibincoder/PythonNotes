def log(func):
    def wrapper(*arg, **kw):
        print("call medthod:",func.__name__)
        return func(*arg, **kw)
    return wrapper

@log
def method1(a, b, c):
    print(type(a))
    print(a)
    print(b)
    print(c)

@log
def method2(a, b, c=10):
    print(type(a))
    print(a)
    print(b)
    print(c)

@log
def method3(*arg):
    print(arg)

@log
def method4(**arg):
    print(method4)
    print(arg)

@log
def method5(*arg, **arg2):
    print("arg:", arg)
    print("arg2", arg2)


method1(10, c=30, b=20)
method2(10, 20, 30)
method2(10, 20)

arg = (1,2,3,4)
method3(arg)
dic = {'a': 1, 'b':2, 'c':3}
method4(**dic)
method5((1, 2, 3, 4), **dic)

class method6:
    item = 1
    def __init__(self):
        self.items = [1,2,3,]
    @classmethod
    def getvalue(cls):
        print(cls.__name__)   # print:
        print(cls.item)

    @staticmethod
    def getstaticvalue():
        # print(item)
        return

method6.getvalue()