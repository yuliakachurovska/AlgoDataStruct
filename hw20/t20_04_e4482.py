import math

INF = 10**18  # обмеження для LCM

class SegmentTree:
    def __init__(self, array):
        self.n = len(array)
        size = 1 << (self.n - 1).bit_length()
        self.size = size
        self.tree_gcd = [0] * (2 * size)
        self.tree_lcm = [1] * (2 * size)
        for i in range(self.n):
            self.tree_gcd[size + i] = array[i]
            self.tree_lcm[size + i] = array[i]
        for i in range(size - 1, 0, -1):
            self.tree_gcd[i] = math.gcd(self.tree_gcd[2 * i], self.tree_gcd[2 * i + 1])
            self.tree_lcm[i] = self.safe_lcm(self.tree_lcm[2 * i], self.tree_lcm[2 * i + 1])

    def safe_lcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        g = math.gcd(a, b)
        # перевірка на переповнення
        if a // g > INF // b:
            return INF
        return a // g * b

    def query_gcd(self, l, r):
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res = math.gcd(res, self.tree_gcd[l])
                l += 1
            if r % 2 == 0:
                res = math.gcd(res, self.tree_gcd[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    def query_lcm(self, l, r):
        l += self.size
        r += self.size
        res = 1
        while l <= r:
            if l % 2 == 1:
                res = self.safe_lcm(res, self.tree_lcm[l])
                l += 1
            if r % 2 == 0:
                res = self.safe_lcm(res, self.tree_lcm[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    def update(self, i, x):
        i += self.size
        self.tree_gcd[i] = x
        self.tree_lcm[i] = x
        i //= 2
        while i >= 1:
            self.tree_gcd[i] = math.gcd(self.tree_gcd[2 * i], self.tree_gcd[2 * i + 1])
            self.tree_lcm[i] = self.safe_lcm(self.tree_lcm[2 * i], self.tree_lcm[2 * i + 1])
            i //= 2


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    tree = SegmentTree(arr)

    for _ in range(m):
        parts = list(map(int, input().split()))
        q, l, r = parts
        l -= 1
        if q == 1:
            gcd_val = tree.query_gcd(l, r - 1)
            lcm_val = tree.query_lcm(l, r - 1)
            if gcd_val < lcm_val:
                print("wins")
            elif gcd_val > lcm_val:
                print("loser")
            else:
                print("draw")
        elif q == 2:
            tree.update(l, r)
