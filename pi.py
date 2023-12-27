def a(x):
    return pow(x, 2) + pow(x, 3)


def b(x):
    return x + (x * 2)


def c(x, y):
    return x + y


print(c(a(3), b(3)))


