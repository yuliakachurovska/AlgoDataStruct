def solve(arr, numb):
    left = 0
    right = len(arr)
    while left < right:
        m = left + (right - left) // 2
        if arr[m] < numb:
            left = m + 1
        elif arr[m] > numb:
            right = m
        else:
            return True
    return False

if __name__ == "__main__":
    f = open("input.txt")
    while f.readline():  
            arr1 = [int(x) for x in f.readline().split()]  
            f.readline()  
            arr2 = [int(x) for x in f.readline().split()]  
    f.close()

    for i in arr2:
        if solve(arr1, i):
            print("YES")
        else:
             print("NO")

