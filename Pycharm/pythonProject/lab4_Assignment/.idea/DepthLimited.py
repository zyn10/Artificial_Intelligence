from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx


class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

        # Function to print a DFS of graph
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
                    if cityy not in visited:  # if city is not in visited
                        stack.append(cityy)   # add city to stack
                        visited.append(cityy) # add city to visited

    def printDFS(self):
        # return dfs path
        nxGraph = nx.Graph()

        for key in g.graph.keys():
            for value in g.graph[key]:
                nxGraph.add_edge(key, value)

        nx.draw(nxGraph, with_labels=True, node_color='orange', node_size=1200, font_size=8)
        plt.show()
        if visited:
            visitedGraph = nx.Graph()
            for i in range(len(visited)):
                if i < len(visited) - 1:
                    visitedGraph.add_edge(visited[i], visited[i + 1])
            nx.draw(visitedGraph, with_labels=True, node_color='lightblue', node_size=1200, font_size=8)
            plt.show()
        else:
            print("No path found")

    def depth_limited_search(self, s, city_name=None, depth_limit=10):
        if city_name in self.graph.keys():
            stack = list()
            visited = list()
            stack.append(s)
            visited.append(s)
            while stack:  # while stack is not empty
                s = stack.pop()  # pop s from stack

                for cityy in self.graph[s]:
                    if cityy not in visited:  # if city is not in visited
                        stack.append(cityy)  # add city to stack
                        visited.append(cityy)  # add city to visited
                        print(cityy)

                        if city_name == cityy:
                            return visited
                        if len(visited) == depth_limit:
                            return visited
            return visited
    def printDFS_Limited(self,destination):
        path = g.depth_limited_search('Dunwich', destination, 6)
        nxGraph = nx.Graph()

        for key in g.graph.keys():
            for value in g.graph[key]:
                nxGraph.add_edge(key, value)
        nx.draw(nxGraph, with_labels=True, node_color='orange', node_size=1200, font_size=10)  # drawing the graph
        plt.show()  # showing the plot
        if len(path) > 0:  # if the vertex is found
            visitedGraph = nx.Graph()  # create graph for path
            for i in range(len(path)):
                if i < len(path) - 1:
                    visitedGraph.add_edge(path[i], path[i + 1])
            nx.draw(visitedGraph, with_labels=True, node_color='orange', node_size=1200, font_size=10)
            plt.show()
        else:
            print("No path found")


g = Graph()

g.addEdge('Dunwich', 'Blaxhall')
g.addEdge('Dunwich', 'Harwich')

g.addEdge('Blaxhall', 'Dunwich')
g.addEdge('Blaxhall', 'Harwich')
g.addEdge('Blaxhall', 'Feering')

g.addEdge('Harwich', 'Blaxhall')
g.addEdge('Harwich', 'Dunwich')
g.addEdge('Harwich', 'Tiptree')
g.addEdge('Harwich', 'Clacton')

g.addEdge('Feering', 'Blaxhall')
g.addEdge('Feering', 'Tiptree')
g.addEdge('Feering', 'Maldon')

g.addEdge('Tiptree', 'Maldon')
g.addEdge('Tiptree', 'Feering')
g.addEdge('Tiptree', 'Clacton')
g.addEdge('Tiptree', 'Harwich')

g.addEdge('Clacton', 'Harwich')
g.addEdge('Clacton', 'Tiptree')
g.addEdge('Clacton', 'Maldon')

g.addEdge('Maldon', 'Feering')
g.addEdge('Maldon', 'Tiptree')
g.addEdge('Maldon', 'Clacton')


src = "Dunwich"
dest = input("Destination : ")
print("Depth Limited Path ")
#visited = g.DFS(src, dest)
#g.printDFS()
limit=6
path = g.depth_limited_search(src,dest,limit)
g.printDFS_Limited(dest)

