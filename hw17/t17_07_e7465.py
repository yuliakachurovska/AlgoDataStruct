class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.head = None
    
    def insert(self, val):
        if self.head is None:
            self.head = TreeNode(val)
        else:
            self._insert(self.head, val)
    
    def _insert(self, node, val):
        if val < node.val:
            if node.left is None:
                node.left = TreeNode(val)
            else:
                self._insert(node.left, val)
        else:
            if node.right is None:
                node.right = TreeNode(val)
            else:
                self._insert(node.right, val)
    
    def is_same_tree(self, other_tree):
        return self._is_same_tree(self.head, other_tree.head)
    
    def _is_same_tree(self, t1, t2):
            if t1 is None and t2 is None:
                return True
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            return self._is_same_tree(t1.left, t2.left) and self._is_same_tree(t1.right, t2.right)


if __name__ == '__main__':
    n1 = int(input())
    tree1 = Tree()
    for _ in range(n1):
        val = int(input())
        tree1.insert(val)

    n2 = int(input())
    tree2 = Tree()
    for _ in range(n2):
        val = int(input())
        tree2.insert(val)

    if tree1.is_same_tree(tree2):
        print("1")
    else:
        print("0")
