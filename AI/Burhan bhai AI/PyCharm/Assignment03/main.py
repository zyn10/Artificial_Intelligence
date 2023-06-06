from tictactoeMinmaxQ1 import  *
from queensproblemSimulatingAnealingQ2 import *
from coloringproblemCSP import *


if __name__ == '__main__':
    print("Assignment 03:\n")

    print("TicTacToe Q1\n")
    comp1 = player(1)
    comp2 = player(2)
    game = ticTacToe()
    game.playGame(comp1,comp2)

    ########################################################################

    print("------------------------------------\n\nQueens Problem Q2")
    x = queensProblem(5)
    x.findSolution(15)

    ########################################################################

    print("-------------------------------------\n\nCSP Coloring Problem Q3")
    q = colorProblem()
    q.findSolution("DJ")