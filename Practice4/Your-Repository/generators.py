#1
"""
def squares(n):
    for i in range(n + 1):
        yield i * i


n = int(input("N: "))
for x in squares(n):
    print(x)
"""
#2
"""

"""
#3
"""

"""
#4
"""
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i


a = int(input("a: "))
b = int(input("b: "))

for x in squares_range(a, b):
    print(x)
"""
#5
"""
def countdown(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("n: "))
for x in countdown(n):
    print(x)
"""