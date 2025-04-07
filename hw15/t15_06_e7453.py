class Node:
    def __init__(self, data: int):
        self.data: int = data
        self.next: 'Node | None' = None


class List:
    def __init__(self):
        self.head: 'Node | None' = None
        self.tail: 'Node | None' = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def empty(self) -> bool:
        return self.head is None

    def RotateRight(self, k: int) -> None:
        """Здійснити обертання Зв’язного Списку праворуч на k позицій"""
        if self.empty() or self.head.next is None:
            return

        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        k %= length
        if k == 0:
            return

        new_tail = self.head
        for _ in range(length - k - 1): # шукаємо елемент на (length - k - 1) позиції, це новий tail
            new_tail = new_tail.next

        new_head = new_tail.next   # Новий head це елемент після нового tail
        new_tail.next = None
        tail.next = self.head
        self.head = new_head
        self.tail = tail

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next
        print()


if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    n = int(lines[0])
    numbers = list(map(int, lines[1].split()))
    kl = list(map(int, filter(None, lines[2:])))

    lst = List()
    for val in numbers:
        lst.addToTail(val)

    for k in kl:
        lst.RotateRight(k)
        lst.Print()
