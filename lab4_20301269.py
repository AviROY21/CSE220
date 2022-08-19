#AVI ROY

#TASK1
openBracket=['[','(','{']
closedBracket=[']',')','}']
expresssion="1+2]*[3*3+{4–5(6(7/8/9)+10)–11+(12*8)]+14"
sTACK=[]
count=1
for x in expresssion:
    if x in openBracket:
        sTACK.append(x)
    if x in closedBracket:
        if (len(sTACK)==0):
            print('This is expression is NOT correct')
            print("Error at character '#{}.'-not closed.".format(expresssion.index(x)+1,x))
            count=0
            break
        poOpped=sTACK.pop()
        if ((poOpped not in openBracket) or (openBracket.index(poOpped) != closedBracket.index(x))):
            print('This expression is NOT correct.')
            print("Error at character #{}.'{}'-not closed. ".format(expresssion.index(poOpped)+1,poOpped))
            count=0
            break
if (count==1):
    print('This expression is correct')


#TASK2
class Node:
    def __init__(self,info):
        self.next=None
        self.info=info
class STACK:
    def __init__(self):
        self.head=None
    def push(self,info):
        if self.head is None:
            self.head=Node(info)
        else:
            Node1=Node(info)
            Node1.next=self.head
            self.head=Node1
    def pop(self):
        if self.head is None:
            return None
        else:
            poOpped=self.head.info
            self.head=self.head.next
            return poOpped
linkL_stack=STACK()
openBracket=['[','(','{']
closedBracket=[']',')','}']
expression="1+2*[3*3+{4–5(6(7/8/9)+10)}–11+(12*8)/{13+13}]+14"
count=1
for x in expression:
    if x in openBracket:
        linkL_stack.push(x)
    if x in closedBracket:
        poOpped=linkL_stack.pop()
        if poOpped is None:
            print('This is expression is NOT correct')
            print("Error at character '#{}.'-not closed.".format(expression.index(x)+1,x))
            count=0
            break
        elif ((poOpped not in openBracket) or (openBracket.index(poOpped) !=closedBracket.index(x))):
            print('This expression is NOT correct.')
            print("Error at character #{}.'{}'-not closed. ".format(expression.index(poOpped)+1,poOpped))
            count=0
            break
if(count==1):
    print('This expression is correct')