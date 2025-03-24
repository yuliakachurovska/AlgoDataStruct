class Stack:
    def __init__(self, maxsize=1000):
        self._items = [0 for _ in range(maxsize)]
        self._top = -1

    def push(self, n):
        self._top += 1
        self._items[self._top] = n

    def pop(self):
        if self.empty():
            return None
        item = self._items[self._top]
        self._top -= 1
        return item

    def back(self):
        if self.empty():
            return None
        return self._items[self._top]

    def size(self):
        return self._top + 1

    def clear(self):
        self._top = -1

    def empty(self):
        return self._top == -1


def check(n, perm):
    stack = Stack()
    next_train = 1

    for train in perm:
        while next_train <= n:
            if stack.empty() or stack.back() != train:
                stack.push(next_train)
                next_train += 1
            else:
                break
        
        if stack.back() == train:
            stack.pop()
        else:
            return "No"
    
    return "Yes"


if __name__ == "__main__":
    while True:
        n = int(input())
        if n == 0:
            break
        
        while True:
            perm = list(map(int, input().split()))
            if perm[0] == 0:
                break
            print(check(n, perm))
        print()