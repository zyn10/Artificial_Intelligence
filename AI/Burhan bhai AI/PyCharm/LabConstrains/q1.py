#18F-0326 Abdul Salam Wasti

from constraint import *

def q1sol():
    print("\nQuestion 01")
    problem = Problem()
    problem.addVariable("a", [1, 2, 3])
    problem.addVariable("b", [4, 5, 6])
    sol = problem.getSolution()
    print("without contraints", sol)
    problem.addConstraint(lambda a, b: a != b, ("a", "b"))
    sol = problem.getSolution()
    print("with contraints", sol)
    print("----------------------------------------------\n")