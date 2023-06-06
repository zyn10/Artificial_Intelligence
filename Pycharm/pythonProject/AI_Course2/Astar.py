# Robot Navigation System
class Robot:
    def __init__(self):
        self.board_Array = []
        self.exploredlist = []
        self.checkArray = [False] # if explored or not
        self.sahiWalaPath = []
# ======================================================
# ====== R E A D   B O A R D   F R O M    F I L E ======
# ======================================================
    def inserting_in_Array (self):
        with open("board.txt", "rt") as board: # ---------> rt=read text
            self.board_Array = [list(line.strip()) for line in board.readlines()]
# ======================================================
# =============   D R A W     B O A R D  ===============
# ======================================================
    def draw_Board(self):
        print(" ===========================================================================================")
        for row in range(len(self.board_Array) - 1):
            for col in range(len(self.board_Array) - 1):
                print(" | ",self.board_Array[row][col], end=" ")
            print(" |")
        print(" ===========================================================================================")
# ======================================================
# =============   D R A W     P A T H  =================
# ======================================================
    def draw_Path(self,sourceX,sourceY):
        dummy_Array = self.board_Array
        cost=0
        print(" ============================      F I N A L    P A T H   ==================================")
        # -----> placing path and finding cost here
        row = 0
        col = 1
        count = 0

        while count <=len(self.sahiWalaPath):
            if row!=len(self.sahiWalaPath)  and col!=len(self.sahiWalaPath):
                xcordinate = self.sahiWalaPath[row]
                ycordinate = self.sahiWalaPath[col]
                dummy_Array[xcordinate][ycordinate] = "*" # ------> path placed
                # ---------> moving up
                if xcordinate == (sourceX - 1) and ycordinate == (sourceY):
                    cost +=2
                    sourceX = sourceX-1
                # ---------> moving right
                elif xcordinate == sourceX and ycordinate == (sourceY + 1):
                    cost+=2
                    sourceY = sourceY+1
                # ---------> Diagonal Movement
                elif xcordinate == (sourceX - 1) and ycordinate == (sourceY + 1):
                    cost += 3
                    sourceX = sourceX-1
                    sourceY = sourceY+1
                row = row + 2
                col = col + 2
            count=count + 1
            continue
        print(" ===========================================================================================")
        for row in range(len(dummy_Array) - 1):
            for col in range(len(dummy_Array) - 1):
                print(" | ", dummy_Array[row][col], end=" ")
            print(" |")
        print(" ===========================================================================================")
        print(" =========================== T O T A L    C O S T  => ",cost,  "==================================")

# =====================================================
# =====   S O U R C E     C O O R D I N A T E S     ====
# ======================================================
    def findSource(self):
        sourceX = 0
        sourceY = 0
        for row in range(len(self.board_Array) - 1):
            for col in range(len(self.board_Array) - 1):
                if (self.board_Array[row][col] == 'S'):
                    sourceX = row
                    sourceY = col
                    break
        return sourceX, sourceY
# ======================================================
# =====       G O A L     C O O R D I N A T E S     ====
# ======================================================
    def findGoal(self):
        goalX = 0
        goalY = 0
        for row in range(len(self.board_Array) - 1):
            for col in range(len(self.board_Array) - 1):
                if ( self.board_Array[row][col] == 'G'):
                    goalX = row
                    goalY = col
                    break
        return goalX, goalY
# ======================================================
# =========  E X P L O R E     P A T H     =============
# ======================================================
    def explorePath(self,x_axis,y_axis,mDistance):
        if(self.board_Array[x_axis][y_axis]!='1'):# ------> 1 == Blockage
            self.exploredlist.append(x_axis)
            self.exploredlist.append(y_axis)
            self.exploredlist.append(mDistance)
            self.checkArray = True
# ======================================================
# ====== M I N I M U M    H E U R I S T I C   ==========
# ======================================================
    def minHeuristic(self):
        index = 2 # ----> for last value of 1st 3
        min = self.exploredlist[index] # -------->storing heuristic
        x = self.exploredlist[index-2]   # -------->x-axis
        y = self.exploredlist[index-1]   # -------->y-axis

        dummy = index
        while index <= len(self.exploredlist):
            if self.exploredlist[index]<min:
                min = self.exploredlist[index]  # -------->storing heuristic
                x = self.exploredlist[index - 2]  # -------->x-axis
                y = self.exploredlist[index - 1]  # -------->y-axis
                dummy = index
            index = index+3

        return x, y, dummy
# ======================================================
# =============== A- S T A R   S E A R C H      ========
# ======================================================
    def astar(self, SX_axis, SY_axis, GX_asix, GY_axis):
        up_cost = 2
        right_cost = 2
        diagonally_cost = 3

        manhathanDistance = abs(SX_axis - GX_asix) + abs(SY_axis - GY_axis)
        # print("manhathan Distance = ",manhathanDistance," \n")
        self.explorePath(SX_axis, SY_axis, manhathanDistance)

        while len(self.exploredlist) != 0:
            row,col,temp =self.minHeuristic()

            checkX = row - 1
            checkY = col + 1

            self.sahiWalaPath.append(row)
            self.sahiWalaPath.append(col)

            self.exploredlist.pop(temp)
            self.exploredlist.pop(temp - 1)
            self.exploredlist.pop(temp - 2)

            if (row == goalX and col == goalY):
                break
            elif checkX != -1 and checkY != 15:

                diagonal = abs((row - 1) - goalX) + abs((col + 1) - goalY)
                total_cost = diagonal + diagonally_cost
                self.explorePath((row - 1), (col + 1), total_cost)

                up = abs((row - 1) - goalX) + abs(col - goalY)
                total_cost = up + up_cost
                self.explorePath((row - 1), col, total_cost)

                right = abs(row - goalX) + abs((col + 1) - goalY)
                total_cost = right + right_cost
                self.explorePath(row, col + 1, total_cost)

    def RBSF(grid, start_x, start_y, goal_x, goal_y, Queue_for_path, path, temp1,
                                    temp2):
        if start_x == goal_x and start_y == goal_y:
            return
        elif temp1 != -1 and temp2 != 15:
            up_heuristic = abs((start_x - 1) - goal_x) + abs(
                start_y - goal_y)  # CALCULATION OF HEURISTIC VALUE OF UPWARD KEY OF RUNNING KEY
            insert_in_queue(grid, Queue_for_path, (start_x - 1), start_y)
            right_heuristic = abs(start_x - goal_x) + abs(
                (start_y + 1) - goal_y)  # CALCULATION OF HEURISTIC VALUE OF RIGTH KEY OF RUNNING KEY
            insert_in_queue(grid, Queue_for_path, start_x, (start_y + 1))
            diagonal_heuristic = abs((start_x - 1) - goal_x) + abs(
                (start_y + 1) - goal_y)  # CALCULATION OF HEURISTIC VALUE OF DIAGONAL KEY OF RUNNING KEY
            insert_in_queue(grid, Queue_for_path, (start_x - 1), (start_y + 1))
        extract_min(Queue_for_path)
        temp1 = x - 1
        temp2 = y + 1
        path.append(x)
        path.append(y)
        start_x = x
        start_y = y
        Queue_for_path.pop(temp)
        Queue_for_path.pop(temp - 1)
        Queue_for_path.pop(temp - 2)
        recursive_best_first_search(self.grid, start_x, start_y, goal_x, goal_y, visiting_nodes, Queue_for_path, path, temp1,
                                    temp2)


obj = Robot()
obj.inserting_in_Array()
obj.draw_Board()
sourceX, sourceY = obj.findSource()
goalX, goalY = obj.findGoal()


obj.astar(sourceX,sourceY,goalX,goalY)
#print(obj.exploredlist, " \n")
#print(obj.checkArray, " \n")
#print(obj.sahiWalaPath)
obj.draw_Path(sourceX,sourceY)
obj.RBSF(sourceX,sourceY)
