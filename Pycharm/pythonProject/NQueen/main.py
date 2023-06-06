class NQueen:
    def __init__(self, in_rows, in_cols, in_queens):
        self.row = in_rows
        self.col = in_cols
        self.queen = in_queens
        self.board=[self.row][self.col]

    def setBoard(self):
        for i in range(self.row-1):
            for j in range(self.col-1):
                self.board[i][j].insert(0)

    def drawBoard(self):
        for i in range(self.row):
                print("\n",self.board,end=" ")





    def checkSafeness(self):
        pass
        # # ----> checking for rows
        # for i in self.row:
        #     if(self.board[row][i]==1):
        #         print (board[][])






obj=NQueen(5,5,5)
obj.setBoard()
obj.drawBoard()
obj.checkSafeness()



