def sequences(lst: list, n, t):
    if len(lst) == t:
        print(*lst)
        return

    for i in range(1, n + 1):
        if i not in lst:
            lst_next = lst[:]
            lst_next.append(i)
            sequences(lst_next, n, t)

if __name__ == '__main__':
    n, k = map(int, input().split())
    sequences([], n, k)