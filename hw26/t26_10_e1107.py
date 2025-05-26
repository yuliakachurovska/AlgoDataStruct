import sys
sys.setrecursionlimit(10000)

def find(u, parent):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

def union(u, v, parent):
    u_root = find(u, parent)
    v_root = find(v, parent)
    if u_root == v_root:
        return False
    parent[v_root] = u_root
    return True

def dfs(u, p, d, g, depth, par, max_edge):
    depth[u] = d
    for v, w in g[u]:
        if v != p:
            par[v][0] = u
            max_edge[v][0] = w
            dfs(v, u, d + 1, g, depth, par, max_edge)

def build_lca(n, par, max_edge):
    for k in range(1, 17):
        for v in range(n):
            if par[v][k - 1] != -1:
                par[v][k] = par[par[v][k - 1]][k - 1]
                max_edge[v][k] = max(max_edge[v][k - 1], max_edge[par[v][k - 1]][k - 1])

def get_max_edge(u, v, depth, par, max_edge):
    res = 0
    if depth[u] < depth[v]:
        u, v = v, u
    for k in reversed(range(17)):
        if par[u][k] != -1 and depth[par[u][k]] >= depth[v]:
            res = max(res, max_edge[u][k])
            u = par[u][k]
    if u == v:
        return res
    for k in reversed(range(17)):
        if par[u][k] != -1 and par[u][k] != par[v][k]:
            res = max(res, max_edge[u][k], max_edge[v][k])
            u = par[u][k]
            v = par[v][k]
    return max(res, max_edge[u][0], max_edge[v][0])

if __name__ == "__main__":
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((w, u - 1, v - 1))

    edges.sort()
    parent = list(range(n))
    mst = []
    total_cost = 0
    graph = [[] for _ in range(n)]

    for w, u, v in edges:
        if union(u, v, parent):
            total_cost += w
            mst.append((u, v, w))
            graph[u].append((v, w))
            graph[v].append((u, w))

    depth = [0] * n
    par = [[-1] * 17 for _ in range(n)]
    max_edge = [[0] * 17 for _ in range(n)]
    dfs(0, -1, 0, graph, depth, par, max_edge)
    build_lca(n, par, max_edge)

    s2 = float('inf')
    mst_set = set((min(u, v), max(u, v), w) for u, v, w in mst)

    for w, u, v in edges:
        if (min(u, v), max(u, v), w) not in mst_set:
            max_in_path = get_max_edge(u, v, depth, par, max_edge)
            if max_in_path != w:
                s2 = min(s2, total_cost - max_in_path + w)

    if s2 == float('inf'):
        s2 = total_cost

    print(total_cost, s2)