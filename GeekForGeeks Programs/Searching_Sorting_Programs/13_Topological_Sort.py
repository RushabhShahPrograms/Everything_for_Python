'''
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.
For example, a topological sorting of the following graph is “5 4 2 3 1 0”. There can be more than one topological sorting for a graph. For example, another topological sorting of the following graph is “4 5 2 3 1 0”. The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no in-coming edges).
'''
from collections import defaultdict

class Graph:
    def __init__(self,vertices):
        self.graph=defaultdict(list)
        self.v=vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
    
    def topologicalsortutil(self,v,visited,stack):
        visited[v]=True

        for i in self.graph[v]:
            if visited[i]==False:
                self.topologicalsortutil(i,visited,stack)
        
        stack.insert(0,v)

    def topologicalsort(self):
        visited=[False]*self.v
        stack=[]

        for i in range(self.v):
            if visited[i]==False:
                self.topologicalsortutil(i,visited,stack)
        
        print(stack)

g=Graph(6)
g.addEdge(5,2);
g.addEdge(5,0);
g.addEdge(4,0);
g.addEdge(4,1);
g.addEdge(2,3);
g.addEdge(3,1);

print("Following is a Topological Sort of the given graph")
g.topologicalsort()
