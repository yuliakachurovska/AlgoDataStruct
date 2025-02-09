from math import sqrt

def solve(f, c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if f(m) < c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0

    return l

if __name__ == '__main__':
    a = 0
    b = 10**5
    C = float(input())
    print(solve(lambda x: x**2 + sqrt(x), C, a, b))