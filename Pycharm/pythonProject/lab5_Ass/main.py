# A* ALGORITHM

def Astar(startState, stopState):
    startSet = set(startState)
    closeSet = set()
    # storing distance from starting node
    dis = {}
    # parentNode contains an adjacency map of all nodes
    parentNode = {}
    pathCost=0
    # ditance of starting node from itself is zero
    dis[startState] = 0
    # startState is root node i.e it has no parent nodes
    # so startState is set to its own parent node
    parentNode[startState] = startState

    while len(startSet) > 0:
        n = None

        # node with lowest f() is found
        for v in startSet:
            if n == None or dis[v] + heuristic(v) < dis[n] + heuristic(n):
                n = v

        if n == stopState or graph[n] == None:
            pass
        else:
            for (m, weight) in neighbors(n):
                # nodes 'm' not in first and last set are added to first
                # n is set its parent
                if m not in startSet and m not in closeSet:
                    startSet.add(m)
                    parentNode[m] = n
                    dis[m] = dis[n] + weight
                    pathCost+=weight


                # for each node m,compare its distance from start i.e dis(m) to the
                # from start through n node
                else:
                    if dis[m] > dis[n] + weight:
                        # update dis(m)
                        dis[m] = dis[n] + weight
                        # change parent of m to n
                        parentNode[m] = n

                        # if m in closed set,remove and add to open
                        if m in closeSet:
                            closeSet.remove(m)
                            startSet.add(m)

        if n == None:
            print('Path does not exist!')
            return None

        # if the current node is the stopState
        # then we begin reconstructin the path from it to the startState
        if n == stopState:
            path = []

            while parentNode[n] != n:
                path.append(n)
                n = parentNode[n]

            path.append(startState)

            path.reverse()

            print('Path found: {}'.format(pathCost))
            return path

        # remove n from the open_list, and add it to closed_list
        # because all of his neighbors were inspected
        startSet.remove(n)
        closeSet.add(n)

    print('Path does not exist!')
    return None


# define fuction to return neighbor and its distance
# from the passed node
def neighbors(v):
    if v in graph:
        return graph[v]
    else:
        return None


# for simplicity we ll consider heuristic distances given
# and this function returns heuristic distance for all nodes
def heuristic(n):
    H_dist = {
        'A': 40,
        'B': 32,
        'C': 25,
        'D': 35,
        'E': 19,
        'F': 17,
        'H': 10,
        'G': 0
    }

    return H_dist[n]


# Describe your graph here
graph = {
    'A': [('B', 11), ('D', 7), ('C', 14)],
    'B': [('A', 11), ('E', 15)],
    'C': [('A', 14), ('E', 8), ('F', 10)],
    'D': [('A', 7), ('F', 25)],
    'E': [('B', 15), ('C', 8), ('H', 9)],
    'F': [('C', 10), ('D', 25), ('G', 20)],
    'G': [('F', 20), ('H', 10)],
    'H': [('E', 9), ('G', 10)],

}
Astar('A', 'G')