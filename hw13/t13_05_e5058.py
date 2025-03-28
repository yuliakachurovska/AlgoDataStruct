BRACKETS = {"(": ")", "[": "]", "{": "}"}

def check(sequence: str) -> bool:
    stack = []
    for bracket in sequence:
        if bracket in BRACKETS:
            stack.append(bracket)
        elif len(stack) == 0 or BRACKETS[stack.pop()] != bracket:
            return False

    return len(stack) == 0


if __name__ == '__main__':
    n = input()
    if check(n):
        print("yes")
    else:
        print("no")
