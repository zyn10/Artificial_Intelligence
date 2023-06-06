#Reverse a number

def ReverseNumber(input):
    Reverse=0
    while(input>0):
        Remainder = input%10
        Reverse=(Reverse*10)+Remainder
        input= input//10

        #The single division operator behaves abnormally generally for very large numbers.
        #The Double Division operator in Python returns the floor value for both integer and floating-point arguments after division

    print("Reversed Number = ", Reverse)
print("lets reverse the number")
number=int(input("\nInput a number : "))

ReverseNumber(number)