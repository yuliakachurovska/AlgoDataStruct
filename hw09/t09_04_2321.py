def qsort(array):
    _qsort(array, 0, len(array) - 1)

def _qsort(array, a, b):
    if a >= b:
        return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
            left += 1
        while pivot < array[right]:
            right -= 1
        if left >= right:
            break
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    _qsort(array, a, right)
    _qsort(array, right + 1, b)

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    arr = [int(x) for x in arr]
    qsort(arr)
    print(*arr)
