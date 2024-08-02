import sys
def fat(n):
    if n <= 1:
        return 1
    return n * fat(n-1)

print(fat(5))

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(5))

def mdc(a,b):
    if b <= 0:
        return a
    return mdc(b, a % b)

print(mdc(6,223))

def mmc(a, b):
    return abs(a*b) / mdc(a*b)

print(mmc(12, 9))