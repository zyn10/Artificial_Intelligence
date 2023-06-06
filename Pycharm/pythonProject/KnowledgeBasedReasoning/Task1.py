from kanren import run,eq,var
x=var()
z=var()

print("Value of Z : ",run(1, x, eq(x,z) ,eq(z,3)))
