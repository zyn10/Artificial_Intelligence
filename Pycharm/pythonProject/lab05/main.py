def graph(dict, list):
    for (src, dest, wei) in list:
        dict[src] = []
        dict[dest] = []
    for (src, dest, wei) in list:
        dict[src].append((dest, wei))
        dict[dest].append((src, wei))

def BFS(s, e, hval, Dict, path):
    Queue = []
    Visited = []
    Queue.append((s, hval[s]))
    Visited.append(s)
    while Queue:
        Queue.sort(key=lambda  x:x[1])
        (N, M) = Queue.pop(0)
        path.append(N)
        if N == e:
            return
        for (d, y) in Dict[N]:
            if d not in Visited:
                Queue.append((d, hval[d]))
                Visited.append(d)



Path = []
Graph = {

}

HoristicValue = {
    "A" : 40,
    "B" : 32,
    "C" : 25,
    "D" : 35,
    "E" : 19,
    "F" : 17,
    "H" : 10,
    "G" : 0

}

Edges = [("A", "B", 11), ("A", "D", 7), ("A", "C", 14), ("B", "E", 15), ("C", "E", 8), ("C", "F", 10), ("D", "F", 25), ("E", "H", 9), ("F", "G", 20), ("H", "G", 10)]
graph(Graph, Edges)
BFS("A", "G", HoristicValue, Graph, Path)
j = 1
i = 0
res = [(A, B) for A, B in zip(Path, Path[1:] + [Path[0]])]
cost = 0
for x in range(len(Path) - 1):
    print(Path[x],),
print(Path[-1],)
for (a,b) in res:
    for (x, y) in Graph[a]:
        if b == x:
            cost = cost + y
print("Total Cost  = ", cost)
