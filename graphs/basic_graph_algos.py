
import collections

class Graph:
    def __init__(self):
        self.graph = collections.defaultdict(list)

    def add_edge(self,u,v):
        self.graph[u].append(v)

    def DFSUtil(self,v,visited):
        visited.add(v)
        print(v,end=' ')
        for neightbor in self.graph[v]:
            if neightbor not in visited:
                self.DFSUtil(neightbor,visited)

    def DFS(self,v):

        visited = set()
        self.DFSUtil(v,visited)

    def BFS(self,v):
        visisted = [False] *(max(self.graph) + 1)

        queue =[]
        queue.append(v)
        visisted[v] = True

        while queue:
            v = queue.pop(0)
            print(v, end = ' ')

            for i in self.graph[v]:
                if visisted[i] == False:
                    queue.append(i)
                    visisted[i] = True


if __name__ =="__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)
    print()
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    g.BFS(2)      
