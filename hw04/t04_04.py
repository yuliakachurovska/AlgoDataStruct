# На відрізку [1.6, 3] знайдіть корінь рівняння
# sin 𝑥 = 𝑥 / 3.

from math import sin

def solve(f, c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if f(m) > c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0

    return l

if __name__ == '__main__':
    a = 1.6
    b = 3
    c = 0
    print(solve(lambda x: sin(x) - (x / 3.0), c, a, b))  # 2.278862660075828