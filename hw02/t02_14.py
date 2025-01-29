def a(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum  #O(n)


def b(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i
    return sum  #O(n)


def c(a, n):
    sum = 0
    for i in range(1, n + 1):
        sum += a**i
    return sum  #O(n)


#0^0 -> невизначеність, будемо починати з 1
def d(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if j == i:
                sum += j**i
    return sum  #O(n^2)
                

def e(n):   #1/(1+i)
    prod = 1
    for i in range(1, n + 1):
        prod *= 1 / (1 + i)
    return prod  #O(n)


def f(n):
    prod = 1
    k = 1
    for i in range(1, n + 1):
        k *= i
        prod *= 1 / (1 + k)
    return prod  #O(n)


def g(n, a):
    prod = 1
    k = 1 # факторіал
    v = 1 # а^i
    for i in range(1, n + 1):
        k *= i
        v *= a
        prod *= (v / (1 + k))
    return prod  #O(n)


# f1 = O(g1), f2 = O(g2) -> f1*f2 == O(g1*g2) 
def h(n, m):
    prod = 1
    v = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            v *= i
        prod *= 1 / (1 + v)
    return prod  #O(nm)


def i(n):
    prod = 1
    v = 1
    for k in range(1, n + 1):
        for j in range(1, n + 1):
            if j == k:
                v = j**k
                prod *= 1 / (1 + v)
    return prod  #O(n^2)