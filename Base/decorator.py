import datetime


def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper

@log
def date():
    print(datetime.datetime.now().strftime('%y/%m/%d %H:%M:%S'))

date()