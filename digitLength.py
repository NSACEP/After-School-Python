
def digitLength0(n):
    return len(str(n))

def digitLength1a(n):
    # fails at n = 0
    i = 0
    while n > 0:
        n = n//10
        i = i + 1
    return i

def digitLength1b(n):
    if n == 0:
        return 1
    i = 0
    while n > 0:
        n = n//10
        i = i + 1
    return i

def digitLength2(n):
    # fails at n = 0
    from math import log10, floor
    return floor(log10(n)) + 1

def digitLength3(n):
    # fails at n = 0
    from math import log10, floor
    return 1 if n == 0 else floor(log10(n)) + 1
\