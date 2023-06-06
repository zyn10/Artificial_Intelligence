import sys

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
def MinimumIndex(myQueue):
    min = 100
    index =-1
    minInd=0
    for x in myQueue:
        index=index+1
        if (min > x[1]):
            min = x[1]
            minInd=index
    return minInd

class Graph:

    def _init_(self,vertices):
        self.vertices=vertices
        self.dict={}
        for vertice in self.vertices:
            self.dict[vertice]=[]

    def AddEdge(self,src,dest,weigth):
        self.dict[src].append([dest,weigth])

    def Display(self):
        for x in self.dict.keys():
            print(x,self.dict[x])


def DepthGoalBased(self, s, g, limit):
    if (limit >= 3):
        limit = pow(2, limit) - pow(2, limit - 1)
    Queu = []
    visited = []
    Queu.append([s,0])
    visited.append(s)
    totalCost=0
    count = 0
    while (Queu):
        x = Queu.pop(len(Queu) - 1)
        print(x[0]+,"->",end=" ")
        totalCost=totalCost+x[1]
        if (x[0] == g):
            print("Found")
            print("Total Cost: ", totalCost)
            return True
        condition = False
        if (limit > len(Queu)):
            for a in self.dict[x[0]]:
                if a[0] not in visited:
                    Queu.append(a)
                    condition = True
                    visited.append(a[0])
        if (condition):
            count = count + 1
            condition = False
        else:
            count = 0
        if (count == 2):
            limit = limit - 1
    print("Not Found")
    return False


def DepthLimitedTraversal(self, s, limit):
    if (limit >= 3):
        limit = pow(2, limit) - pow(2, limit - 1)
    Queu = []
    visited = []
    Queu.append([s,0])
    visited.append(s)
    totalCost=0
    count = 0
    while (Queu):
        x = Queu.pop(len(Queu) - 1)
        print(x[0]+"->",end=" ")
        totalCost=totalCost+x[1]
        condition = False
        if (limit > len(Queu)):
            for a in self.dict[x[0]]:
                if a[0] not in visited:
                    Queu.append(a)
                    condition = True
                    visited.append(a[0])
        if (condition):
            count = count + 1
            condition = False
        else:
            count = 0
        if (count == 2):
            limit = limit - 1
    print("Total Cost: ", totalCost)

    def DFS(self, temp, city_name=None):

        if city_name not in self.graph.keys():
            return False
        elif city_name in self.graph.keys():
            stack = list()
            visited = list()
            stack.append(temp)
            visited.append(temp)

            while stack: #Stack !empty
                s = stack.pop()
                print(s)

                if city_name == s:
                    return visited

                for cityy in self.graph[s]:
                    if cityy not in visited:  
                        stack.append(cityy)  
                        visited.append(cityy) 










    def iterative_deepening_search(self, s, data=None):
        if city_name in self.graph.keys():
            stack = list()
            visited = list()
            stack.append(s)
            visited.append(s)
            while stack:
                s = stack.pop()
                for citty in self.graph[s]:
                    if citty not in visitd:
                        stack.append(data)
                        visited.append(data)
                        print(citty)

                        if city_name == data:
                            return visited
                        if len(visited) == len(self.graph):
                            return visited
        else:
            print("City not found")
            return None

