#
from itertools import permutations
from collections import defaultdict
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)
        self.hillArray = []
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print(self.graph)

    def findactualpathvalue(self,mypath ,costs):
        pathstr = ""
        cost = 0
        for x in mypath:
            pathstr += x
        j = 2
        for i in range(0 , len(mypath)-1):
            slice1 = slice(i, j, 1)
            temp = pathstr[slice1]
            weight = costs[temp]
            cost += weight
            j = j+1

        print("Path => ",mypath,"\nPath Cost:",cost)
        self.hillArray.append(cost)


    def generateallsol(self):
        path = list(self.graph.keys())[:]
        path.extend(['A'])
        pairs = [i for i in set(permutations(path)) if i[0] == 'A' and i[-1] == 'A']
        print("Possible Pairs:")
        print(pairs)
        return pairs

    def hillclimbing(self):
        print(self.hillArray)
        lengthh = len(self.hillArray)
        current = self.hillArray[0]
        nextpoint = self.hillArray[1]

        for i in range(lengthh):
                if ( self.hillArray[i] > self.hillArray[i+1] ):
                    current = nextpoint
                elif(current < nextpoint ):
                     break

        print(current)

    def printwithCost(self,paths,actualvalues):
        for i in range(0, len(paths)):
            self.findactualpathvalue(paths[i], actualvalues)


# Driver code
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'A')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('C', 'A')
g.addEdge('C', 'B')
g.addEdge('C', 'D')
g.addEdge('D', 'A')
g.addEdge('D', 'B')
g.addEdge('D', 'C')

actualvalues = \
    {'AB': 25,
     'AD': 15,
     'BD': 45,
     'BC': 10,
     'CD': 5,
     'AC': 10,
     'BA': 25,
     'DA': 15,
     'DB': 45,
     'CB': 10,
     'DC': 5,
     'CA': 10,
     }

g.printGraph()
paths = g.generateallsol()
g.printwithCost(paths,actualvalues)
g.hillclimbing()