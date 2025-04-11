class Tree:
    def __init__(self, key: int):
        self.key = key
        self.parent = None
        self.children = []
        self.colors = set()

    def add_child(self, child):
        self.children.append(child)

    def dfs(self):
        for child in self.children:
            child.dfs()
            self.colors.update(child.colors)

def counter(nodes: dict, N):
    for i in range(1, N + 1):
        print(len(nodes[i].colors), end=" ")

if __name__ == "__main__":
    with open("input.txt") as f:
        N = int(f.readline())

        nodes = {}
        for i in range(1, N + 1):
            nodes[i] = Tree(i)

        root_id = None
        for i in range(1, N + 1):
            parent, color = [int(el) for el in f.readline().split()]
            node = nodes[i]
            node.colors.add(color)

            if parent == 0:
                root_id = i
            else:
                par_node = nodes[parent]
                node.parent = par_node
                par_node.add_child(node)

    root = nodes[root_id]
    root.dfs()
    counter(nodes, N)
