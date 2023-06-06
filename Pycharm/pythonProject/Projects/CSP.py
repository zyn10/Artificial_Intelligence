#neighbour connection function
def neighbours(matrix, x, y):
    matrix[x][y] = 1
    matrix[y][x] = 1


def CSP( matrix, states, coloredArray, colored):
    for i in range(0, len(states)):
        temp = coloredArray[i]
        colored[i] = temp.pop()
        coloredArray[i] = colored[i]
        connections = []
        n = 0
        for j in range(0, len(states)):
            if matrix[i][j] == 1:
                if colored[j] == " ":
                    connections.append(j)
                    n = n + 1

        for j in range(n, len(states)):
            connections.append(-1)

        for j in range(0, len(connections)):
            if connections[j] != -1:
                p = coloredArray[connections[j]]
                for k in p:
                    if colored[i] == k:
                        p.remove(colored[i])
                coloredArray[connections[j]] = p

        q = 0
        possibleColors = ["red", "green", "blue"]
        for j in range(i+1, len(states)):
            if j != connections[q]:
                coloredArray[j] = possibleColors
            q = q + 1
    display(coloredArray, states)


def display(coloredArray, states):
    print("---------------\nPOSSIBLE RESULT\n---------------")
    for i in range(0, len(states)):
        color = " "
        if coloredArray[i] == "red":
            color = "RED"
        elif coloredArray[i] == "green":
            color = "GREEN"
        else:
            color = "BLUE"
        print("(", states[i], ":", color, ")")
    print("---------------")


states = ["DJ", "SO", "ET", "KE", "UG", "TA", "RW", "BU"]
availableColors=["red", "green", "blue"]
colored = [" ", " ", " ", " ", " ", " ", " ", " "]
coloredArray = []

#initialized coloredArray with all the available colors
for i in range(0, len(states)):
    coloredArray.append(availableColors)

#adjacency matrix creation
matrix=[[0 for i in range(len(states))] for j in range(len(colored))]
neighbours(matrix, 0, 1)
neighbours(matrix, 0, 2)
neighbours(matrix, 1, 0)
neighbours(matrix, 1, 2)
neighbours(matrix, 1, 3)
neighbours(matrix, 2, 0)
neighbours(matrix, 2, 1)
neighbours(matrix, 2, 3)
neighbours(matrix, 3, 1)
neighbours(matrix, 3, 2)
neighbours(matrix, 3, 4)
neighbours(matrix, 3, 5)
neighbours(matrix, 4, 3)
neighbours(matrix, 4, 5)
neighbours(matrix, 4, 6)
neighbours(matrix, 5, 3)
neighbours(matrix, 5, 4)
neighbours(matrix, 5, 6)
neighbours(matrix, 5, 7)
neighbours(matrix, 6, 4)
neighbours(matrix, 6, 5)
neighbours(matrix, 6, 7)
neighbours(matrix, 7, 5)
neighbours(matrix, 7, 6)
CSP(matrix, states, coloredArray, colored)