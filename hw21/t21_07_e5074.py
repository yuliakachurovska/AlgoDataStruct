def solve(lst, n):
    InVert = {i: 0 for i in range(1, n + 1)}
    OutVert = {i: 0 for i in range(1, n + 1)}
    for i in lst:
        u, v = i
        InVert[v] += 1
        OutVert[u] += 1
    return InVert, OutVert


if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        u, v = map(int, input().split())
        lst.append([u, v])
    solve(lst, n)
    in_degree, out_degree = solve(lst, n)
    for i in range(1, n + 1):
        print(in_degree[i] + out_degree[i])