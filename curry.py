from pow import curried_pow

def curry2(f):
    def g(x):
        def h(x):
            return f(x,y)
        return h
    return g

