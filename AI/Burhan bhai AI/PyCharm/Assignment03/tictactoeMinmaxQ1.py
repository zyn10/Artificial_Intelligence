import copy
import random
from graphics import  *


#using 1 for player 1 & and 2 for player 2

def playerWin(board):
    winMask = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    result = 0  #tie
    for i in winMask:
        if board[i[0]] == board[i[1]] and board[i[1]] == board[i[2]] and board[i[0]] != 0:
            result = board[i[0]]

    if result == 0 and 0 not in board:
        result = 3

    return result

def minmax(board, depth, alpha, beta, maximingPlayer, player):
    result = playerWin(board)

    if result != 0:

        if result == 3:
            print("tie => ", end="")
            print(board)
            result = 0
        elif result == player:
            print("won => ", end="")
            print(board)
            result = 1 * depth
        else:
            print("lost => ", end="")
            print(board)
            result = -1 * depth
        return result

    if maximingPlayer:
        p = 1 if player == 2 else 2
        chilList = []
        for i in range(len(board)):
            if board[i] == 0:
                child = copy.deepcopy(board)
                child[i] = p
                chilList.append(child)

        #print(chilList)
        maxEval = -999
        for children in chilList:
            eval = minmax(children, depth+1, alpha, beta, False, player)
            maxEval = max(maxEval,eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        print("----------------------------------")
        return maxEval

    else:
        p = 1 if player == 2 else 2
        chilList = []
        for i in range(len(board)):
            if board[i] == 0:
                child = copy.deepcopy(board)
                child[i] = player
                chilList.append(child)

        minEval = 999
        for children in chilList:
            eval = minmax(children, depth+1 , alpha, beta, True, player)
            minEval = min(minEval,eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval

class player:

    def __init__(self, id):
        self.playerID = id

    def chooseMove(self,board):
        moves = []

        for i in range(len(board)):
            if board[i] == 0:
                newBoard = copy.deepcopy(board)
                newBoard[i] = self.playerID
                x = minmax(newBoard,1, -999, 999, True, self.playerID)
                moves.append(x)
            else:
                moves.append(0)
            #print("--------------------------------------------------------------")

        sameMoves = []
        win = 999
        winIndex = -1
        tieIndex = -1
        counter = 0
        for x in moves:
            if win == x:
                sameMoves.append(counter)
            if x > 0 and x < win:
                win = x
                winIndex = counter
                sameMoves.clear()
                sameMoves.append(winIndex)
            if board[counter] == 0 and x == 0 and tieIndex == -1:
                tieIndex = counter
            counter +=1

            #print("----------------------------------------------------------")
        print(moves)


        if winIndex != -1:
            winIndex = random.choice(sameMoves)
            return winIndex
        return tieIndex


class ticTacToe:

    board = [2, 1, 0, 2, 0, 0, 1, 0, 0]
    #board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def printBoard(self):
        counter = 0
        for x in self.board:
            if x == 0:
                x = " "
            elif x == 1:
                x = "*"
            elif x == 2:
                x = "%"

            print(x, end="")
            counter += 1
            if (counter%3 == 0):
                print("\n----------")
            else:
                print(" | ", end="")

    def playGame(self, player1,player2):
        playerTurn = 2

        result = playerWin(self.board)
        while result == 0:
            newBoard = copy.deepcopy(self.board)
            if playerTurn == 1:
                print("Player "+ str(playerTurn) +":")
                blockChoosed = player1.chooseMove(newBoard)
                self.board[blockChoosed] = 1
                playerTurn = 2
            else:
                print("Player " + str(playerTurn) + ":")
                blockChoosed = player2.chooseMove(newBoard)
                self.board[blockChoosed] = 2
                playerTurn = 1
            result = playerWin(self.board)
            self.printBoard()
            f = input()
            #print("----------------------------------------")
        if result == 3:
            print("Tie - No one wins")
        else:
            if playerTurn == 1:
                print("-- Player 2 won --")
            else:
                print("-- Player 1 won --")




