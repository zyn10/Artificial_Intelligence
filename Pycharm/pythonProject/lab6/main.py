from itertools import permutations
def generateallsol():
    li = ['A','B','C','D']
    li.extend(['A'])
    solutions = [x for x in set(permutations(li))
                 if x[0] == 'A' and x[-1] == 'A']
    print("Possible Pairs :")
    print(solutions)

generateallsol()



