def merge_sort(array):
    _merge_sort(array, 0, len(array) - 1)

def _merge_sort(array, a, b):
    if a == b:
        return

    m = a + (b - a) // 2
    _merge_sort(array, a, m)
    _merge_sort(array, m + 1, b)

    left = array[a: m + 1]
    right = array[m + 1: b + 1]
    i = 0
    j = 0
    k = a

    while i < len(left) and j < len(right):
        if left[i][0] < right[j][0]:  # Якщо лівий елемент менший записуємо його в array[k]
            array[k] = left[i]
            i += 1
        elif left[i][0] > right[j][0]:  # Якщо правий менший записуємо його в array[k]
            array[k] = right[j]
            j += 1
        else:  # Якщо рівні, то беремо елемент з лівої частини
            array[k] = left[i]
            i += 1
        k += 1

    while i < len(left):
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        array[k] = right[j]
        j += 1
        k += 1


if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    merge_sort(arr)
    for i in arr:
        print(*i)
