from collections import defaultdict

class Graph:
# Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
# function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)
# Function to print a BFS of graph
    def BFS(self,start,end):
        Queu = []
        visited = []

        Queu.append(start)
        visited.append(start)

        while Queu:
            temp = Queu.pop(0)
            print("Popped Element : ", temp)
            if(temp==end):
                break

            else:

                for i in self.graph[start]:

                    if i not in visited:
                        visited.append(i)
                        Queu.append(i)
# # Function to print a BFS of graph
#     def BFS(self, s):
#         Queu = []
#         visited = []
#
#         Queu.append(s)
#         visited.append(s)
#
#         while Queu:
#             temp = Queu.pop(0)
#             print("Popped Element : " , temp)
#             for i in self.graph:
#                 if i not in visited:
#                     visited.append(i)
#                     Queu.append(i)
#


# Driver code

# Create a graph given in
# the above diagram
g = Graph()
g.addEdge(1, 2)
g.addEdge(1, 3)
g.addEdge(2, 4)
g.addEdge(2, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)

g.addEdge(2, 1)
g.addEdge(3, 1)
g.addEdge(4, 2)
g.addEdge(5, 2)
g.addEdge(6, 3)
g.addEdge(7, 3)
start=int(input("Input the starting Point : "))
end=int(input("Input the ending point     : "))

print("Following is Breadth First Traversal"
      " (starting from vertex )",start)
g.BFS(start,end)
