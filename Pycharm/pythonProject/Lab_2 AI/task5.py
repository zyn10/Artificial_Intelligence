#EVEN ODD using for and while

print("Lets print even and odd Numbers")
starting = int(input("\nInput a starting value : "))
ending   = int(input("Input a ending value     : "))
EvenArray=[]
OddArray=[]
print("\n Using For Loop")
for x in range(starting,ending):
    if(x%2==0):
        EvenArray.append(x)
    else:
        OddArray.append(x)

print("For Even : ", EvenArray)
print("For ODD  : ", OddArray)
print("\n Using While Loop")
EvenArray=[]
OddArray=[]

while starting < ending:
    if(starting%2==0):
        EvenArray.append(starting)
        starting+=1
    else:
        OddArray.append(starting)
        starting += 1

print("While Even : ", EvenArray)
print("While ODD  : ", OddArray)
