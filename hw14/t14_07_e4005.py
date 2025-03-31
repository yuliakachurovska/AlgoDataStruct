class Queue:
    def __init__(self, maxsize):
        self._items = [None] * maxsize
        self._maxsize = maxsize
        self._front = 0
        self._back = -1
        self._size = 0

    def push(self, item):
        if self._size == self._maxsize:
            raise OverflowError()
        self._back = (self._back + 1) % self._maxsize
        self._items[self._back] = item
        self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError()
        item = self._items[self._front]
        self._front = (self._front + 1) % self._maxsize
        self._size -= 1
        return item
    
    def front(self):
        if self._size == 0:
            raise IndexError()
        return self._items[self._front]
    
    def size(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0


def play_game(n, p1, p2):
    player1 = Queue(n)
    player2 = Queue(n)
    for card in p1:
        player1.push(card)
    for card in p2:
        player2.push(card)
    
    MAXTURNS = 200000
    turns = 0
        
    while turns < MAXTURNS:
        if player1.is_empty():
            return "second", turns
        elif player2.is_empty():
            return "first", turns
        
        card1 = player1.pop()
        card2 = player2.pop()

        if (card1 > card2 and not (card1 == n - 1 and card2 == 0)) or (card1 == 0 and card2 == n - 1):
            player1.push(card1)
            player1.push(card2)
        else:
            player2.push(card1)
            player2.push(card2)

        turns += 1

    return "draw",

n = int(input())
p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
print(*play_game(n, p1, p2))