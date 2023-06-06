from os import system, name
import sys
import random
from math import exp
from copy import deepcopy
import time
import networkx as nx # For Graph Layout
import matplotlib.pyplot as plt # For drawing/visualizing graphs on screen

grid = []

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def prRed(skk): print("\033[91m {}\033[00m" .format(skk),   end="")
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk),   end="")
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk),   end="")
def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk),   end="")
def prPurple(skk): print("\033[95m {}\033[00m" .format(skk),   end="")
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk),   end="")
def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk),   end="")
def prBlack(skk): print("\033[98m {}\033[00m" .format(skk),   end="")

def initializeVariables_Nqueen(gridSize):
    global grid
    grid = [[0 for i in range(gridSize)] for j in range(gridSize)]

def constructResultantGrid(board):
    global grid
    for column, row in board.items():
        grid[row][column] = 1

def displayBoard(board):
    global grid
    constructResultantGrid(board)
    i = 1
    for row in grid:
        if(i < 10):
            print('\n' + str(i) + ":  ",  end="" )
        else:
            print('\n' + str(i) + ": ",  end="")

        for element in row:
            if(element == 1):
                prCyan('1 ')
            else:
                prLightGray(str(element) + ' ')
        i+=1
    print('\n')

def calculateThreat(n):
    if n < 2: # This means only 1 or no queens reside in the column so no threat
        return 0
    if n == 2: # This means 2 queens reside in the column so 1 threat
        return 1
    return (n - 1) * n / 2 # The rest n queens we can calculate an approximate threat level


def createBoard(n):
    # chessBoard = {0:0, 1:1, 2:2, 3:3, 4:4}
    # print(chessBoard[0])
    chessBoard = {}
    temp = list(range(n))
    random.shuffle(temp) # Reorganize the list
    column = 0

    while len(temp) > 0:
        row = random.choice(temp) # Randomly selects
        chessBoard[column] = row
        temp.remove(row)
        column += 1
    del temp
    return chessBoard


def calculateCost(chessBoard):
    '''Calculate how many pairs of threaten queen'''
    threat = 0
    chessBoardA = {}
    chessBoardB = {}

    for column in chessBoard:
        resultForChessBoardA = column - chessBoard[column] # column - row
        resultForChessBoardB = column + chessBoard[column]
        ''' Storing in local chessboards in two different specturms '''
        if resultForChessBoardA not in chessBoardA:
            chessBoardA[resultForChessBoardA] = 1 # Set the column index to 1 as only 1 queen is present here
        else:
            chessBoardA[resultForChessBoardA] += 1 # Add the queen in to the column, i.e queens are colliding
        if resultForChessBoardB not in chessBoardB:
            chessBoardB[resultForChessBoardB] = 1
        else:
            chessBoardB[resultForChessBoardB] += 1
    ''' Calculating threat levels '''
    for i in chessBoardA:
        threat += calculateThreat(chessBoardA[i])
    del chessBoardA

    for i in chessBoardB:
        threat += calculateThreat(chessBoardB[i])
    del chessBoardB

    # returning the total threat
    return threat


def simulatedAnnealing(queens, temperature):
    start = time.time()
    solutionFound = False
    resultantQueensCoordinates = createBoard(queens)
    prRed("Initial N-Queens Solution: ")
    displayBoard(resultantQueensCoordinates)
    initializeVariables_Nqueen(queens)

    # To avoid recounting when can not find a better state
    #print(resultantQueensCoordinates)
    calculatedCost = calculateCost(resultantQueensCoordinates)

    t = temperature
    decayRate = 0.80

    while t > 0:
        if((time.time() - start) > 3):
            prRed("Time has exceeded the set limit!\n")
            break
        t *= decayRate
        successor = deepcopy(resultantQueensCoordinates)
        # Randomly picking two coordinates for two queens
        while True:
            index1 = random.randrange(0, queens - 1)
            index2 = random.randrange(0, queens - 1)
            if index1 != index2:
                break
        successor[index1], successor[index2] = successor[index2], successor[index1]  # swap two chosen queens
        delta = calculateCost(successor) - calculatedCost # Successors cost - Current cost
        delta = -delta
        if delta > 0 or 1 > exp(delta / t): # Check delta or probability is smaller than 1 of the probability function
            resultantQueensCoordinates = deepcopy(successor)
            calculatedCost = calculateCost(resultantQueensCoordinates)
        if calculatedCost == 0: # Success condition satisfied
            solutionFound = True
            prGreen("Resultant N-Queens Solution: ")
            displayBoard(resultantQueensCoordinates)
            break
    if solutionFound is False:
        prRed("Failed")

def nqueensProblem():
    queens = int(input("Enter Number Of Queens: "))
    temperature = int(input("Enter Temperature: "))
    initializeVariables_Nqueen(queens)
    simulatedAnnealing(queens, temperature)
    
    

# The above function will only initialize the board
def initialize_Board():
    return [['_', '_', '_'],
            ['_', '_', '_'],
            ['_', '_', '_']]

Board = []
copy_Board = []

# just to print the board
def print_Board(Board):
    for row in Board:
        prLightGray('| ')
        for element in row:
            if(element == 'X'):
                prGreen('X ')
            elif(element == 'O'):
                prRed('O ')
            elif(element == '_'):
                prYellow('_ ')
        prLightGray('|\n')
    return

def player_Turn(Board):  # {
    count_player1 = 0
    count_player2 = 0
    for row in Board:  # {
        for counter in row:  # {
            if counter == 'X':  # {
                count_player1 = count_player1 + 1
                # }
            if counter == 'O':  # {
                count_player2 = count_player2 + 1
                # }
            # }
        # }
    return 'O' if count_player1 > count_player2 else 'X'

# The function will calculate the winning conditions otherwise it the program continue
def winning_Condtion(Board,ch):
    flag_row = flag_col = True
    for i in range(3):
        for j in range(3):
            if Board[j][i] != ch:
                flag_col = False
            if Board[i][j] != ch:
                flag_row = False

        if flag_col or flag_row:
            return True
        flag_row = True
        flag_col = True
# the above is for row and coloumn wining condition

    flag_row = flag_col = True
    for i in range(3):
        if Board[i][2-i] != ch:
            flag_row = False
        if Board[i][i] != ch:
            flag_col = False
    if flag_col or flag_row:
        return True
# the above is for diagonal wining condition

    return False


# The function will check the termination of our program
def terminate(Board):  # {
    flag = winning_Condtion(Board, 'X')
    if flag:
        return True
    flag = winning_Condtion(Board, 'O')
    if flag:
        return True
    # If nothing then this means there are empty states available
    for i in range(3):
        for j in range(3):
            if (Board[i][j] == '_'):
                return False
    # If empty states are also filled then it should terminate
    return True
    # }

# This is the utility function
def utility_Function(Board):
    flag = winning_Condtion(Board, 'X')
    if flag:
        return 1
    flag = winning_Condtion(Board, 'O')
    if flag:
        return -1
    return 0


# Return the empty spaces indexes list
def actions(Board):
    action_Move = list()
    for i, row in enumerate(Board):
        for j, col in enumerate(row):
            if col == '_':
                action_Move.append((i, j))
    return action_Move

# The function will put the turn in the respective position
def result(Board, coordinate):
    row, col = coordinate
    if (Board[row][col] == '_'):
        move = player_Turn(Board)
        copy_Board[row][col] = move
        return copy_Board
    else:
        raise Exception("Invalid Move")


def Max_Value_Pruning(state, Alpha, Beta):
    if terminate(state):
        return utility_Function(state) , None
    value = -1000
    best_Action = None
    actions_pos = actions(state)
    for a in actions_pos:
        Value_get = Min_Value_Pruning(result(state, a), Alpha, Beta)[0]
        if (Value_get > value):
            value = Value_get
            best_Action = a

        r, c = a
        state[r][c] = '_'
        if (value >= Beta):  # A condition for pruning
            return value, best_Action
        Alpha = max(Alpha, value)
    return value, best_Action


def Min_Value_Pruning(state, Alpha, Beta):
    if terminate(state):
        return utility_Function(state), None
    value = 1000
    best_Action = None
    actions_pos = actions(state)
    for a in actions_pos:
        Value_get = Max_Value_Pruning(result(state, a), Alpha, Beta)[0]
        if (Value_get < value):
            value = Value_get
            best_Action = a
        r, c = a
        state[r][c] = '_'
        if (value <= Alpha):  # A condition for pruning
            return value, best_Action
        Beta = min(Beta, value)
    return value, best_Action


def Alpha_Beta_Search(Board):
    prCyan("\nInitital State\n")
    print_Board(Board)
    global copy_Board
    while (True):
        if terminate(Board):
            break
        if (player_Turn(Board) == 'X'):
            value, Best_Move = Max_Value_Pruning(copy_Board, -1000, 1000) # -1 or 1 [The player X or Y] and coordinates
            R, C = Best_Move
            Board[R][C] = 'X'
            copy_Board = list(Board)

        elif (player_Turn(Board) == 'O'):
            value_get, Best_Move = Min_Value_Pruning(copy_Board, -1000, 1000)
            R, C = Best_Move
            Board[R][C] = 'O'
            copy_Board = list(Board)
            
        else:
            # Human vs Computer
            # row = int(input("Enter your Row = "))
            # col = int(input("Enter your Col = "))
            # Board[row][col] = 'O'
            # copy_Board = list(Board)
            # print_Board(Board)
            raise Exception("Error for Optimal Moves")
            
    if(utility_Function(Board) == 1):
        prGreen("\nX has won!\n")
    elif(utility_Function(Board) == -1):
        prRed("\nO has won!\n")
    else:
        prYellow("\nGame has been drawn!\n")
    print_Board(Board)

def ticTacToe():
    global Board, copy_Board
    Board = initialize_Board()
    copy_Board = initialize_Board()
    Alpha_Beta_Search(Board)
    
G = nx.DiGraph()# Graph type using networkx

numberOfNodes = 0
nodesList = []
nodeEdges = []
domains = ['red', 'green', 'blue'] # Red, Green, Blue

def initializeVariables_CSP():
    global numberOfNodes, nodesList, nodeEdges
    f = open("CSP.txt", "r")
    numberOfNodes = int(f.readline())
    nodesList = list(f.readline().split(' '))
    nodesList[len(nodesList)-1] = nodesList[len(nodesList)-1].strip()
    while True:
        data = f.readline()
        if data ==  '':
            break
        edge = data.split(' ')
        edge[len(edge)-1] = edge[len(edge)-1].strip()
        nodeEdges.append(edge)

def generateGraph(solution):
    global G, nodeEdges
    colors = []
    for state, color in solution.items():
        G.add_node(state)# Adding a node
        colors.append(color)
    for edge in nodeEdges: 
        G.add_edge(edge[0], edge[1])# Linking nodes
    pos = nx.spring_layout(G) # Setting layout

    nx.draw_networkx_nodes(G, pos) # Drawing nodes
    nx.draw_networkx_labels(G, pos) # Drawing labels
    nx.draw(G, pos, \
    node_size=1200, node_color=colors, linewidths=0.25, \
    font_size=10, font_weight='bold', with_labels=True, arrows=False)
    plt.show()


class Variable():
    def __init__(self, node, domain):
        self.node = node
        self.domain = domain

class Constraint():
    def __init__(self, edges): # Storing the edges
        # print(variables)
        self.edges = edges

    ''' Function to check if the neighbors have the same domain values '''
    def check(self, values):
        # print(values)
        if len(values) == 0: # That means there are no values thus no constraints
            return True
        v = None
        for val in values: # Assigns a single domain to the variable
            if v is None:
                v = val
            elif val == v: # Checks if the domain is already present returns false
                return False
        return True # If the domain is assigned and has no conflicts it returns true

# Returns a sub set of d with only the items whose key is in the keys array
# e.g d = {BU: R, RW: G}
#     keys = [BU, RW]  
def filterDictionary(d, keys):
    return {k: v for (k, v) in d.items() if k in keys}


# Filtering the values from the dictionaries
# d.items() = [BU: R]
# v = R
def dictionaryToArray(d):
    return [v for (k, v) in d.items()]


''' Merges the two sets[Elimintates the same sets and combines the different sets] '''
def union(d1, d2):
    d = d1.copy()
    d.update(d2)
    return d

class Problem():
    def __init__(self):
        self.variables = []
        self.constraints = []

    def addVariable(self, variable):
        self.variables.append(variable)

    def addConstraint(self, constraint):
        self.constraints.append(constraint)
        # for item in self.constraints:
        #     print(item.variables)
        # print(self.constraints[0].variables)

    def checkConsistency(self, assignment):
        for constraint in self.constraints:
            # Filtering the dictionary with just the matching node names
            relevantValues = filterDictionary(assignment, constraint.edges)
            '''
                Calling Check function to
                check if the neighbors have the same domain value
            '''
            if not constraint.check(dictionaryToArray(relevantValues)): 
                return False
        return True
    
    def find(self, assignment, variables):
        # print(assignment)
        vars = variables.copy()  # because it is passed by reference, we need to create a local copy
        if len(vars) == 0: # If there are no variables left return the assignment
            return [assignment]

        var = vars.pop() # Popping variables that are to be visited
        results = []
        for option in var.domain: # Taking out the available domain options i.e from [R, G, B]
            #print((assignment, {var.node: option}))
            # Eliminating repition and appending the different sets
            newAssignment = union(assignment, {var.node: option})
            ''' 
                 Now performing constraint satisfaction
                 Where we will be adding those assignment in to the final result
                 which donot have a conflict      
            '''
            if self.checkConsistency(newAssignment):
                '''
                    If there are no conflicts in neighbors domain values,
                    further proceed and recursively call this functions
                '''
                res = self.find(newAssignment, vars) 
                results += res
        return results

    def getSolutions(self):
        return self.find({}, self.variables.copy())

def mapColoring():
    initializeVariables_CSP()
    problem = Problem()

    for node in nodesList:
        problem.addVariable(Variable(node, domains))

    for edge in nodeEdges: 
        problem.addConstraint(Constraint(edge))

    solution = problem.getSolutions()[0]
    print(solution)
    generateGraph(solution)

def restartProgram():
    main()

def isInputCorrect(input, expectedOutput):
    for output in expectedOutput:
        if(input == output):
            return True
    return False

def showMenu():
    prYellow("\n 1. N Queens Problem Using Simulated Annealing\n")
    prGreen("2. TicTacToe Using Alpha Beta Pruning\n")
    prPurple("3. Map Coloring Using Constraint Satisfaction Problem\n")
    opt = int(input("Enter Option: "))
    if(isInputCorrect(opt, [1, 2, 3])):
        return opt 
    else:
        print("Invalid Input!")
        clear()
        showMenu()


def main():
    opt = showMenu()
    if(opt == 1):
        nqueensProblem()
    elif(opt == 2):
        ticTacToe()
    elif(opt == 3):
        mapColoring()
    conclusionQuestion = input("\nDo you want to exit the program?(Enter 'y' for yes or 'n' for no)")
    if(isInputCorrect(conclusionQuestion, ['y', 'n'])):
        if(conclusionQuestion == 'y'):
            exit(0)
        else:
            clear()
            restartProgram()

main()