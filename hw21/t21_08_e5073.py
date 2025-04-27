def solve(lst):
    t1 = [tuple(sublist) for sublist in lst]
    set_t1 = set(t1)
    return len(set_t1) == len(lst)

if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = []
    for _ in range(m):
        u, v = map(int, input().split())
        lst.append([u, v])
    if solve(lst):
        print("NO")
    else:
        print("YES")