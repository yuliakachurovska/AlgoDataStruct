class Node:

     def __init__(self, item):
        self.item = item
        self.next = None

class Queue:

    def __init__(self):
        self._front = None
        self._back = 0
        self._size = 0
    
    def push(self, item):
        node = Node(item)
        if self._size > 0:
            self._back.next = node
        else:
            self._front = node
        self._back = node
        self._size += 1
        return "ok" 
        
    def pop(self):
        node = self._front
        if self._size == 0:
            return "error"
        if self._size == 1:
            self._back = None
        self._front = self._front.next    
        self._size -= 1
        return node.item
            
    def front(self):
        if self._size == 0:
            return "error"
        return self._front.item
    
    def clear(self):
        self._front = self._next = None
        self._back = self._size = 0
        return "ok"

    def size(self):
        return self._size

    def exit(self):
        return "bye"
    
    def execute(self, command):
        method, *args = command.split()
        return getattr(self, method)(*args)
    

if __name__ == "__main__":
    with open("input.txt") as f:
        queue = Queue()
        for line in f:
            res = queue.execute(line)
            print(res)
            if res == "bye":
                break