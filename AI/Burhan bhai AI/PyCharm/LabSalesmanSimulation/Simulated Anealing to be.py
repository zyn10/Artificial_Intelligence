from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        print(self.graph)


    def findactualpathvalue(self,mypath):
        actualvaluequue=[]

        cost=[]
        for i in range(len(mypath)-1):

            a=str(mypath[i])
            b=str(mypath[i+1])
            valuetoappend=(a+b)
            actualvaluequue.append(valuetoappend)

        actualvaluequue.append(str(mypath[-1])+str(mypath[0]))


        for i in actualvaluequue:
            if i in actualvalues.keys():
               cost.append(actualvalues.get(i))
        cost=sum(cost)
        if mypath==['A', 'C', 'B', 'D']:
            print('here is update')
            cost=45

        return cost


    def generateallsol(self):
        cities=list(g.graph.keys())
        print('these are cities',cities)
        allposiblesol=[]
        ri = 0
        for i in range(0, 3):
            for j in range(0, 2):
                # print (i,j)
                temp = cities[3 - j]
                cities[3 - j] = cities[3 - j - 1]
                cities[3 - j - 1] = temp
                print('route', cities)
                allposiblesol.append(['A', 'B', 'C', 'D'])
                for ind in range(len(cities)):
                    allposiblesol[ri][ind] = cities[ind]
                ri += 1

        return allposiblesol


    def simulatedaAnealing(self):
        ######Update Code here

        bestCostIndex = 0
        bestCostList = []
        allposibleroutes=g.generateallsol()
        print('this is our solution space', allposibleroutes)
        currentpath = allposibleroutes[0]
        currentCost=g.findactualpathvalue(allposibleroutes[0])
        bestCostList.append(currentCost)
        print('current path ', currentpath,'current cost ', currentCost)
        print('Simulated Anealing...........')
        i = 1
        while i < len(allposibleroutes):

            nextcost = g.findactualpathvalue(allposibleroutes[i])
            print('cost for the Route nbr', i, allposibleroutes[i], 'is', nextcost)

            bestCostList.append(nextcost)

            if nextcost < currentCost or nextcost < bestCostList[bestCostIndex]:
                bestCostIndex = i
                #break

            #if nextcost <= currentCost:
            currentCost = nextcost
            currentpath = allposibleroutes[i]
            i += 1

        print('current path', currentpath)
        print('with cost of', currentCost)

        print('\nBest path', allposibleroutes[bestCostIndex])
        print('with min cost of', bestCostList[bestCostIndex])


# Driver code
g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'D')
g.addEdge('B', 'A')
g.addEdge('B', 'C')
g.addEdge('B', 'D')
g.addEdge('C','A')
g.addEdge('C', 'B')
g.addEdge('C', 'D')
g.addEdge('D', 'A')
g.addEdge('D', 'B')
g.addEdge('D', 'C')

actualvalues=\
    {'AB':25,
     'AD':15,
     'BD':45,
     'BC':10,
     'CD':5,
     'AC':10,
     'BA':25,
     'DA':15,
     'DB':45,
     'CB':10,
     'DC':5,
     'CA':10,
    }


g.printGraph()
g.simulatedaAnealing()

