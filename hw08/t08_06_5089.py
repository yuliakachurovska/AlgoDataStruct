def bubble_sort(arr, n):
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = [input() for _ in range(n)]
    res = bubble_sort(arr, n)
    for i in res:
        print(i)
