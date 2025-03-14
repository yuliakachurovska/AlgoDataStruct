import sys
sys.set_int_max_str_digits(100000)

def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    half_n = n // 2

    x_l = x // 10**half_n
    x_r = x % 10**half_n
    y_l = y // 10**half_n
    y_r = y % 10**half_n

    Res1 = karatsuba(x_l, y_l)
    Res2 = karatsuba(x_r, y_r)
    Res3 = karatsuba(x_l + x_r, y_l + y_r)

    return (10**(2 * half_n) * Res1) + (10**half_n * (Res3 - Res1 - Res2)) + Res2


x, y = map(int, input().split())
result = karatsuba(x, y)
print(result)
