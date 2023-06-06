#list addition and removal

list = ["apple", "cherry", "orange", "kiwi", "melon", "mango"]
print("Items in list...")
print(list)
print("Removing cherry and melon....")
list.remove("cherry")#removal by name \ value
list.remove("melon")
print(list)
print("Adding banana in second last slot")
list.insert(-1,"banana")
#-1 indicates last element
# we are adding infront of last element so second last
print(list)