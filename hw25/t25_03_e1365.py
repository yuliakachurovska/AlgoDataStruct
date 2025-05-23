import heapq

def dijkstra(graph, start, n):
    distances = [float('inf')] * n
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances

def matrix_to_graph(matrix):
    n = len(matrix)
    graph = {i: {} for i in range(n)}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != -1 and i != j:
                graph[i][j] = matrix[i][j]
    return graph

if __name__ == "__main__":
    n, s, f = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    graph = matrix_to_graph(matrix)
    distances = dijkstra(graph, s - 1, n)
    result = distances[f - 1]
    print(result if result != float('inf') else -1)
