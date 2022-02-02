#AVI ROY


# TASK:1 -
def shiftLeft(source, k):
    for a1 in range(0, len(source) - k):

        if (a1 + k < len(source)):
            source[a1] = source[a1 + k]
        else:
            source[a1] = 0

    for a1 in range(len(source) - k, len(source)):
        source[a1] = 0

    print(source)


sourc e= [10 ,20 ,30 ,40 ,50 ,60]

shiftLeft(source ,3)


# TASK:2-
def rotateLeft(source ,k):
    for ar1 in range(len(source)):
        if (ar 1 + k <len(source)):

            j = source[ar1]

            source[ar1 ] =source[ar 1 +k]
            source[ar 1 +k ] =j
    print(source)
source = [10 ,20 ,30 ,40 ,50 ,60]
rotateLeft(source ,3)


# TASK:3-


def remove(source ,size ,idx):

    if (id x> =0 and siz e> =idx):
        while (size >= idx):
            source[idx] = source[id x +1]
            idx + =1
        source[siz e -1] =0
        print(source)
    if 0 in source:
        size = source.index(0)
        funct = True

    else:
        funct = False


source = [10, 20, 30, 40, 50, 0, 0]
remove(source, 5, 2)


# TASK:4-
def removeAl(source, size, element):
    x = 0
    new = []
    for i in source:
        if element == i:
            x += 1
        if i != element:
            new += [i]
    for i in range(x):
        new += [0]
        if 0 < i < len(source):
            source[i] = new[i]
    print(new)


source = [10, 2, 30, 2, 50, 2, 2, 60, 0, 0]
removeAl(source, 8, 2)


# TASK:5-

def splitnarray(as1, sb1):
    i = sb1
    left = as1[:i - 1]
    right = as1[i:len(as1) - 1]
    if left == right:
        return True
    else:
        return False


source = [1, 1, 1, 2, 1]
print(splitnarray(source, 2))


# TASK:6-


def narrayserieS(n):
    s = [0] * n * n
    k = 0
    Createn = n
    ar1 = 0
    while ar1 < len(s):
        ar1 = ar1 + 1
        for ar2 in range(1, Createn + 1):
            s[k] = ar2
            k += 1
        if (Createn < n):

            for ar2 in range(0, n - Createn):
                if k == n * n:
                    break
                s[k] = 0
                k += 1
        Createn -= 1

    s = s[::-1]

    print(s)


narrayserieS(4)


# TASK:7-
def mBunchA(ar):
    c = 0
    high1 = 1
    for i in range(len(ar)):
        if ar[i] == ar[i - 1]:
            c = c + 1
        else:
            c = 1
        if high1 < c:
            high1 = c

    print(high1)


ar = [1, 1, 2, 2, 1, 1, 1, 1]
mBunchA(ar)


# TASK:8-
def repetition(ar):
    couT = {}
    for prod in ar:
        if prod not in couT:
            if ar.count(prod) > 1:
                couT[prod] = ar.count(prod)
    total = 0
    s1 = 0
    for i in couT.values():
        total += i
        s1 += 1
    average = total / s1

    for check in couT.values():
        if check == average:
            return True

        else:
            return False


source = [3, 4, 6, 3, 4, 7, 4, 6, 8, 6, 6]
repetition(source)


# TASK:9-
def palindrome(cirnar, start, size):
    index = start
    sour1 = [0] * size
    for ar1 in range(0, size):
        sour1[ar1] = cirnar[index]
        index = (index + 1) % len(cirnar)

    if sour1 == sour1[::-1]:
        print('True')
        pass

    else:
        print('False')


source = [10, 20, 0, 0, 0, 10, 20, 30]
palindrome(source, 5, 5)


# TASK:10-
def Intersection(cirnarr, start, size, cirnarr1, start1, size1):
    ar1 = 0
    indexI = start
    result = []

    while (ar1 < size):
        ar2 = 0
        indexII = start1
        while (ar2 < size1):

            if (cirnarr[indexI] == cirnarr1[indexII]):
                result.append(cirnarr[indexI])
            indexII = (indexII + 1) % len(cirnarr1)
            ar2 += 1

        indexI = (indexI + 1) % len(cirnarr)
        ar1 += 1

    print(result)


input1 = [40, 50, 0, 0, 0, 10, 20, 30]
input2 = [10, 20, 5, 0, 0, 0, 0, 0, 5, 40, 15, 25]
Intersection(input1, 5, 5, input2, 8, 7)

# TASK:11-

# 3. Musical Chair game
import random


# Function for chair rotation
def rotate_chair(list):
    temp = list[0]
    for i in range(0, len(list)):
        if (i == len(list) - 1):
            list[i] = temp
        else:
            list[i] = list[i + 1]
    return list


# function for select the winner
def musical_chair_game(list):
    loop = True
    while (loop == True):
        if len(list) == 1:
            print()
            print("-----GAME OVER-----")
            print("Name of the Winner:", "Participant", list[0])
            loop = False
        else:
            random_number = random.randint(0, 3)
            rotate_chair(list)
            if random_number == 1:
                eleminate = len(list) // 2
                print("Stop Music")
                print("Eliminate Participant No.:", list[eleminate])
                list.pop(eleminate)


# participants_list is used for mentioning the participants
participants_list_as_number = [1, 2, 3, 4, 5, 6, 7]
participants_list_as_name = ["Mita", "Hia", "Keya", "Pushpita"]
print("Game 01")
musical_chair_game(participants_list_as_number)
print("Game 02")
musical_chair_game(participants_list_as_name)

