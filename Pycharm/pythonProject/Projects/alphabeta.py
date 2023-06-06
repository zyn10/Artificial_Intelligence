# Tic Tac Toe
# Alpha-beta pruning
import numpy as obj_nmpy
# ------> for positive and negative infinity

class AlphaBeta:

    def __init__(self):
        print("\t<----TIC TAC TOE---->")

    # =============================================
    # ========      Initialize Board    ===========
    # =============================================

    def assignBoard(self):
        return [['_', '_', '_'],
                ['_', '_', '_'],
                ['_', '_', '_']]
    # =============================================
    # ============    DRAW BOARD      =============
    # =============================================

    def drawBoard(self, Board):
        for row in Board:
            print('\t| ' + ' | '.join(row) + ' |')
        return
    # =============================================
    # ========   Switching player       ===========
    # =============================================

    def switchPlayerTurn(self, Board):
        count_player1 = 0
        count_player2 = 0

        for row in Board:
            for counter in row:
                if counter == 'X':
                    count_player1 = count_player1 + 1
                elif counter == 'O':
                    count_player2 = count_player2 + 1

        return 'O' if count_player1 > count_player2 else 'X'
    # =============================================
    # ========  Check Win or To be continue =======
    # =============================================

    def checkWin(self, Board, ch):
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




        for i in range(3):
            if Board[i][2 - i] != ch:
                flag_row = False
            if Board[i][i] != ch:
                flag_col = False
        if flag_col or flag_row:
            return True

        return False
    # =============================================
    # ==========   Done or Not         ============
    # =============================================

    def terminate(self, Board):
        flag = self.checkWin(Board, 'X')
        if flag: # ---> true
            print()
            self.drawBoard(Board)
            return True
        flag = self.checkWin(Board, 'O')
        if flag:
            return True
        # ------------->else all are  empty states
        for i in range(3):
            for j in range(3):
                if Board[i][j] == '_':
                    return False
        # ----------> hogya pora board no empty state
        return True
    # =============================================
    # ========      Utility Function      =========
    # =============================================

    def uFunction(self, Board):
        flag = self.checkWin(Board, 'X')
        if flag:
            return 1
        flag = self.checkWin(Board, 'O')
        if flag:
            return -1
        return 0
    # =============================================
    # ========      Move Move Move        =========
    # =============================================

    def move(self, Board):
        move = list()
        for i, row in enumerate(Board):
            for j, col in enumerate(row):
                if col == '_':
                    move.append((i, j))
        return move
    # =============================================
    # ========      Check and Place       =========
    # =============================================

    def result(self, Board, coordinate):
        row, col = coordinate
        if Board[row][col] == '_':
            move = self.switchPlayerTurn(Board)
            copy_Board[row][col] = move
            return copy_Board
        else:
            print("Invalid Move")
    # =============================================
    # ========       Max Pruning          =========
    # =============================================

    def maxValue(self, state, Alpha, Beta):
        if self.terminate(state):
            return self.uFunction(state), None

        value = -obj_nmpy.inf  # -----> negative infinity

        best_Action = None
        actions_pos = self.move(state)

        for a in actions_pos:
            Value_get = self.minValue(self.result(state, a), Alpha, Beta)[0]
            if Value_get > value:
                value = Value_get
                best_Action = a

            r, c = a  # ----> row col action
            state[r][c] = '_'
            if value >= Beta:
                return value, best_Action
            Alpha = max(Alpha, value)
        return value, best_Action
    # =============================================
    # ========       Min Pruning          =========
    # =============================================

    def minValue(self, state, Alpha, Beta):
        if self.terminate(state):
            return self.uFunction(state), None
        value = obj_nmpy.inf # ---------> positive infinity
        best_Action = None
        actions_pos = self.move(state)
        for a in actions_pos:
            Value_get = self.maxValue(self.result(state, a), Alpha, Beta)[0]
            if Value_get < value:
                value = Value_get
                best_Action = a

            r, c = a    # ----> row col action
            state[r][c] = '_'
            if value <= Alpha:  # A condition for pruning
                return value, best_Action
            Beta = min(Beta, value)
        return value, best_Action

    # =============================================
    # ========       Min Pruning          =========
    # =============================================
    def Alpha_Beta_Search(self, Board):
        global copy_Board
        while True:
            if self.terminate(Board):
                print("\n\nboard terminate")
                self.drawBoard(Board)
                return None
            if self.switchPlayerTurn(Board) == 'X':
                value, Best_Move = self.maxValue(copy_Board, -obj_nmpy.inf, obj_nmpy.inf)
                R, C = Best_Move
                Board[R][C] = 'X'
                copy_Board = list(Board)
                print()
                self.drawBoard(Board)
            elif self.switchPlayerTurn(Board) == 'O':
                value_get, Best_Move = self.minValue(copy_Board, -obj_nmpy.inf, obj_nmpy.inf)
                R, C = Best_Move
                Board[R][C] = 'O'
                copy_Board = list(Board)
                print()
                self.drawBoard(Board)
            else:
                raise Exception("Error for Optimal Moves")


obj = AlphaBeta()
Board = obj.assignBoard()
copy_Board = obj.assignBoard()
obj.Alpha_Beta_Search(Board)
