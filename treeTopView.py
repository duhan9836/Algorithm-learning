class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def topView(root):
    res = []
    leftmost = 0
    rightmost = 0
    if root:
        levelnodes = [(root,0)]
        res.append((root.info,0))
        while len(levelnodes)>0:
            temptnodes = map(children,levelnodes)
            levelnodes = [child for childs in temptnodes for child in childs]
            if len(levelnodes)>0:
                levelleftnode = min(levelnodes,key=lambda x:x[1])
                levelrightnode = max(levelnodes,key=lambda x:x[1])
                if levelleftnode[1]<leftmost:
                    res.append((levelleftnode[0].info,levelleftnode[1]))
                    leftmost = levelleftnode[1]
                if levelrightnode[1]>rightmost:
                    res.append((levelrightnode[0].info,levelrightnode[1]))
                    rightmost=levelrightnode[1]
        res = sorted(res,key=lambda x:x[1])
    print(" ".join(map(lambda x:str(x[0]),res)))


def children(nodelvl):
    ret = []
    if nodelvl[0].left:
        ret.append((nodelvl[0].left,nodelvl[1]-1))
    if nodelvl[0].right:
        ret.append((nodelvl[0].right,nodelvl[1]+1))
    return ret



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
