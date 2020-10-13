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
        print(curr)
        k = k + 1
    return curr

print(fib(8))