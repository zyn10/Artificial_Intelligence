#Arithmatic Functions

def Sum():
    var1=float(input("Input 1st operand "))
    var2 = float(input("Input 2nd operand "))
    print("The sum of two numbers is ", var1+var2)

def Sub():
    var1=float(input("Input 1st operand "))
    var2 = float(input("Input 2nd operand "))
    print("The difference of two numbers is ", var1-var2)
def Multiply():
    var1=float(input("Input 1st operand "))
    var2 = float(input("Input 2nd operand "))
    print("The Product of two numbers is ", var1*var2)
def Divide():
    var1=float(input("Input 1st operand "))
    var2 = float(input("Input 2nd operand "))
    print("The Quotient is ", var1/var2)
    print("The Remainder is ", var1 % var2)
def Square():
    var = float(input("Input operand "))
    print("The Square is ",var**2)
def Cube():
    var = float(input("Input operand "))
    print("The Cube is ",var**3)

print("**Airthmatic Calculator**")
print(" *Test all operations*")

print("=> Addition\n=> Subtraction\n=> Multiplication\n=> Division\n=> Square\n=> Cube\n")