class Node:

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class Deque:

    def __init__(self):
        self._size = 0
        self._front = None
        self._back = None

    def push_front(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = self._back = node
        else:
            node.next = self._front
            self._front.prev = node
            self._front = node
        self._size += 1
        return "ok"

    def push_back(self, item):
        node = Node(item)
        if self._size == 0:
            self._front = self._back = node
        else:
            node.prev = self._back
            self._back.next = node
            self._back = node
        self._size += 1
        return "ok"

    def pop_front(self):
        if self._size == 0:
            return "error"
        item = self._front.item
        if self._size == 1:
            self._front = self._back = None
        else:
            self._front = self._front.next
            self._front.prev = None
        self._size -= 1
        return item

    def pop_back(self):
        if self._size == 0:
            return "error"
        item = self._back.item
        if self._size == 1:
            self._front = self._back = None
        else:
            self._back = self._back.prev
            self._back.next = None
        self._size -= 1
        return item

    def front(self):
        if self._size == 0:
            return "error"
        return self._front.item

    def back(self):
        if self._size == 0:
            return "error"
        return self._back.item

    def size(self):
        return self._size

    def clear(self):
        self._front = self._back = None
        self._size = 0
        return "ok"

    def exit(self):
        return "bye"

    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)


if __name__ == '__main__':
    deque = Deque()
    with open("input.txt") as f:
        for line in f:
            res = deque.execute(line.strip())
            print(res)
            if res == "bye":
                break
