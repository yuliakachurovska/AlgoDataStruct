from collections import deque

def read_graph(inp, n, m):
    graph = {i: [] for i in range(1, n + 1)}
    indegree = {i: 0 for i in range(1, n + 1)}
    
    for _ in range(m):
        u, v = map(int, inp.readline().split())
        graph[u].append(v)
        indegree[v] += 1

    return graph, indegree

def topological_sort(graph, indegree, n):
    queue = deque()
    for node in range(1, n + 1):
        if indegree[node] == 0:
            queue.append(node)

    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    if len(order) == n:
        return order
    else:
        return [-1]

if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        graph, indegree = read_graph(inp, n, m)
        result = topological_sort(graph, indegree, n)

    print(' '.join(map(str, result)))
