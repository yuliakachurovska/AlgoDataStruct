class Heap:
    def __init__(self, array):
        self.array = array
        self.len = len(array)

    def check(self):
        for i in range(self.len):
            left = 2 * i + 1
            right = 2 * i + 2

            if left < self.len and self.array[i] > self.array[left]:
                return False
            if right < self.len and self.array[i] > self.array[right]:
                return False
        return True

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    heap = Heap(arr)
    print("YES" if heap.check() else "NO")