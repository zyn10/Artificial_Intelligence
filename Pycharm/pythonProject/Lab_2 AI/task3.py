#Value Manipulation

def manipulation(one,two,three):
    one=one+5
    two=two+10
    three=three+15
    return one, two, three

var1 = float(input("Input 1st operand "))
var2 = float(input("Input 2nd operand "))
var3 = float(input("Input 3rd operand "))
#we can show the returning values in couple of ways
# 1) store it in respective variables & print each
# 2) Direct print the returning values
var1,var2,var3=manipulation(var1, var2, var3)
print(var1,var2,var3)
# lets test both ways
print(manipulation(var1, var2, var3))

