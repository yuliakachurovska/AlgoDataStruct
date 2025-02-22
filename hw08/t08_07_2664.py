def insertion_sort(array, n):
    flag = True

    for i in range(1, n):
        pos = i
        current = array[pos]

        while pos > 0 and array[pos - 1] > current:
            array[pos] = array[pos - 1]
            pos -= 1
        array[pos] = current

        if pos != i:
            flag = False
            print(*array)

    if flag:
        return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr, n)
