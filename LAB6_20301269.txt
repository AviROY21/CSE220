NAME:AVISHEK ROY SPARSHO
SEC-02
ID-20301269



#TASK-1
def exchange(Array,x,y):
    struc=Array[x]
    Array[x]=Array[y]
    Array[y]=struc
def recursivesort_Selection(Array, x, num):
    countmin=x
    for y in range(x+1,num):
        if Array[y] < Array[countmin]:
            countmin=y
    exchange(Array, countmin, x)
    if x+1 <num:
        recursivesort_Selection(Array,x+1,num)
if __name__ == '__main__':
    tester=[-3,-5, 82, 22, 8, 4,2]
    recursivesort_Selection(tester, 0, len(tester))
    print(tester)
#TASK-2
def Recursivesort_Insertion(array, num):
    if num<= 1:
        return
    Recursivesort_Insertion(array,num- 1)
    prev = array[num-1]
    y = num - 2
    while (y>= 0 and array[y] >prev):
        array[y+1] = array[y]
        y-=1
    array[y+1]=prev
array= [1,6, 9, 7, 3,8,2,11,2]
newArr=len(array)
Recursivesort_Insertion(array, newArr)
print('Sorted array:')
for x in range(newArr):
    print(array[x], end=" ")

# Task-03
class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
class List:
    def __init__(self,a):
        self.head=None
        previous=None
        for x in range(0,len(a)):
            newNODE= Node(a[x], None)
            if self.head == None:
                self.head = newNODE
                previous=self.head
            else:
                previous.next =newNODE
                previous=newNODE

    def list1(self, node1):
        if node1 is not None:
            return 1 + self.list1(node1.next)
        else:
            return 0

    def print(self):
        if self.head == None:
            print('List is empty')
        else:
            node1=self.head
            while node1 != None:
                print(node1.element)
                node1 = node1.next



    def bubbleSort(self):
        node1 = self.head
        len1 =self.list1(node1)
        for x in range(len1 - 1, -1, -1):
            node1 = self.head
            for y in range(0,x):
                if node1.element > node1.next.element:
                    struc= node1.element
                    node1.element=node1.next.element
                    node1.next.element =struc
                node1=node1.next
        return self.head


tester= [19,-5,11,55,78,25, 72,48]
tester=List(tester)
tester.bubbleSort()
tester.print()



#TASK-4

class Node:
    def __init__(self,element,next):
        self.element=element
        self.next=next
class List:
    def __init__(self,a):
        self.head=None
        previous=None
        for x in range(0,len(a)):
            newNODE= Node(a[x], None)
            if self.head == None:
                self.head = newNODE
                previous=self.head
            else:
                previous.next =newNODE
                previous=newNODE

    def list1(self, node1):
        if node1 is not None:
            return 1 + self.list1(node1.next)
        else:
            return 0

    def print(self):
        if self.head == None:
            print('List is empty')
        else:
            node1=self.head
            while node1 != None:
                print(node1.element)
                node1 = node1.next

    def selection_sorting(self):
        node = self.head
        count = self.list1(node)
        for x in range(0, count, 1):
            low = node.element
            y = x + 1
            node1 = node.next
            while y <= count - 1:
                if node1.element < low:
                    low = node1.element
                    struc= node.element
                    node.element = node1.element
                    node1.element =struc
                node1 = node1.next
                y =y+1
            node = node.next


tester = [29, 45, 1, 5, 55, 78, 2, 4]
tester = List(tester)
tester.selection_sorting()
tester.print()


#TASK7
FibArrfrom=[1, 1]
def Fibonacci(n):
    if n <= 0:
        print("Incorrect input")
    if (n==0 or n==1):
        return 1
    else:
        if n <= len(FibArrfrom):
            return FibArrfrom[n - 1]
    strucFib = Fibonacci(n-1)+Fibonacci(n- 2)
    FibArrfrom.append(strucFib)
    return strucFib

n=int(input('Enter value: '))
print(Fibonacci(n))



#TASK-6

def binarySearch(list1,key,start,end):
    if end-start <= 1:
        if key < list1[start]:
            return start-1
        else:
            return start

    middle = (start + end) // 2
    if list1[middle] < key:
        return binarySearch(list1, key, middle+1, end)
    else:
        if list1[middle] > key:
            return binarySearch(list1, key, start, middle-1)
    return middle


list1 = [9,2,3,4,6]
binarySearch(list1,3,0,len(list1))


#TASK5


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def getNode(data):
    newNode = Node(0)
    newNode.data = data
    newNode.prev = newNode.next = None
    return newNode
def sortedInsert(head_ref, newNode):
    if (head_ref == None):
        head_ref = newNode

    elif ((head_ref).data >= newNode.data):
        newNode.next = head_ref
        newNode.next.prev = newNode
        head_ref = newNode

    else:
        current = head_ref
        while (current.next != None and
               current.next.data < newNode.data):
            current = current.next
        newNode.next = current.next
        if (current.next != None):
            newNode.next.prev = newNode
        current.next = newNode
        newNode.prev = current
    return head_ref
def insertionSort(head_ref):
    sorted = None
    current = head_ref
    while (current != None):
        next = current.next
        current.prev = current.next = None
        sorted = sortedInsert(sorted, current)
        current = next
    head_ref = sorted
    return head_ref
def printList(head):
    while (head != None):
        print(head.data, end=" ")
        head = head.next
def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = (head_ref)
    new_node.prev = None

    if ((head_ref) != None):
        (head_ref).prev = new_node
    (head_ref) = new_node
    return head_ref
if __name__ == "__main__":
    head = None
    head = push(head, 9)
    head = push(head, 3)
    head = push(head, 5)
    head = push(head, 10)
    head = push(head, 12)
    head = push(head, 8)
    print('Before Sorting')
    printList(head)
    head = insertionSort(head)
    print('\nAfter Sorting')
    printList(head)





