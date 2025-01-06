class BFS:
    def __init__(self):
        self.graph = {}
    def add_edge(self,u,v):
        if u not in self.graph:
            self.graph[u] = []
            self.graph[u].append(v)
        if v not in self.graph:
            self.graph[v] = []
            self.graph[v].append(u)
    

            
