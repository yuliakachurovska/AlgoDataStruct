def solve(arr, a, b):
    sum = 0
    for i in arr:
        if a <= i <= b:
            sum += 1
    return sum


if __name__ == "__main__":
    f = open("input.txt")
    while f.readline():
        arr = [int(x) for x in f.readline().split()]
        a, b = [int(x) for x in f.readline().split()]
        print(solve(arr, a, b))
    f.close()
