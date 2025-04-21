class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.position = {}

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.position[self.heap[i][1]] = i
        self.position[self.heap[j][1]] = j

    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i][0] > self.heap[parent][0]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        size = len(self.heap)
        while 2 * i + 1 < size:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i
            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right
            if largest != i:
                self._swap(i, largest)
                i = largest
            else:
                break

    def add(self, id, priority):
        self.heap.append((priority, id))
        idx = len(self.heap) - 1
        self.position[id] = idx
        self._sift_up(idx)

    def pop(self):
        top = self.heap[0]
        last = self.heap.pop()
        del self.position[top[1]]
        if self.heap:
            self.heap[0] = last
            self.position[last[1]] = 0
            self._sift_down(0)
        return top

    def change(self, id, new_priority):
        idx = self.position[id]
        old_priority, _ = self.heap[idx]
        self.heap[idx] = (new_priority, id)
        if new_priority > old_priority:
            self._sift_up(idx)
        else:
            self._sift_down(idx)


if __name__ == '__main__':
    pq = PriorityQueue()
    try:
        while True:
            line = input()
            if not line:
                continue
            parts = line.strip().split()
            cmd = parts[0]
            if cmd == "ADD":
                id = parts[1]
                pr = int(parts[2])
                pq.add(id, pr)
            elif cmd == "POP":
                pr, id = pq.pop()
                print(f"{id} {pr}")
            elif cmd == "CHANGE":
                id = parts[1]
                new_pr = int(parts[2])
                pq.change(id, new_pr)
    except EOFError:
        pass