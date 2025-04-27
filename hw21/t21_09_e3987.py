def solve(lst, n):
    edges = dict()
    for u, v in lst:
        if u not in edges:
            edges[u] = set()
        if v not in edges:
            edges[v] = set()
        edges[u].add(v)
        edges[v].add(u)

    for i in range(1, n+1):
        if i not in edges or len(edges[i]) != n-1:
            return False
    return True

if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        u, v = map(int, input().split())
        lst.append((u, v))
    if solve(lst, n):
        print("YES")
    else:
        print("NO")
