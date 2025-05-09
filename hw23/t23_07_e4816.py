import sys
sys.setrecursionlimit(200000)

def dfs(v):
    visited[v] = True
    component.append(v)
    for u in graph[v]:
        if not visited[u]:
            dfs(u)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (n + 1)
    components = []

    for i in range(1, n + 1):
        if not visited[i]:
            component = []
            dfs(i)
            components.append(component)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(' '.join(map(str, comp)))
