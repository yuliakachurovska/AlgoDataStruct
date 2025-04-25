import math

class SegmentTree:
    def __init__(self, array):
        k = len(array)
        n = 1 << (k - 1).bit_length()
        self.size = n
        self.tree = [0] * (2 * n)
        for i in range(k):
            self.tree[n + i] = array[i]
        for i in range(n - 1, 0, -1):
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])

    def query_gcd(self, l, r):
        l += self.size
        r += self.size
        res = 0
        while l <= r:
            if l % 2 == 1:
                res = math.gcd(res, self.tree[l])
                l += 1
            if r % 2 == 0:
                res = math.gcd(res, self.tree[r])
                r -= 1
            l //= 2
            r //= 2
        return res

    def update(self, i, x):
        i += self.size
        self.tree[i] = x
        i //= 2
        while i >= 1:
            self.tree[i] = math.gcd(self.tree[2 * i], self.tree[2 * i + 1])
            i //= 2


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    tree = SegmentTree(arr)

    for _ in range(m):
        parts = list(map(int, input().split()))
        q, l, r = parts
        if q == 1:
            print(tree.query_gcd(l - 1, r - 1))
        elif q == 2:
            tree.update(l - 1, r)
