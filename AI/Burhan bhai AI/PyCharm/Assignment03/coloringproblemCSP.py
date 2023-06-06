from collections import defaultdict

class colorProblem:

    def __init__(self):
        self.stateSpace = defaultdict(list)
        self.colorDomain = []
        self.assignedColor = defaultdict(list)
        self.setValues()
    def addEdge(self, u, v):
        self.stateSpace[u].append(v)
    def printStateSpace(self):
        for x in self.stateSpace:
            print(x,end=" => ")
            print(self.stateSpace[x])
    def setValues(self):

        self.addEdge("DJ", "SO")
        self.addEdge("DJ", "ET")
        self.addEdge("ET", "DJ")
        self.addEdge("ET", "SO")
        self.addEdge("ET", "KE")
        self.addEdge("SO", "DJ")
        self.addEdge("SO", "ET")
        self.addEdge("SO", "KE")
        self.addEdge("KE", "ET")
        self.addEdge("KE", "SO")
        self.addEdge("KE", "UG")
        self.addEdge("KE", "TA")
        self.addEdge("UG", "KE")
        self.addEdge("UG", "TA")
        self.addEdge("UG", "RW")
        self.addEdge("TA", "KE")
        self.addEdge("TA", "UG")
        self.addEdge("TA", "RW")
        self.addEdge("TA", "BU")
        self.addEdge("RW", "UG")
        self.addEdge("RW", "TA")
        self.addEdge("RW", "BU")
        self.addEdge("BU", "RW")
        self.addEdge("BU", "TA")

        self.colorDomain.append("red")
        self.colorDomain.append("green")
        self.colorDomain.append("blue")

        print("\nStates (variables):")
        self.printStateSpace()

        print("\nColor Domain", end=" => ")
        print(self.colorDomain)



    def checkCondition(self, v, color):
        if self.assignedColor[v] == color:
            return False
        return True

    def findSolution(self, startingNode):

        observable = []
        assigned = []
        visited = []

        observable.append(startingNode)

        constrain = False
        while observable:

            node = observable.pop(0)
            visited.append(node)
            neighboursNodes = self.stateSpace[node]

            constrain = False
            for color in self.colorDomain:

                for neighbour in neighboursNodes:
                    constrain = self.checkCondition(neighbour, color)
                    if not constrain:
                        break

                if constrain:
                    self.assignedColor[node] = color
                    break

            for neighbour in neighboursNodes:
                if neighbour not in visited and neighbour not in observable:
                    observable.append(neighbour)


        if not constrain:
            print(":: Solition not possible ::")
        else:
            print("\n:: Solition Found ::")
            for x in self.assignedColor:
                print(x, end=" => ")
                print(self.assignedColor[x])
            print("----------------------------------------------------------------------")

