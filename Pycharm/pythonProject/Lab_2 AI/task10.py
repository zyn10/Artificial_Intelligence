#empty list using while loop
list = [ 1, 4, 56, 2, 4 , 12, 6, 89 ,11, 0]
counter=len(list)-1

while counter>0:
    print("Deleting ...", list.pop(counter)," ",len(list) ," ",counter)
    counter=counter-1

if counter == 0:
    print("List is empty.....")