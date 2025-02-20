EMPTY = None

class TelephoneBook:
    def __init__(self, size=11):
        self._size = size
        self._count = 0
        self._keys: list[EMPTY | int] = [EMPTY for _ in range(size)]

    def hash(self, key: int):
        return key % self._size

    def set(self, key: int):
        i = self.hash(key)
        while self._keys[i] is not EMPTY:
            if self._keys[i] == key:
                return
            i = (i + 1) % self._size
        
        self._count += 1
        self._keys[i] = key

    def count(self):
        return self._count


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(int, input().split()))
    book = TelephoneBook(size=1.5 * n)
    
    for num in numbers:
        book.set(num)
    
    print(book.count())