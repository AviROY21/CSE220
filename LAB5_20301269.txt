NAME:AVISHEK ROY SPARSHO
SEC:02
ID:20301269




#TASK-1

#a
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
number=int(input('value: '))
print(factorial(number))

#b
def FibonacciS(n):
    if n<0:
        print('Wrong input')
    elif n==0:
        return 0
    elif n<=1:
        return n
    else:
        return (FibonacciS(n-1)+FibonacciS(n-2))
inPut=int(input('value:'))
for x in range(0,inPut):

    print(FibonacciS(x))

#c

def recursiveArray(array,count=0):

    if len(array) == count:
        return
    else:
        print(array[count])
        recursiveArray(array,count+1)
list = [10,20,30,40]
recursiveArray(list)


#d

def powerRecursively(Num,power=0):
    if power==0:
        return 1
    else:
        return Num* powerRecursively(Num,power-1)
print(powerRecursively(3,1))
print(powerRecursively(3,3))
print(powerRecursively(3,2))
#TASK-02

#a

def deciTObin(Dec_number,string=''):
    if Dec_number==0:
         print(string)
    else:
        binary=Dec_number%2
        string=str(binary)+string
        deciTObin(Dec_number//2,string)
DecimalNum=int(input('Value:'))

deciTObin(DecimalNum)

#b


class Node:
    def __init__(self,element,next):

        self.element=element
        self.next = next


    def SUmofNodes(head):
        if (head == None):
            return 0
        else:
           return (head.element+Node.SUmofNodes(head.next))

head1=Node(7,None)
head2=Node(6,head1)
head3=Node(8,head2)
head4=Node(4,head3)
head5=Node(2,head4)
head6=Node(10,head5)
head=Node(1,head6)
print("Sum of Nodes={}".format(Node.SUmofNodes(head)))



#c


class Node:


    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:


    def __init__(self):
        self.head = None


    def reverse(self):
        prev = None
        current = self.head
        while (current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    def printList(self):
        temp = self.head
        while (temp):
            print (temp.data)
            temp = temp.next



list = LinkedList()
list.push(40)
list.push(30)
list.push(20)
list.push(10)
print("Given Linked List")
list.printList()
list.reverse()
print("\nReversed Linked List")
list.printList()

#TASK-3
def hocBuilder(height):
    if height<=0:
        return
    elif height==1:
        return 8
    else:
        return 5+hocBuilder(height-1)
x=hocBuilder(3)
print(x)

#TASK-4

#a
def recursionPattern(Num,count=1):
    if count==Num+1:
        return
    else:
        for x in range(1,count+1):
            print(x,end=' ')
        print()
        recursionPattern(Num,count+1)
inPUT=int(input('Input:'))
recursionPattern(inPUT)

#b
def recursionReversePattern(Num1,count1=1):
    if count1==Num1+1:
        return
    else:
        print(' '*(Num1-count1),end='')
        for y in range(1,count1+1):
            print(y,end='')
        print()
        recursionReversePattern(Num1,count1+1)
inPUT1=int(input('Input:'))
recursionReversePattern(inPUT1)

#TASK-5
class FinalQ:
    def print(self,array,idx):
        if (idx<len(array)):
        profit=self.calcProfit(array[idx])
        print(f"{isx+1}. Investment:{array[idx]}; Profit:{profit}")
        self.print(array,idx+1)
    def calProfit(self,investment):
        investment -=25000
        profit=0
        if investment>=75000:
            profit=75000*(4.5/100)
            investment-=75000
        else:
            profit=investment*(4.5/100)
            investment=0
        profit=investment*(8/100)+profit
        return profit
array=[25000,100000,250000,350000]
f=FinalQ()
f.print(array,0)
