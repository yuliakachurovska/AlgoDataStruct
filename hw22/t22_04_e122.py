def solve(graph, curr, target, d, visited):
    if d < 0:
        return 0
    if curr == target:
        return 1

    count = 0
    visited.add(curr)

    for neighbor in graph[curr]:
        if neighbor not in visited:
            count += solve(graph, neighbor, target, d - 1, visited)

    visited.remove(curr)
    return count

if __name__ == '__main__':
    n, k, a, b, d = map(int, input().split())
    graph = {i: [] for i in range(1, n + 1)}
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u].append(v)

    result = solve(graph, a, b, d, set())
    print(result)
