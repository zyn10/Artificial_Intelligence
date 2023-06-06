#list with random numbers
import random

list=[]
def populateList(num):
    for i in range(num):
        list.append(random.randint(0,100))
    print("After Populating with Random Numbers\n",list)

def findMax(num):
    max = 0
    counter = 0
    for i in range(num):
        if max < list[i]:
            max = list[i]
            counter = counter + 1
        else:
            counter = counter + 1
    print("Maximum Value\t= ", max)
    return max
def findMin(max,size):
    min = max
    counter = 0
    for i in range(size):
        if min > list[i]: 
            min = list[i]
            counter = counter + 1
        else:
            counter = counter + 1
    print("Minimum Value\t= ", min)

# print("Random Number Generator")
size=int(input("Input the Size of the list : "))
populateList(size)
max=findMax(size)
findMin(max,size)