graphs = {
  '1': ['2', '3'],
  '2': ['1', '4', '5'],
  '3': ['1', '6', '7'],
  '4': ['2'],
  '5': ['2'],
  '6': ['3'],
  '7': ['3']
}

DFSstarting = '1'

stack = []
visited = []

def travers(starting,stak,visit, graph):
    stak.append(starting)

    while stak:
        node = stak.pop()
        visit.append(node)
        for conectedNode in graph[node]:
            if conectedNode not in visited and conectedNode not in stak:
                stak.append(conectedNode)
        print (str(node) + " -> ")



travers(DFSstarting,stack,visited,graphs)
