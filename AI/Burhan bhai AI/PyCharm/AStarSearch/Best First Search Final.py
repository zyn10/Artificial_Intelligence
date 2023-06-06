
from collections import defaultdict

class Graph:


    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):

        self.graph[u].append(v)

    def printGraph(self):
        print("Given Graph",self.graph)

    # Function to print a BFS of graph
    def BFS(self, s, e):
        print("This is our starting node", s)
        print("This is our ending node",e)
        visited=[]
        queue = []
        path=[]
        queue.append(s)
        visited.append(s)
        while queue:
            nodetoselect=g.findHeuristic(queue,huristic)
            s=nodetoselect
            path.append(s)
            print("Node to Select",s)
            indexofselectedvalue = queue.index(s)
            queue.pop(indexofselectedvalue)
            if s==e:
                break
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        print("this is our final path",path)
        g.findactualpathvalue(path)

    def findactualpathvalue(self,mypath):

        actualvaluequue=[]
        cost=[]
        for i in range(len(mypath)-1):
            a=str(mypath[i])
            b=str(mypath[i+1])
            valuetoappend=(a+b)
            print('from ', a,'to', b, end=' ')
            actualvaluequue.append(valuetoappend)
        print("this is the path to go",actualvaluequue)
        for i in actualvaluequue:
            if i in actualvalues.keys():
               cost.append(actualvalues.get(i))
        print('This is the actual cost', sum(cost))

    def findHeuristic(self,pqueu,dich):

        keyslist=[]
        valueslist=[]
        for i in pqueu:
            if i in dich.keys():
                keyslist.append(i)
                valueslist.append(dich.get(i))
        indexofvalue=valueslist.index(min(valueslist))
        keyofminvalue=keyslist[indexofvalue]
        print('Keys list:', keyslist)
        print("Value list", valueslist)
        return keyofminvalue

# Driver code

g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'E')
g.addEdge('C', 'F')
g.addEdge('D','F')
g.addEdge('E', 'H')
g.addEdge('F', 'G')
g.addEdge('H', 'G')
huristic=\
    {'A': 40,
     'B':32,
     'C':25,
     'D':35,
     'E':19,
     'F':17,
     'H':10,
     'G':0
}

actualvalues=\
    {'AB':11,
     'AC':14,
     'AD':7,
     'BE':15,
     'CE':8,
     'CF':10,
     'DF':25,
     'FG':20,
     'EH':9,
     'HG':10,
    }

g.printGraph()
print("heuristic Values",huristic)
print("Actual Cost of the graph", actualvalues)
g.BFS('A','G')


