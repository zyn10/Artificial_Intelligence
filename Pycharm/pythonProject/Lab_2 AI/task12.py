#armstrong number

def checkArmstrong(input):
    sum=0
    temp=input
    while temp > 0:
        digit=temp%10#extracting each elemnent
        sum= sum+(digit**3)#taking cube of each digit and taking there sum
        temp=temp//10#removing digit from number
    return  sum

Num=int(input("Input a number to check weather it si armstrong or not"))
checker=checkArmstrong(Num)
if checker==Num:
    print("Yes This is Armstrong Number")
else:
    print("No this is not Armstrong Number")