# creating dictionary
import random
listAdd=[]
Dictionary = {
        "brand": "Samsung",
        "os-type": "Oreo",
        "color": "black",
        "camera": "42 megapixels",
        "year": 2012,
        "sizes":[]
            }
def addList(size):
    for i in range(size):
        listAdd.append(random.randint(0,100))
size=int(input("Input the size of the list : "))
addList(size)
print("Dictonary Before Addition...\n",Dictionary)
Dictionary["sizes"].append(listAdd)
print("Dictonary After Addition...\n",Dictionary)
del Dictionary['year']
print("Dictonary After Deletion...\n",Dictionary)
print(sorted(Dictionary))