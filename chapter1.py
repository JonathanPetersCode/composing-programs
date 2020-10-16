from doctest import testmod
from doctest import run_docstring_examples as run_doc_ex

#Chapter 1
# Info : Call the section number to return code from excersies (EX: 1.1)

#Chapter 1.1

#Goal create public interface, that prints important information and the completed exercises from each section in each chapter.

section1_1 = """Computer science is a tremendously broad academic discipline. The areas of globally distributed systems, artificial intelligence, robotics, graphics, security, scientific computing, computer architecture, and dozens of emerging sub-fields all expand with new techniques and discoveries every year.

These fundamental ideas have long been taught using the classic textbook Structure and Interpretation of Computer Programs(SICP) by Harold Abelson and Gerald Jay Sussman with Julie Sussman.

SICP : https://mitpress.mit.edu/sites/default/files/sicp/index.html

Creative Commons : https://creativecommons.org/licenses/by-nc-sa/3.0/deed.en_US
"""

section1_1_1 = """A language isn't something you learn so much as something you join.

—Arika Okrent

The best way to get started programming in Python is to interact with the interpreter directly. This section describes how to install Python 3, initiate an interactive session with the interpreter, and start programming."""



foo = "from urllib.request import urlopen print(str(urlopen('http://composingprograms.com/shakespeare.txt')))"

# chap_1_exercises = {
#     "section1_1": chapter1_1
# }


#Exercise 1.5.5 - Fibonacci Sequence

def fib(n):
    """Return Fibonacci sequence number of (n) length"""
    prev, curr = 0, 1
    k = 2
    while k < n:
        prev, curr = curr, prev + curr
        k = k + 1
    return curr

print("The {n}th number of the Fibonacci sequence is {fib}".format(n=12, fib=fib(12)))

#Assert Fib() Tests
def fib_test():
    assert fib(12) == 89, "The 12th Fibonacci number should be 89"
    assert fib(8) == 13, "The 8th Fibonacci number should be 13"
    assert fib(20) == 4181, "The 20th Fibonacci number should be 4181"
    assert fib(
        100) == 218922995834555169026, "The 100th Fibonacci number should be 218922995834555169026"

# #Exercise 1.5.6 - sum_naturals 
# Add Doc Tests 
# Import doctest

# Doctests. Python provides a convenient method for placing simple tests directly in the docstring of a function.

def sum_naturals(x):
    """Returns the sum of all natural numbers up to (x)
    
    Doctests
    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """

    total, z = 0, 1
    while z <= x:
        total, z = total + z, z + 1
    return total


print("The sum of natural numbers starting at {x} is {sum}".format(x=10, sum=sum_naturals(10)))


print(testmod())


# To verify the doctest interactions for only a single function, we use a doctest function called run_docstring_examples.

#run_docstring_example imported as run_doc_ex

run_doc_ex(sum_naturals, globals(), True)

#Output :
# Finding tests in NoName
# Trying:
#     sum_naturals(10)
# Expecting:
#     55
# ok
# Trying:
#     sum_naturals(100)
# Expecting:
#     5050
# ok
# None


# When writing Python in files, all doctests in a file can be run by starting Python with the doctest command line option:

# python3 -m doctest /Users/JonathanPeters/Documents/Github-Repos-Main/composing-programs/chapter1.py


def average(x, y):
 return (x + y)/2

def improve(update, close, guess=1):
 while not close(guess):
     guess = update(guess)
 return guess

def approx_eq(x, y, tolerance=1e-3):
    return abs(x - y) < tolerance

    def sqrt(a):
        def sqrt_update(x):
            return average(x, a/x)
    
        def sqrt_close(x):
            return approx_eq(x * x, a)
        return improve(sqrt_update, sqrt_close)

    result = sqrt(256)

#Calculate Square Root

def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update


def find_zero(f, df):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero)


def square_root_newton(a):
        def f(x):
            return x * x - a

        def df(x):
            return 2 * x
        return find_zero(f, df)

print(square_root_newton(64))
