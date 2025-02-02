def bsearch_leftmost(arr, x):
    left = 0
    right = len(arr)
    while left < right:
        m = left + (right - left) // 2
        if arr[m] < x:
            left = m + 1
        else:
            right = m
    return left

def bsearch_rightmost(arr, x):
    left = 0
    right = len(arr)
    while left < right:
        m = left + (right - left) // 2
        if arr[m] <= x:
            left = m + 1 
        else:
            right = m
    return left - 1

if __name__ == "__main__":
    f = open("input.txt")
    while f.readline():  
            arr1 = [int(x) for x in f.readline().split()]  
            f.readline()  
            arr2 = [int(x) for x in f.readline().split()]  
            print(arr1)
            print(arr2)
    f.close()

    for i in arr2:
        res = bsearch_rightmost(arr1, i) - bsearch_leftmost(arr1, i) + 1
        if res == -1:
            print(0)
        else:
            print(res)
