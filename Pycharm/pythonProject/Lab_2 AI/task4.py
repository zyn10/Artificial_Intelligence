#String Manipulatioin
string1="HELLO WORLD"
string2="HOW,arE yOu"

def concatenate():
    print("After Concatenation ",string1+string2)
def UpperLower():
    print(string1.upper())
    print(string2.upper())
    print(string1.lower())
    print(string2.lower())


concatenate()
UpperLower()

print(string1)
print(string2)

print("The String 1 After Slicing: ", end="")
print(string1[5:].replace(" ", ""))

print("The String 2 After Slicing: ", end="")
print(string2[-5:-1].replace(" ", ""))