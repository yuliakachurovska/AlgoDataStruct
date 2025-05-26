import heapq

def prim(n, graph):
    visited = [False] * n
    mst_edges = set()
    heap = []
    visited[0] = True

    for w, v in graph[0]:
        heapq.heappush(heap, (w, 0, v))

    while heap:
        w, u, v = heapq.heappop(heap)
        if visited[v]:
            continue
        visited[v] = True
        mst_edges.add((min(u, v), max(u, v)))
        for next_w, to in graph[v]:
            if not visited[to]:
                heapq.heappush(heap, (next_w, v, to))
    return mst_edges


if __name__ == "__main__":
    with open("input.txt") as f:
        t = int(f.readline())
        for _ in range(t):
            n, m, p, q = map(int, f.readline().split())
            p -= 1
            q -= 1

            graph = [[] for _ in range(n)]
            for _ in range(m):
                u, v, w = map(int, f.readline().split())
                u -= 1
                v -= 1
                graph[u].append((w, v))
                graph[v].append((w, u))

            mst = prim(n, graph)

            if (min(p, q), max(p, q)) in mst:
                print("YES")
            else:
                print("NO")