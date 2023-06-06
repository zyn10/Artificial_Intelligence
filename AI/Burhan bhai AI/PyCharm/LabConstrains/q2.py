#18F-0326 Abdul Salam Wasti

from constraint import *

def q2sol():
    print("\nQuestion 02")
    problem = Problem()
    problem.addVariable("a", [2, 4, 6, 8, 10, 12])
    problem.addVariable("b", [3, 6, 12, 15])
    sol = problem.getSolution()
    print("without contraints", sol)
    problem.addConstraint(lambda a, b: a == b and a == 6, ("a", "b"))
    sol = problem.getSolution()
    print("with contraints", sol)
    print("----------------------------------------------\n")