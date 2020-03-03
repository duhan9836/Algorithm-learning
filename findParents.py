from nodeAndTree import Node,BinarySearchTree
#non-recursive way
def findParents1(root,val):
    parents = []
    marked = []
    current = root
    while current:
        #print(current.info)
        #print(list(map(lambda x:x.info,parents)))
        if current.info == val:
            return parents
        else:
            if current not in parents:
                parents.append(current)
            if current.left and current.left not in marked:
                current = current.left
            elif current.right and current.right not in marked:
                current = current.right
            else:
                marked.append(parents.pop())
                current = parents[-1]

#recursive way
def findParents(root,val):
    if root.info == val:
        return []
    else:
        currentlvl = [root]
        nextlvl = []
        while len(currentlvl)>0:
            for node in currentlvl:
                if node.left and node.left.info == val:
                    return findParents(root,node.info).append(node)
                elif node.right and node.right.info == val:
                    return findParents(root,node.info).append(node)
                else:
                    nextlvl.append(node.left)
                    nextlvl.append(node.right)
            currentlvl = nextlvl




tree = BinarySearchTree()
#t = int(input())
#arr = list(map(int, input().split()))
t = 7
arr = [5,3,8,1,4,7,9]
for i in range(t):
    tree.create(arr[i])
print("tree created")

parents = findParents(tree.root,1)
print(list(map(lambda x:x.info,parents)))
