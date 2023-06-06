from constraint import *
z = Problem()
z.addVariable("a",[2,4,6,8,10,12])
z.addVariable("b",[3,6,12,15])
z.addConstraint(lambda a, b: a == b & a==6,("a","b"))

print(z.getSolutions(),end= " ")