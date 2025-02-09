# На відрізку [0, 2] знайдіть корінь рівняння
# 𝑥³ + 4𝑥² + 𝑥 − 6 = 0.

def solve(f, c, a, b):
    l = a
    r = b
    m = (l + r) / 2.0
    while l != m and m != r:
        if f(m) <= c:
            l = m
        else:
            r = m
        m = (l + r) / 2.0

    return l

if __name__ == '__main__':
    a = 0
    b = 2
    c = 0
    print(solve(lambda x: x**3 + 4*x**2 + x - 6, c, a, b))  # 1.0
