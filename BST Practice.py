class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        current = self.root
        while current:
            if current.value == new_val:
                return None
            elif current.value > new_val:
                if current.left:
                    current = current.left
                else:
                    current.left = Node(new_val)
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = Node(new_val)

    def search(self, find_val):
        current = self.root
        while current:
            if current.value == find_val:
                return True
            elif current.value > find_val:
                current = current.left
            else:
                current = current.right
        return False

   # def print_in_order(self):
    #    start = self.root
     #   return print_in_order(start.left) + str(start.value) + print_in_order(start.right)


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

#print(print_in_order(tree))
