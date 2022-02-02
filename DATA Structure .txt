1. Sort a singly linked sequential list using bubble sort algorithm

#user defined class for nodes
class Node:
    def __init__(self, data=None, link=None):
        self.data=data
        self.link=link
    def __str__(self):
        return str(self.data)

#user defined class for Linked list
class LinearList:
    def __init__(self, start=None,nodecount=0):
        self.start=start
        self.nodecount=nodecount #stores number of nodes in linked list
    def addBegNode(self, value=None):#Adding nodes at beginning
        node=Node(value)
        node.link=self.start
        self.start=node
        self.nodecount=self.nodecount+1

    def printList(self):#traverse abd display nodes
        ptr=self.start
        while ptr:
            print(ptr)
            ptr=ptr.link
        print()
    
    def bubbsort(self):
        for i in range(self.nodecount-1):#for controlling passes of Bubble Sort
            curr=self.start
            nxt=curr.link
            prev=None
            while nxt:#Comparisons in passes
                if curr.data>nxt.data:
                    if prev==None:
                       prev=curr.link
                       nxt=nxt.link
                       prev.link=curr
                       curr.link=nxt
                       self.start=prev
                    else:   
                        temp=nxt
                        nxt=nxt.link
                        prev.link=curr.link
                        prev=temp
                        temp.link=curr
                        curr.link=nxt
                else:           
                    prev=curr
                    curr=nxt
                    nxt=nxt.link
            i=i+1             
           
#Create blank Linked List        
ll=LinearList()
numele= input('How many elements to be added in the Linked List??')
#add nodes at begging in the Linked List
for cnt in range(int(numele)):
    ele= input('Enter a value to be added at the beginning of the Linked List ')
    ll.addBegNode(ele)
    cnt=cnt+1
#Print Linked List  before sorting  
print("Linked List Initially")
ll.printList()
ll.bubbsort()
#Print Linked List  After sorting  
print("Linked List after sorting")
ll.printList()
2. Sort a singly linked sequential list using selection sort algorithm

class Node(object):

    def __init__(self,val):

        self.val = val

        self.next = None



    def get_data(self):

        return self.val



    def set_data(self,val):

        self.val = val



    def get_next(self):

        return self.next



    def set_next(self,next):

        self.next = next





class LinkedList(object):



    def __init__(self,*values):

        self.count = len(values) -1

        self.head = Node(values[0])

        node = self.head

        for idx, val in enumerate(values):

            if idx == 0:

                continue

            else:

                tempnode = Node(val)

                node.set_next(tempnode)

                node = node.get_next()





    def get_count(self):

        return self.head



    def insert(self,data):

        new_node = Node(data)

        new_node.set_next(self.head)

        self.head = new_node

        self.count +=1



    def insert_at(self,idx,val):

        if idx > self.count +2:

            return



        if idx == 0:

            self.insert(val)

        else:

            tempIdx = 0

            node = self.head

            while tempIdx < idx -1:

                node = node.get_next()

                tempIdx += 1

            continuation = node.get_next()

            insertion = Node(val)

            node.set_next(insertion)

            node.get_next().set_next(continuation)

            self.count += 1



    def find(self,val):

        item = self.head

        while item != None:

            if item.get_data() == val:

                return item

            else:

                item = item.get_next()



        return None



    def deleteAt(self,idx):

        if idx > self.count+1:

            return

        if idx == 0:

            self.head = self.head.get_next()

        else:

            tempIdx = 0

            node = self.head

            while tempIdx < idx -1:

                node = node.get_next()

                tempIdx +=1

            node.set_next(node.get_next().get_next())

            self.count -= 1



    def dump_list(self):

        tempnode = self.head

        while (tempnode != None):

            print("Node: ",tempnode.get_data())

            tempnode = tempnode.get_next()





    def swap(self,idx_a,idx_b):

        if idx_a == idx_b:

            return

        elif idx_a > idx_b:

            idx_2,idx_1 = idx_a,idx_b

        else:

            idx_2,idx_1 = idx_b,idx_a



        node = self.head

        tempIdx = 0



        while tempIdx < idx_2:

            if tempIdx != idx_1:

                node = node.get_next()

                tempIdx += 1

            else:

                elem_1 = node.get_data()

                node = node.get_next()

                tempIdx += 1

        elem_2 = node.get_data()



        self.deleteAt(idx_1)

        self.deleteAt(idx_2-1)

        self.insert_at(idx_1,elem_2)

        self.insert_at(idx_2,elem_1)



    def move_min(self,sorted_idx):

        temp_idx = 0

        node = self.head

        selection = self.head.get_data()

        while temp_idx <= self.count:



            if temp_idx <= sorted_idx:

                node = node.get_next()

                temp_idx += 1



            elif temp_idx == sorted_idx +1:

                selection = node.get_data()

                selected_idx = temp_idx

                node = node.get_next()

                temp_idx += 1



            else:

                if node.get_data() < selection:

                    selection = node.get_data()

                    selected_idx = temp_idx

                try:

                    node = node.get_next()

                    temp_idx +=1

                except:

                    break



        self.deleteAt(selected_idx)

        self.insert_at(sorted_idx, selection)

        return sorted_idx + 1



    def selection_sort(self):

        """

        Note, move_min() method assumes that the element at first index is already sorted. As such, after

        iteratively calling move_min(), the first element will be moved to the final index. Logic must be

        built in to ID the final element and move it to its appropriate home.

        """



        # part 1: sorts elements, pushing first element to last position

        sorted_idx = 0

        while sorted_idx < self.count:

            sorted_idx = self.move_min(sorted_idx)





        # part 2: identifies final element and relocates appropriately

        temp_idx = 0

        node = self.head

        while temp_idx < self.count:

            node = node.get_next()

            temp_idx += 1

        final_elem = node.get_data()

        final_idx = temp_idx



        temp_idx = 0

        node = self.head

        while temp_idx < self.count:

            if node.get_data() < final_elem:

                temp_idx += 1

                node = node.get_next()

            else:

                self.deleteAt(final_idx)

                self.insert_at(temp_idx,final_elem)

                break





if __name__ == '__main__':

    t1 = LinkedList(4,2,1,0,3)

    t1.selection_sort()

    t1.dump_list()
3. Sort a doubly linked sequential list using insertion sort algorithm

# create class Node of a doubly linked list
class Node:
    #initialise the constructor values 
        def __init__(self, data):
                self.data = data
                self.prev = None
                self.next = None


#insert data in a sorted way inside doubly sorted linked list  
def sortedInsertIntoDB(headsreference, new_nodex):
    #point curr variable to null
        currH = None
        
        # if list is empty then assigne head refrence to new node
        if (headsreference == None):
            headsreference = new_nodex

        # if the node is to be inserted at the beginning in doubly linked list
        elif ((headsreference).data >= new_nodex.data) :
            new_nodex.next = headsreference
            new_nodex.next.prev = new_nodex
            headsreference= new_nodex
                
        #otherwise 
        else :
            #assing headsreferece to curr
                currH = headsreference

                # find the node after which the new node needs to be inserted
                while (currH.next != None and
                        currH.next.data < new_nodex.data):
                        currH = currH.next

                # make a link with the newnode and curr node'next 
                new_nodex.next = currH.next

                # if the new node is not inserted is not inserted at the end 
                if (currH.next != None):
                        new_nodex.next.prev = new_nodex

                currH.next = new_nodex
                new_nodex.prev = currH
        
        return headsreference;
        
#sort doublylinkedlist by insertionSort
def insertionSortingofDb( headsreference):

        # Initialize 'sorted' - a sorted doubly linkedlist
        sorted = None
        
        # iterate in the given doubly linked list
        # and insert every node to 'sorted'
        currp = headsreference
        while (currp != None) :

                # Store next for next iteration in current
                next = currp.next

                # removing all the links  because we have to create
                # 'curp' as a new node for  the insertion
                currp.prev = currp.next = None

                # insert curr in 'sorted' doubly linked list
                sorted = sortedInsertIntoDB(sorted, currp)

                # Update curr to next 
                currp = next
        
        # Update headsreference to point to
        # sorted doubly linked list
        headsreference = sorted
        #now return headsreference
        return headsreference

#insert node at beginning of list
def pushIntoDb(headsreference, newdata):

    #create the node with -1 as default value you can take anything becausewe need to change it later 
        newnodex = Node(-1)
        
    #assign the data to the node
        newnodex.data = newdata

    #make next to headsreference and prev to none
        newnodex.next = (headsreference)
        newnodex.prev = None

        # now change head to prev node to new node
        if ((headsreference) != None):
                (headsreference).prev = newnodex

        # move head to point to new node
        (headsreference) = newnodex
        return headsreference
        
#print doubly linked list
def printListdata(head):
    #interate untill head is not equal to null
        while (head != None) :
            # print the data without new line and with a separator " "
                print( head.data, end = " ")
                # advance the head pointer
                head = head.next
        

# let us test our code with few samples  of data in it
#start with empty doubly linked list
head = None
# insert  data into the doubly linkedlist
head = pushIntoDb(head, 23)
head = pushIntoDb(head, 43)
head = pushIntoDb(head, 53)
head = pushIntoDb(head, 78)
head = pushIntoDb(head, 92)
head = pushIntoDb(head, 80)

print( "Before insertion sort:")
printListdata(head)

#sort and take the head of doublylinkedlist 
headofdoublylinkedlist = insertionSortingofDb(head)

print("\nAfter insertion sort:")
printListdata(headofdoublylinkedlist)
4. Implement binary search algorithm recursively

#implementation of binarysearch
def binarysearch(arr, data):
        low = 0 # starting index
        high = len(arr) - 1 #ending index
        
        #iterate until low<=high
        while low <= high:
       #find mid
                mid = (high + low) // 2

                # If data is greater, ignore left half array
                if arr[mid] < data:
                        low = mid + 1

                # If data is smaller, ignore right half array
                elif arr[mid] > data:
                        high = mid - 1

                # it means data is present at mid index
                else:
                        return mid

        # If nothing is returned till now , then the element was not present return -1 from here
        return -1


#take the input inside array
array =list(map(int,input().split()))

# enter the data to be searched
data =int(input("enter data to be searched in sorted array:"))

#get the result of binarysearch in index varible
index = binarysearch(array, data)

# if index is not equal to -1 then print the index of data
if index != -1:
        print("data is present at index",index,"inside the array")
else:
        print("data is not present inside the array ")
5. Implement a recursive algorithm to find the nth fibonacci number using memoization

# Initialize array of dp
dp = [-1 for i in range(10)]
 
def fib(n):
    if (n <= 1):
        return n;
    global dp;
     
    # Temporary variables to store
    # values of fib(n-1) & fib(n-2)
    first = 0;
    second = 0;
 
    if (dp[n - 1] != -1):
        first = dp[n - 1];
    else:
        first = fib(n - 1);
    if (dp[n - 2] != -1):
        second = dp[n - 2];
    else:
        second = fib(n - 2);
    dp[n] = first + second;
 
    # Memoization
    return dp[n] ;
 
# Driver Code
if __name__ == '__main__':
    n = 9;
    print(fib(n));
6. Sort an array recursively using selection sort algorithm

# Recursive Python3 code to sort
# an array using selection sort
  
# Return minimum index
def minIndex( a , i , j ):
    if i == j:
        return i
          
    # Find minimum of remaining elements
    k = minIndex(a, i + 1, j)
      
    # Return minimum of current 
    # and remaining.
    return (i if a[i] < a[k] else k)
      
# Recursive selection sort. n is 
# size of a[] and index is index of 
# starting element.
def recurSelectionSort(a, n, index = 0):
  
    # Return when starting and 
    # size are same
    if index == n:
        return -1
          
    # calling minimum index function 
    # for minimum index
    k = minIndex(a, index, n-1)
      
    # Swapping when index and minimum 
    # index are not same
    if k != index:
        a[k], a[index] = a[index], a[k]
          
    # Recursively calling selection
    # sort function
    recurSelectionSort(a, n, index + 1)
      
# Driver code
arr = [3, 1, 5, 2, 7, 0]
n = len(arr)
  
# Calling function
recurSelectionSort(arr, n)
  
# printing sorted array
for i in arr:
    print(i, end = ' ')
7. Sort an array recursively using insertion sort algorithm

# Recursive Python program for insertion sort
# Recursive function to sort an array using insertion sort
  
def insertionSortRecursive(arr,n):
    # base case
    if n<=1:
        return
      
    # Sort first n-1 elements
    insertionSortRecursive(arr,n-1)
    '''Insert last element at its correct position
        in sorted array.'''
    last = arr[n-1]
    j = n-2
      
      # Move elements of arr[0..i-1], that are
      # greater than key, to one position ahead
      # of their current position 
    while (j>=0 and arr[j]>last):
        arr[j+1] = arr[j]
        j = j-1
  
    arr[j+1]=last
      
# A utility function to print an array of size n
def printArray(arr,n):
    for i in range(n):
        print arr[i],
  
# Driver program to test insertion sort 
arr = [12,11,13,5,6]
n = len(arr)
insertionSortRecursive(arr, n)
printArray(arr, n)