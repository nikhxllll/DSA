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
    def bfs(self,strt):
        visited = set()
        queue =[strt]
        while queue:
            node = queue.pop(0)
            print(node,end = " ")
            visited.add(node)
            for nei in self.graph[node]:
                if nei not in visited:
                        queue.append(nei)

            
