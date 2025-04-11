class Directory:
    def __init__(self, name):
        self.name = name
        self.children = {}

    def add_child(self, name):
        if name not in self.children:
            self.children[name] = Directory(name)

    def get_child(self, name):
        return self.children.get(name)

def build_tree(paths):
    root = Directory('')
    
    for path in paths:
        directories = path.split('\\')
        current = root
        for directory in directories:
            if current.get_child(directory) is None:
                current.add_child(directory)
            current = current.get_child(directory)
    
    return root

def print_tree(directory, depth=0):
    for child_name in sorted(directory.children.keys()): #у лексикографічному порядку
        print(' ' * depth + child_name)
        print_tree(directory.children[child_name], depth + 1)

if __name__ == "__main__":
    N = int(input())
    paths = [input().strip() for _ in range(N)]

    root = build_tree(paths)
    print_tree(root)
