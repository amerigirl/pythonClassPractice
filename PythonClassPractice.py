#very basic python operations
# add() extend()--> adds element from another list, (remove(), pop())--> both removes
# accessing is the same (via index), iterating, loop: for...in..
listA = []

listA.append("apple")
print(listA)
listA.append("orange")
listA.append(230)
print(listA)
print(listA[0])
print(listA.remove(230))
print(listA)
print(len(listA))

#write a function that can add digits in a number and return the sum.
# 234    add 2 + 3 + 4 = 9

def sum(num):
    result = 0
    while (num > 0):
        result += num % 10
        num //= 10  #integer division in python
    return result

print(sum(234))
#------------------------------------------
import ctypes
#lets create list functionalities from scratch

class CreateList:

#making the array
    def __init__(self): #this is a dunder method: special one with __ on both sides
        self.size = 1
        self.n = 0 # same as setting a var to zero in javascript
        self.A = self.__make_array(self.size)


#finding/returning the length
    def __len__(self): #this is a dunder method: special one with __ on both sides
        return self.n


#increasing the size/appending
    def append(self, item):
        if self.n == self.size:
            self.__resize(self.size * 2)


#remove from a list

    def remove(self, item):
        #first locate the item
        position = self.find(item)
        if type(position) is not None:
            self.__delitem__(position)

#get an item

    def __getitem__(self, index): #this is a dunder method: special one with __ on both sides
        if 0 <= index < self.n:
            return self.A[index]
        else:
            return 'IndexError'

