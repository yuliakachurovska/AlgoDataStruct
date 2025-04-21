class MinHeap:
    def __init__(self):
        self._items = [0]

    def _swap(self, i, j):
        self._items[i], self._items[j] = self._items[j], self._items[i]

    def insert(self, item):
        self._items.append(item)
        self._sift_up(len(self._items) - 1)

    def _sift_up(self, i):
        while i > 1:
            parent = i // 2
            if self._items[i] < self._items[parent]:
                self._swap(i, parent)
                i = parent
            else:
                break

    def _sift_down(self, i):
        while 2 * i < len(self._items):
            left = 2 * i
            right = 2 * i + 1
            min_child  = i

            if left < len(self._items) and self._items[left] < self._items[min_child ]:
                min_child  = left
            if right < len(self._items) and self._items[right] < self._items[min_child ]:
                min_child  = right

            if min_child  != i:
                self._swap(i, min_child )
                i = min_child 
            else:
                break

    def extract_min(self):
        if len(self._items) <= 1:
            return None
        self._swap(1, -1)
        item = self._items.pop()
        self._sift_down(1)
        return item


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))

    heap = MinHeap()
    for num in nums:
        heap.insert(num)

    total = 0

    while len(heap._items) > 2:
        x = heap.extract_min()
        y = heap.extract_min()
        cost = x + y
        total += cost
        heap.insert(cost)

    print(total)
