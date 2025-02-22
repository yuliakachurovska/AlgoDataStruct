def bubble_sort(arr, n):
    count = 0
    for i in range(n - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                count += 1 
    return count

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(bubble_sort(arr, n))