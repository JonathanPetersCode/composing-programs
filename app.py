def fibonacci(n):
    prev, curr = 0 , 1
    next_val = 2

    while next_val < n:
        prev, curr = curr, prev + curr
        next_val += 1
    return curr


# print(fibonacci(8))
# print(fibonacci(11))
# print(fibonacci(19))


def fibonacci_assert_test():
    assert fibonacci(8) == 13, "fibonacci(8) should equal 13"
    assert fibonacci(11) == 55, "fibonacci(8) should equal 55"
    assert fibonacci(19) == 2584, "fibonacci(8) should equal 2584"


print(fibonacci_assert_test())
