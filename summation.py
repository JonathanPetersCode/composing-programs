def summation(n):
    total, k = 0, 1
    while k <= n:
        total, k  = total + k , k + 1
    return total

def pi_sum(n):
        total, k = 0, 1
        while k <= n:
            total, k = total + 8 / ((4*k-3) * (4*k-1)), k + 1
        return total


def summation_cubed(n):
    total, k = 0, 1
    while k <= n:
        total, k = total + k ** 3, k + 1
    return total

def summation_generic(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total 


def cubed(x):
    return x ** 3 


print(summation_generic(8, cubed))



