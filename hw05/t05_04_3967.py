def find_max_length(n, k, array):
    """Знаходить максимальну довжину шматків мотузки, яку можна нарізати. 
    
    :param n: Кількість білизняних мотузок (1 ≤ n ≤ 10001).
    :param k: Кількість будиночків  (1 ≤ k ≤ 10001).
    :param array: Не відсортований масив довжин наявних мотузок у сантиметрах (1 ≤ array[i] ≤ 10^7).
    :return: Максимальна довжина мотузки, яку можна нарізати, 
        або 0, якщо довжини не вистачить на k відрізків довжини 1. 
    """
    left = 1
    right = max(array)

    while left <= right:
        m = left + (right - left) // 2
        sum = 0
        for i in array:
            sum += i // m
        
        if sum >= k:  # 5 7
            left = m + 1
        else:
            right = m - 1

    return right

if __name__ == '__main__':
    n, k = [int(i) for i in input().split()]
    arr = [int(input()) for _ in range(n)]
    print(find_max_length(n, k, arr))
