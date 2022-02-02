#AVI ROY




#TASK1


class Node:
    def __init__(self, object, next=None, previous=None):
        self.object = object
        self.next = next
        self.previous = previous


# TASK2
class DoublyList:
    def __init__(self, a):
        list1 = Node(None, None, None)
        self.head = list1
        for x in a:
            node1 = Node(x, None, None)
            if self.head is None:
                self.head.next = node1
                node1.previous = self.head
                tail = node1
            else:
                tail = node1
                tail.next = node1
                node1.previous = tail
        self.head.previous = tail
        node1.next = self.head

    # TASK3
    def showList(self):
        node1 = self.head.next
        if self.head is None:
            print('EMPTY list')
        else:
            while node1 is not self.head:
                print(node1.object)
                node1 = node1.next

    def size(self):
        node1 = self.head.next
        size = 0
        while node1 is not self.head:
            size = size + 1
            node1 = node1.next
        return self.size

    # TASK 4
    def insert(self, newElement):
        newList = Node(newElement, None, None)
        node1 = self.head.next
        if node1 is None:
            self.head.next = newList
        else:
            while node1 is not self.head:
                if node1.value == newElement:
                    print('newElement already exists')
                node1 = node1.next
            interInfo = self.head.next
            while interInfo.next is not self.head:
                interInfo = interInfo.next
            interInfo.next = newList
            newList.previous = interInfo
            newList.next = self.head
            self.head.previous = newList

    # TASK5
    def insertInd(self, newElement, index):
        self.newElement = newElement
        self.index = index
        newList = Node(newElement, None, None)
        node1 = self.head.next
        count = 1
        while count < self.index:
            node1 = node1.next
            count += 1
        interInfo = node1.next
        node1.next = newList
        newList.previous = node1
        newList.next = interInfo
        interInfo.previous = newList
        return (self.showList())

    # TASK6
    def remove(self, index):
        self.index = index
        selected_node = self.head
        if selected_node < 0:
            print('Wrong index')
            return
        else:
            node1 = self.head.next
            if self.head is None:
                print('This list is empty ')
            else:
                count = 0
                while node1 is not self.head:
                    self.tail = node1.previous
                    self.head = node1.next
                    if count is index:
                        self.tail.next = self.head
                        self.head.previous = self.tail
                        node1.next = None
                        node1.previous = None
                        return
                    count = count + 1
                    node1 = node1.next
            return (self.showList())

    # Task7
    def removeKey(self, deletekey):
        self.deletekey = deletekey
        node1 = self.head.next
        count = 0
        while node1 is not self.head:
            if node1.element is deletekey:
                count += 1
                node1 = node1.next
            else:
                node1 = node1.next
                if count == 0:
                    print('Given element is not present')
                else:
                    print('Deleted key value:', deletekey)
                    node1 = self.head.next
                    while node1 is not self.head:
                        if (node1.element == self.deletekey):
                            node1.previous.next = node1.next
                            node1.next.previous = node1.previous
                            node1 = node1.next
                        else:
                            node1 = node1.next
                    return (self.showList())

    def nodeAt(self, index):
        self.index = index
        count = 0
        for tail in self.head.next:
            if count == index:
                return tail
            count += 1
        return None


print("\n *  Test-01 *")
list1 = [10, 20, 30, 40]
linklist = DoublyList(list1)
linklist.showList()
assert "\n **  Test-02  *" in linklist
myNode = linklist.nodeAt(3)
linklist.insert(50)
assert "\n *  Test-03  *" in myNode
index = linklist.index(40)
assert index == 80
linklist.insertInd()
assert "\n *  Test-04  **" in myNode
linklist.remove(4)
assert "\n *  Test-05  **" in myNode
linklist.removeKey(30)



list1 = [1, 2, 3, 4, 5]
linklist = DoublyList(list1)
print("Elements of the list : ")
linklist.showList()
print("After inserting a new element at the tail of the list : ")
linklist.insert(6)
linklist.showList()
print("After inserting a new element at the given index : ")
linklist.insert(7, 5)
linklist.showList()
print("After removing the node at given index")
linklist.remove(6)
linklist.showList()
print("The deleted key value : ")
print(linklist.removeKey(7))
print("After removing the element : ")
linklist.showList()


print("\n *  Test-01 *")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1)
h1.showList()
assert "\n **  Test-02  *" in h1
myNode = h1.nodeAt(3)
h1.insert(50)
assert "\n *  Test-03  *" in myNode
index = h1.index(40)
assert index == 80
h1.insertInd()
assert "\n *  Test-04  **" in myNode
h1.remove(4)
assert "\n *  Test-05  **" in myNode
h1.removeKey(30)


