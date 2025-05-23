import heapq
import sys

INF = sys.maxsize
graph = []

def getWay(start, end):
    n = len(graph)
    distances = [INF] * n
    distances[start] = 0
    sources = [-1] * n
    visited = [False] * n

    heap = [(0, start)]

    while heap:
        cur_dist, u = heapq.heappop(heap)

        if visited[u]:
            continue
        visited[u] = True

        if u == end:
            break

        for v, weight in graph[u].items():
            if distances[v] > cur_dist + weight:
                distances[v] = cur_dist + weight
                sources[v] = u
                heapq.heappush(heap, (distances[v], v))
    else:
        return []

    path = []
    v = end
    while v != -1:
        path.append(v)
        v = sources[v]
    path.reverse()
    return path


if __name__ == '__main__':
    n, m = map(int, input().split())
    s, f = map(int, input().split())
    s -= 1
    f -= 1

    graph = [{} for _ in range(n)]

    for _ in range(m):
        b, e, w = map(int, input().split())
        b -= 1
        e -= 1
        graph[b][e] = w
        graph[e][b] = w

    path = getWay(s, f)
    if not path:
        print(-1)
    else:
        dist = 0
        for i in range(len(path) - 1):
            dist += graph[path[i]][path[i+1]]

        print(dist)
        print(" ".join(str(v + 1) for v in path))
