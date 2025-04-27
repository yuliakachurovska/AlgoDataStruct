def solve(matrix, n):
    res = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
        if count == 1:
            res += 1
    return res


if __name__ == '__main__':
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    res = solve(matrix, n)
    print(res)