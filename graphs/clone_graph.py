# 18.5 CLONE A GRAPH

# Consider a vertex type for a directed graph in which there are two fields: an
# integer label and a list of references to other vertices. Design an algorithm
# that takes a reference to a vertex u, and creates a copy of the graph on the
# vertices reachable from u. Return the copy of u.
#
# Hint: Maintain a map from vertices in the original graph to their counterparts
# in the clone.

# 133. Clone Graph https://leetcode.com/problems/clone-graph/

import collections
from typing import List

class GraphVertex:
    def __init__(self,label:int)->None:
        self.label = label
        self.edges: List['GraphVertex'] = []

def clone_graph(firstVertex:GraphVertex) -> GraphVertex:
    if firstVertex is None:
        return None

    q = collections.deque([firstVertex])
    visited = {firstVertex:GraphVertex(firstVertex.label)}

    while q:
        v = q.popleft()
        for e in v.edges:
            # try to copy vertex
            if e not in visited:
                visited[e] = GraphVertex(e.label)
                q.append(e)
            # copy edge
            visited[v].edges.append(visited[e])
    return visited


if __name__ =="__main__":
    vert1 = GraphVertex(1)
    vert2 = GraphVertex(2)
    vert3 = GraphVertex(3)
    vert4 = GraphVertex(4)
    vert5 = GraphVertex(5)
    vert6 = GraphVertex(6)
    vert7 = GraphVertex(7)
    vert8 = GraphVertex(8)
    vert9 = GraphVertex(9)

    vert6.edges.append(vert7)
    vert6.edges.append(vert8)
    vert3.edges.append(vert6)
    vert3.edges.append(vert7)
    vert3.edges.append(vert4)
    vert3.edges.append(vert5)
    vert1.edges.append(vert2)
    vert1.edges.append(vert3)


    clonedGraph = clone_graph(vert1)
    print(clonedGraph)
    for i in clonedGraph:
        print("node:",i.label)
        for j in clonedGraph[i].edges:
            print(j.label)
