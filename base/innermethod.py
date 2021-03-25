def outer():
    x = 1

    def inner():
        print(x)

    return inner

x = 2
foo = outer()
foo()