#Dsorting

def dsort(List):
    counter = len(List)
    temp = None
    for x in range(counter):
        for y in range(counter):
            if (List[x] > List[y]):
                temp = List[x]
                List[x] = List[y]
                List[y] = temp


print("\t\t***Descending Order***")
list_ = [5, 6, 7, 23, 12, 3, 3, 4, 5, 12, 34]
print("Before Sorting ......\n",list_)
dsort(list_)
print("After Sorting.........\n",list_)

