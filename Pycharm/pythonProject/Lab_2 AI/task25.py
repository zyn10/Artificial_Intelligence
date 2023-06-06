def append_edge(vertex1, vertex2,weight):
    global graph
    global vertices_no
    global vertices

    if vertex1 not in vertices:
        print("==> ", vertex1, " Vertex not exist <==")
    elif vertex2 not in vertices:
        print("==> ", vertex2, " Vertex not exist <==")
    else:
        index1 = vertices.index(vertex1)
        index2 = vertices.index(vertex2)
        graph[index1][index2] = weight


def append_Vertex(vertex):
    global graph
    global vertices_no
    global vertices
    if vertex in vertices:
        print("==>", vertex, " Vertex already exists <==")
    else:
        vertices_no = vertices_no + 1
        vertices.append(vertex)
        if vertices_no > 1:
            for vertex in graph:
             vertex.append(0)
        temp = []
        for i in range(vertices_no):
            temp.append(0)
            graph.append(temp)

def print_graph():
    global graph
    global vertices_no
    for i in range(vertices_no):
        for j in range(vertices_no):
            if graph[i][j] != 0:
                print(vertices[i], " -> ", vertices[j]," weight :- ", graph[i][j])
def appendVer():
    append_Vertex(5)
    append_Vertex(6)
    append_Vertex(3)
    append_Vertex(4)
    append_Vertex(1)
    append_Vertex(2)
def appendEdg():
    append_edge(5, 6, 9)
    append_edge(5, 4, 6)
    append_edge(6, 3, 2)
    append_edge(6, 5, 9)
    append_edge(6, 1, 14)
    append_edge(3, 6, 2)
    append_edge(3, 1, 9)
    append_edge(3, 4, 11)
    append_edge(3, 2, 10)
    append_edge(4, 3, 11)
    append_edge(4, 2, 15)
    append_edge(2, 3, 10)
    append_edge(2, 4, 15)
    append_edge(2, 1, 7)
    append_edge(1, 6, 14)
    append_edge(1, 3, 9)
    append_edge(1, 2, 7)
vertices = []
vertices_no = 0
graph = []
appendVer()
appendEdg()
print("\t*** Ajency Matrix Using Dictionay ***")
print("\t***Print Ajency List***")
print_graph()
print("\t Print Ajency Matrix")
print(" Matrix :- ", graph)
