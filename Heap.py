#Heap Order Property: In a heap, for every node x with parent p, the value for p is smaller than or equal to the value of x.
"""attributes: a list representing the heap, the list size as currentsize;
methods: insert a node; delete a node with index i;build a heap from any given list of numbers;
tips: for list index convention of index i, the natural index is i+1,
children of list index i are : (i+1)*2-1 = 2*i+1, and (i+1)*2+1-1 = 2*i+2,
parent of list index i is (i+1)//2-1,
the range for i to be a child: i >0 and i < currentsize,
the range for i to be a parent: i >= 0 and 2*i+2 < currentsize"""

import random
class BinaryHeap():
    def __init__(self):
        self.heap = []
        self.currentsize = 0
    def insert(self,newnode):
        self.heap.append(newnode)
        self.currentsize += 1
        self.uprelocate(self.currentsize-1)
    def deleteany(self,i):
        #注意该函数对heap的两个attribute带来的改变，改变列表顺序，列表规模减一
        if i == self.currentsize -1:
            self.heap.pop()
            self.currentsize -= 1
        else:
            last = self.heap.pop()
            self.currentsize-=1
            self.heap[i] = last
            self.downrelocate(i)

    def buildHeap(self,alist):
        #从最后一个parent开始工作，利用downrelocate辅助函数将其放置合适位置，然后指针移至前一个parent做同样操作，直至root
        self.currentsize = len(alist)
        self.heap = alist[:]
        #用深度复制方式为self.heap赋值一个列表，防止原列表变化时变量值随之改变。
        i = (len(alist)+1)//2-1
        while i >= 0:
            self.downrelocate(i)
            i -= 1
        """逐一insert元素入heap，对于每个待插入元素来说，由于heap本身是有序的，因此找到新元素位置需要O(log(n)),而插入元素则需要O（n),因此整个操作的效率为O(nlog(n))
        而使用上面整体构建的方法，效率为O(n),怎么证明？？？？？"""
    def uprelocate(self,i):
        while i > 0 and self.heap[i] < self.heap[(i+1)//2-1]:
            self.heap[i],self.heap[(i+1)//2-1] = self.heap[(i+1)//2-1],self.heap[i]
            i=(i+1)//2-1


    #downrelocate 函数有问题！！！！！！！！！！！！！！（已解决）（no，corner case尚未解决）
    def downrelocate(self,i):
        while (i+1)*2 <= self.currentsize and self.heap[i] > self.heap[self.minChild(i,self.currentsize)]:
            minChild = self.minChild(i,self.currentsize)
            #隐含假设parent有两个child。what if仅有一个child呢？测试用例未考虑这样因素！！！！！！！！
            #此处注意：将函数值用变量固定下来，否则其后引用时，当函数变量变化时，函数值将随之改变。
            self.heap[i],self.heap[minChild] = self.heap[minChild],self.heap[i]
            i = minChild
    def minChild(self,i,s):
        if (i+1)*2 < s and self.heap[2*i+1] > self.heap[2*i+2]:
            return 2*i+2
        else:
            return 2*i+1

def heapSort(alist):
    res = []
    hs = BinaryHeap()
    hs.buildHeap(alist)
    n = len(alist)
    for i in range(n-1):
        res.append(hs.heap[0])
        hs.deleteany(0)
    res.append(hs.heap[0])
    return res
#问题出在未考虑currentsize很小的情况，当heap少于三个元素时，上面minChild函数失效。

lists = []
for j in range(3):
    alist=[]
    for i in range(10):
        alist.append(random.randrange(50))
    lists.append(alist)
#print(lists)

for alist in lists:
    print(alist,heapSort(alist))




alist=[10,29,47,82,16,36,20,11,4,3,9,7,6,2,5]
print(heapSort(alist))
#test insert,delete
h = BinaryHeap()
h.buildHeap(alist)
#print(h.heap)
blist = [5,8,3,9,1,17,2,4,6]
for i in blist:
    h.insert(i)
    #print(h.heap)
#print(h.currentsize)
h.deleteany(0)
#print(h.heap)



