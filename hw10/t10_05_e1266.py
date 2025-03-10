def solve(nums, MaxTime):
    global best_score
    best_score = 0
    _solve(nums, 0, 0, MaxTime)
    return best_score


def _solve(nums: list, score, index, MaxTime):
    global best_score

    if score > MaxTime:
        return
    
    if score > best_score:
        best_score = score
    
    if best_score == MaxTime:
        return

    for i in range(index, len(nums)):
        _solve(nums, score + nums[i], i + 1, MaxTime)


if __name__ == '__main__':
    with open("input.txt") as f:
        for line in f:
            a = [int(x) for x in line.split()]
            MaxTime = a[0]
            nums = a[2:]
            result = solve(nums, MaxTime)
            print(f"sum:{result}")
