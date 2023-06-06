class queensProblem:

    def __init__(self, N):
        self.queens = N
        self.board = [[0 for y in range(N)] for x in range(N)]
        self.queenCol = [-1 for y in range(N)]
        self.iteration = 0


    def conditionCheck(self, queenCol, queenRow):
        noConflict = True

        for x in range(self.queens):
            if x+queenCol < self.queens:
                col = x + queenCol
                if x+queenRow < self.queens:
                    row = x+queenRow
                    if self.board[row][col] != 0 and (row != queenRow and col != queenCol):
                        noConflict = False
                        return noConflict
                if queenRow-x >= 0:
                    row = queenRow-x
                    if self.board[row][col] != 0 and (row != queenRow and col != queenCol):
                        noConflict = False
                        return noConflict

            if queenCol-x >= 0:
                col = queenCol - x
                if x+queenRow < self.queens:
                    row = x+queenRow
                    if self.board[row][col] != 0 and (row != queenRow and col != queenCol):
                        noConflict = False
                        return noConflict
                if queenRow-x >= 0:
                    row = queenRow-x
                    if self.board[row][col] != 0 and (row != queenRow and col != queenCol):
                        noConflict = False
                        return noConflict
        return noConflict

    def printBoard(self):
        for x in range(self.queens):
            for y in range(self.queens):
                print(self.board[x][y], end=" ")
            print(" ")

    def solveQuens(self, queen, board, reqIteration):

        self.iteration += 1
        if queen >= self.queens:
            return True
        if self.iteration+1 > reqIteration:
            return False

        solutionFound = False
        for selectedRowQueen in range(self.queens):

            if self.iteration + 1 > reqIteration:
                return False

            if selectedRowQueen not in self.queenCol:
                self.queenCol[queen] = selectedRowQueen
                self.board[queen][selectedRowQueen] = 1


                solutionFound = self.conditionCheck(selectedRowQueen,queen)
                #self.printBoard()
                #j = input()
                #print("----------------------------------------------")
                if solutionFound:
                    solutionFound = self.solveQuens(queen+1, board, reqIteration)
                if not solutionFound:
                    self.queenCol[queen] = -1
                    self.board[queen][selectedRowQueen] = 0

        return solutionFound

    def findSolution(self, totalIteration):

        solution = self.solveQuens(0,self.board, totalIteration)
        if solution:
            print("Solution Found in " + str(self.iteration-1) + " iterations::")
            self.printBoard()
            #print("--------------------------------")
        else:
            print("Solution Not-Found  in " + str(self.iteration) + " iterations::")