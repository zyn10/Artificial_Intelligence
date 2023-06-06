#list inside Functions
def list2Sum(list_1,list_2):
    counter= max(len(list_2),len(list_1))
    list_3=[]
    for x in range(counter):
        temp=(list_1[x] + list_2[x])
        list_3.append(temp)
        print(list_1[x], " + ", list_2[x], " = ", list_3[x])
    return list_3


list1 = [11, 22, 33, 44, 21, 54, 67, 54, 33, 222, 4]
list2 = [3, 4, 5, 32, 21, 33, 66, 75, 87, 97, 1]
list3 = list2Sum(list1, list2)

