def func1(x):
    return x + 100 


def func2(x):
    return 20


def compose1(f, g):
    return lambda x : f(g(x))

print(compose1(func1, func2))

