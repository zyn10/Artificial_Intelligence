def append_Vertex(vertex):
    global graph
    global vertices_no
    if vertex in graph:
        print("***", vertex, " Vertex already exists ***")
    else:
        vertices_no = vertices_no + 1
        graph[vertex] = []
def append_edge(vertex1, vertex2):
    global graph
    if vertex1 not in graph:
        print("*** ", vertex1, " Vertex not exist ***")
    elif vertex2 not in graph:
        print("*** ", vertex2, " Vertex not exist ***")
    else:
        temp = [vertex2]
        graph[vertex1].append(temp)

def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print (vertex, " -> ", edges[0])
graph = {}
vertices_no = 0
append_Vertex('A')
append_Vertex('B')
append_Vertex('C')
append_Vertex('D')
append_Vertex('E')
append_Vertex('F')
append_Vertex('G')
append_Vertex('H')
append_edge('A', 'B')
append_edge('A', 'C')
append_edge('A', 'D')
append_edge('B', 'E')
append_edge('B', 'F')
append_edge('E', 'G')
append_edge('F', 'H')
print("*** Ajency List Using Dictionay ***")
print("*** Print Ajency List ***")
print_graph()