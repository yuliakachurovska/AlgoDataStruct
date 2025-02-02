from math import log2, floor

def cyclic_shift(n, amount_bit):
    high_bit = n >> (amount_bit-1)
    res = ((n << 1) + high_bit) & ((1 << amount_bit) - 1)
    return res

def solve(n):
    am_bit = floor(log2(n)+1)
    res = n
    for i in range(am_bit - 1):
        n = cyclic_shift(n, am_bit)
        if n > res:
            res = n
    return res

if __name__ == "__main__":
    n = int(input())
    print(solve(n))