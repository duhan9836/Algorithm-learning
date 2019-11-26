class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        start = self.root
        while start:
            if start.value == new_val:
                pass
            elif start.value > new_val:
                if start.left:
                    start = start.left
                else:
                    start.left = new_val
            else:
                if start.right:
                    start = start.right
                else:
                    start.right = new_val

    def search(self, find_val):
        start = self.root
        while start:
            if start.value == find_val:
                return True
            elif start.value > find_val:
                start = start.left
            else:
                start = start.right
        return False

    def print_in_order(self):
        start = self.root
        return print_in_order(start.left) + str(start.value) + print_in_order(start.right)


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print
tree.search(4)
# Should be False
print
tree.search(6)

print(print_in_order(tree))