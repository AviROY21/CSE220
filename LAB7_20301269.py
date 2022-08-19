#NAME: AVISHEK ROY SPARSHO
#ID:20301269
#sec:02



#task 1

class keyINDEX:
    def __init__(self,a):
        self.k=[]
        self.negativeValue=0
        minimum=a[0]
        maximum=a[0]
        for value in a[1:]:
            if value<minimum:
                minimum=value
            if value>maximum:
                maximum=value

        if minimum<0:
            self.negativeValue=minimum*(-1)
        self.k=[0]*(maximum + self.negativeValue+1)
        for value in a:
            self.k[value+self.negativeValue]+=1


    def search(self,value):
        if value+self.negativeValue <len(self.k) and self.k[value+self.negativeValue]:
            return True
        else:
            return False


    def sort(self):
        sortedArray=[]
        for x in range(len(self.k)):
            for nTimes in range(self.k[x]):
                y=x-self.negativeValue
                sortedArray.append(y)
        return sortedArray


def tester():

    test=keyINDEX([-1,20,-10,10,-3,6,9])
    print(test.search(10))
    print(test.search(91))
    print(test.sort())
    test=keyINDEX([-1,-2,10,5,40,68,50])
    print(test.search(50))
    print(test.search(29))
    print(test.sort())
tester()












#TASK-2
class Hashtable:
    def __init__(self, strings: list):
        self.strings = strings
        self.Hashtable = [None] * 10

    def hash(self, string):

        string = string.upper()
        total_number_of_consonants = 0
        summation_of_the_digits = 0

        for letter in string:
            if letter in 'BCDFGHJKLMNPQRSTVWXYZ':
                total_number_of_consonants += 1
            elif letter in '0123456789':
                summation_of_the_digits += int(letter)

        return (total_number_of_consonants * 24 + summation_of_the_digits) % 9

    def linearpobing(array, element, index):
        while array[index] is not None:
            index = (index + 1) % len(array)
        array[index] = element

    def hashTable(self):
        for x, string in enumerate(self.strings):
            index = self.hash(string)
            self.linearpobing(x, index)
        return self.hashTable


if __name__ == '_main_':
    string1 = ['ST1E89B8A32']
    hashTable = Hashtable(string1)
    table = hashTable.hashTable()
    for x, value in enumerate(table):
        print(f"{x}:\t{value}")


