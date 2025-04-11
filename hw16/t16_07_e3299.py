from collections import deque

class Tree:
    def __init__(self, key, parent=None):
        self.key = key
        self.parent = parent
        self.children = []

    def bfs(self, key):
        queue = deque([self])
        while queue:
            node = queue.popleft()
            if node.key == key:
                return node
            queue.extend(node.children)
        return None

    def lca(self, i, j):
        ances = set()
        node_i = self.bfs(i)
        while node_i:
            ances.add(node_i)
            node_i = node_i.parent

        node_j = self.bfs(j)
        while node_j:
            if node_j in ances:
                return node_j.key
            node_j = node_j.parent

def build_tree(parents, n):
    nodes = [Tree(i) for i in range(n)]
    for i, p in enumerate(parents):
        nodes[i+1].parent = nodes[p]
        nodes[p].children.append(nodes[i+1])
    return nodes[0]

def result(tree, n, m, a1, a2, t1, t2, t3):
    res = 0
    v = 0
    a_prev2, a_prev1 = a1, a2
    for i in range(m):
        if i == 0:
            u = (a1 + v) % n
            v = tree.lca(u, a2)
        else:
            a_curr = (t1 * a_prev2 + t2 * a_prev1 + t3) % n
            a_next = (t1 * a_prev1 + t2 * a_curr + t3) % n
            u = (a_curr + v) % n
            v = tree.lca(u, a_next)
            a_prev2, a_prev1 = a_curr, a_next
        res += v
    return res

if __name__ == "__main__":
    with open("input.txt") as f:
        n, m = map(int, f.readline().split()) # n — кількість вершин, m — кількість запитів
        parents = list(map(int, f.readline().split())) 
        a1, a2 = map(int, f.readline().split())
        t1, t2, t3 = map(int, f.readline().split())

    tree = build_tree(parents, n)
    print(result(tree, n, m, a1, a2, t1, t2, t3))
