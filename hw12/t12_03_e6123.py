class Stack:

    def __init__(self, maxsize=100):
        self._items = [0 for _ in range(maxsize)]
        self._top = -1

    def push(self, n):
        self._top += 1
        self._items[self._top] = n
        return "ok"

    def pop(self):
        if self.empty():
            return "error"
        item = self._items[self._top]
        self._top -= 1
        return item

    def back(self):
        if self.empty():
            return "error"
        return self._items[self._top]

    def size(self):
        return self._top + 1

    def clear(self):
        self._top = -1
        return "ok"

    def exit(self):
        return "bye"

    def empty(self):
        return self._top == -1
    
    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)
    

if __name__ == "__main__":
    with open("input.txt") as f:
        stack = Stack()
        for line in f:
            res = stack.execute(line)
            print(res)
            if res == "bye":
                break