def selection_sort(times):
    n = len(times)
    for j in range(n - 1):
        pos = j
        for i in range(j + 1, n):
            if times[i] < times[pos]:
                pos = i
        times[j], times[pos] = times[pos], times[j]

if __name__ == '__main__':
    n = int(input())
    times = []
    for _ in range(n):
        times.append(tuple(map(int, input().split())))

    selection_sort(times)
    for t in times:
        print(*t)
