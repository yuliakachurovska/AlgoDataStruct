# Знайдіть найменше 𝑥∈[0, 10], що
# 𝑓(𝑥) = 𝑥³ + 𝑥 + 1 > 5.

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
    b = 10
    c = 5
    print(solve(lambda x: x**3 + x + 1, c, a, b))  # 1.378796700129551