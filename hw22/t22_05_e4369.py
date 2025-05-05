from collections import deque

def bfs(n, graph, sources):
    time = [-1] * (n + 1)
    queue = deque()

    for source in sources:
        time[source] = 0
        queue.append(source)

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if time[neighbor] == -1:
                time[neighbor] = time[node] + 1
                queue.append(neighbor)

    return time

def solve(n, graph, sources):
    time = bfs(n, graph, sources)
    max_time = max(time[1:])
    latest_vert = [i for i, t in enumerate(time[1:], 1) if t == max_time]
    return max_time, min(latest_vert)

if __name__ == "__main__":
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    k = int(input())
    sources = list(map(int, input().split()))

    sec, vert = solve(n, graph, sources)

    print(sec)
    print(vert)
