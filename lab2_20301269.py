#AVI ROY
# Task1(i)
class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def printNode(self):
        print(self.value, end=" ")




# Task
class MyList:

    # Task2(1a)
    def __init__(self, a):
        self.head = None
        if isinstance(a, list):  # Task2(1b)
            self.head = None
            nde = None
            for i in range(0, len(a)):
                n1 = Node(a[i], None)
                if (self.head == None):
                    self.head = n1
                    nde = n1
                else:
                    nde.next = n1
                    nde = n1
        elif isinstance(a, MyList):  # Task2(1c)
            self.head = None
            nde = None
            n = a.head
            while n != None:
                n1 = Node(n.value, None)
                if (self.head == None):
                    self.head = n1
                    nde = n1
                else:
                    nde.next = n1
                    nde = n1
                n = n.next

    # Task2(2)
    def showList(self):
        nde = self.head
        if nde == None:
            print("List is empty")
        else:
            while nde != None:
                nde.printNode()
                nde = nde.next

    # Task2(3)
    def isEmpty(self):
        nde = self.head
        if nde == None:
            return True
        else:
            return False

    # Task2(4)
    def clear(self):
        self.head = None

    # Task2(5)

    def insert(self, newElement,):
        nde = self.head
        if (self.head is None):
            nde1 = Node(newElement, None)
            self.head = nde1
        else:
            while nde is not None:
                if (nde.value == newElement):
                    return "Given element already exists"
                nde = nde.next
            nde = self.head
            while nde.next is not None:
                nde = nde.next
            nde.next =nde1
        return self.head

    # Task2(6)

    def insert(self, newElement, index):
        nde = self.head
        if self.head is None:
            nde1 = Node(newElement, None)
            self.head = nde1
        else:
            while nde is not None:
                if nde.value == newElement:
                    return "Given element already exists"
                nde = nde.next
            counter = 0
            nde = self.head
            while n is not None:
                if counter < (index - 1):
                    nde = nde.next
                    counter = counter + 1
            nde1.next = nde.next
            n.next = nde1
        return self.head

    # Task2(7)

    def remove(self, deletekey):
        nde = self.head
        if self.head != None and nde.value == deletekey:
            self.head = nde.next
            nde = None
            while nde != None and nde.value != deletekey:
                pre = nde
                nde = nde.next
            pre.next = nde.next
            nde = None

    # Task3(1)

    def findEven(self):
        nde = self.head
        emp = list()
        while nde != None:
            if (nde.value % 2) == 0:
                emp += nde.value
            nde = nde.next
        print(emp)

    # Task3(2)
    def objcheck(self, num):
        nde = self.head
        while nde != None:
            if nde.element == num:
                return True
            nde = nde.next
        return False

    # Task3(3)
    def reverser(self):
        h1 = None
        nde = self.head
        while nde != None:
            temp = nde.next
            nde.next = h1
            h1 = nde
            nde = temp
            self.head = h1

    #task3(4)
    class Solution:
        def solve(self, node):

        values = []
        head = node
        while node:
            values.append(node.val)
            node = node.next

        values.sort()
        values = collections.deque(values)

        node = head
        while node:
            node.val = values.popleft()
            node = node.next

        return head

    # Task3(5)
    def total(self):
        total = 0
        nde = self.head
        while nde != None:
            total += nde.value
            nde = nde.next
        print(total)
    #task3(6)

    def rotate(self, r, k):
        if r == ("left"):
            if k == 0:
                return
            newNode = self.head
            count = 1
            while (count < k and newNode is not None):
                currentNode = newNode.next
                count += 1
                if currentNode is None:
                    return
                kNode = currentNode
                while (newNode.next is not None):
                    newNode = newNode.next
                newNode.next = self.head
                self.head = kNode.next
                kNode.next = None
                link.showList()
        elif r == ("right"):
            temp = self.head
            i = 1
            while (temp.next is not None):
                temp = temp.next
                i += 1
            if (k > i):
                k = k % i
            k = i - k
            if (k == 0 or k == i):
                return self.head
            newNode = self.head
            count = 1
            while (count < k and newNode is not None):
                newNode = newNode.next
                count += 1
            if (newNode is None):
                return self.head
            kthnode = newNode
            temp.next = self.head
            self.head = kthnode.next
            kthnode.next = None
            link.showList()


a = [11, 22, 33, 44, 55, 66]
lst = MyList(a)
lst1 = MyList(lst)
lst2 = MyList(a)
lst.showList()
print()
lst1.showList()
print()
lst2.showList()
print(lst2.isEmpty())
lst.clear()
lst.showList()
lst.insert(77, 2)
lst.showList()
print()
lst.remove(22)
lst.showList()
print()
lst.reverser()
lst.showList()