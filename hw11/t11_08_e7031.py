def merge_and_count(arr, temp, left, mid, right, t):
    i = left
    j = mid + 1
    k = left
    count = 0

    l = mid + 1
    for x in range(left, mid + 1):
        while l <= right and arr[x] > arr[l] + t:
            l += 1
        count += (l - (mid + 1))

    i, j = left, mid + 1
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right + 1):
        arr[i] = temp[i]

    return count

def solve(arr, temp, left, right, t):
    if left >= right:
        return 0
    
    mid = (left + right) // 2
    count = solve(arr, temp, left, mid, t)
    count += solve(arr, temp, mid + 1, right, t)
    count += merge_and_count(arr, temp, left, mid, right, t)
    
    return count

n, t = map(int, input().split())
arr = list(map(int, input().split()))

temp = [0] * n
result = solve(arr, temp, 0, n - 1, t)
print(result)