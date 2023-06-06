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

    def iterative_deepening_search(self, s, city_name=None):
        if city_name in self.graph.keys():
            stack = list()
            visited = list()
            stack.append(s)
            visited.append(s)
            while stack:
                s = stack.pop()
                for citty in self.graph[s]:
                    if citty not in visited:
                        stack.append(citty)
                        visited.append(citty)
                        print(citty)

                        if city_name == citty:
                            return visited
                        if len(visited) == len(self.graph):
                            return visited
        else:
            print("City not found")
            return None
    def printDFS_Limited(self):
        nxGraph = nx.Graph()
        for key in g.graph.keys():
            for value in g.graph[key]:
                nxGraph.add_edge(key, value)
        nx.draw(nxGraph, with_labels=True, node_color='orange', node_size=1200, font_size=10)  # drawing the graph
        plt.show()
        if len(path) > 0:
            visitedGraph = nx.Graph()
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
#path = g.depth_limited_search(src,dest,limit)
#g.printDFS_Limited(dest)

path = g.iterative_deepening_search('Dunwich')