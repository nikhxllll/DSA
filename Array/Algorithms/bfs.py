class BFS:
    def __init__(self):
        self.graph = {}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)
    def bfs(self,strt):
        visited = set()
        queue =[strt]
        while queue:
            node = queue.pop(0)
            if node not in visited:
                print(node,end = " ")
                visited.add(node)
                for nei in self.graph[node]:
                    if nei not in visited:
                            queue.append(nei)                      
# Driver Code
d = BFS()
d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(2,4)
d.add_edge(2,5)
print(d.bfs(1))
