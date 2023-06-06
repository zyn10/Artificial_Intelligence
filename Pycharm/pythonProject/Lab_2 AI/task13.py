#Factorial Code
def Factorial(input):
#first we will define the base case
    if input==1:
        return 1
#Recurssion ...main muda
    else:
        return (input*Factorial(input-1))

print("Factorial Calculator")
Num=int(input("Input Number to get Factorial : "))
if Num<0:
    print("Factorial Not exist of negative number")
else:
    Ans=Factorial(Num)
    print("The Factorial of ",Num," is ",Ans)