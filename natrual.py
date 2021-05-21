from doctest import testmod, run_docstring_examples

def sum_natural(n):
    """Returns the sum of natural numbers to n

    >>> sum_natural(4)
    10

    >>> sum_natural(245)
    30135
    """
    total, curr = 0 , 1

    while curr <= n:
        total, curr = total + curr, curr + 1
    return total


# print(sum_natural(245))

def assert_sum_natural():
    assert sum_natural(4) == 10, "The sum of natural number to 4 is 10"
    assert sum_natural(7) == 28, "The sum of natural number to 4 is 28"
    assert sum_natural(10) == 55, "The sum of natural number to 4 is 10"


# print(assert_sum_natural())

print(run_docstring_examples(sum_natural, globals(), True))