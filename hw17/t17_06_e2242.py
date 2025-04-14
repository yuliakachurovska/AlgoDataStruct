class TreeNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)

    def preorder(self):
        result = self.key
        if self.left:
            result += self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result


if __name__ == '__main__':
    lines = []
    while True:
        line = input().strip()
        if line == '*':
            break
        lines.append(line)

    root = None
    for line in reversed(lines):
        for i in line:
            if root is None:
                root = TreeNode(i)
            else:
                root.insert(i)

    if root:
        print(root.preorder())
    else:
        print('')
