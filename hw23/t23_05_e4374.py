def read_graph(inp, n_edges):
    graph = {i: [] for i in range(1, n + 1)}
    edge_map = {}

    for edge_id in range(1, n_edges + 1):
        u, v = map(int, inp.readline().split())
        graph[u].append((v, edge_id))
        graph[v].append((u, edge_id))
        edge_map[edge_id] = (u, v)

    return graph, edge_map

def read_queries(inp, k):
    queries = []
    for _ in range(k):
        parts = list(map(int, inp.readline().split()))
        queries.append(parts[1:])
    return queries

def dfs(graph, node, visited, b_edges):
    visited[node] = True
    for neighbor, edge_id in graph[node]:
        if edge_id in b_edges:
            continue
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, b_edges)

def solve(graph, b_edges, n):
    visited = {i: False for i in range(1, n + 1)}
    dfs(graph, 1, visited, b_edges)
    return all(visited.values())

if __name__ == "__main__":
    with open("input.txt") as inp:
        n, m = map(int, inp.readline().split())
        graph, edge_map = read_graph(inp, m)
        k = int(inp.readline())
        queries = read_queries(inp, k)

    for edge_ids in queries:
        ban = set(edge_ids)
        if solve(graph, ban, n):
            print("Connected")
        else:
            print("Disconnected")
