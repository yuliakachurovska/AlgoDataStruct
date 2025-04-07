class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.next: [Node | None] = None

class List:

    def __init__(self):
        self.head: [Node | None] = None
        self.tail: [Node | None] = None

    def addToTail(self, val: int) -> None:
        """Додати число val в кінець Зв’язного Списку"""
        node = Node(val)
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def Print(self) -> None:
        """Вивести елементи Зв’язного Списку"""
        tmp = self.head
        while tmp:
            print(tmp.data, end=" ")
            tmp = tmp.next

    def PrintReverse(self, node=None) -> None:
        """Вивести елементи Зв’язного Списку в зворотному порядку"""
        if node is None:
            node = self.head
            if node is None:
                return

        if node.next is not None:
            self.PrintReverse(node.next)
        print(node.data, end=" ")


if __name__ == '__main__':
    n = int(input())
    lst = List()
    number = list(map(int, input().split()))
    for i in number:
        lst.addToTail(i)
    lst.Print()
    print()
    lst.PrintReverse()