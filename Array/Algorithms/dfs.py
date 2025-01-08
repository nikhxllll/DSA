class Dfs:
    def __init__(self):
        self.items = {}
    def add_edge(self,u,v):
        if u not in self.items:
            self.items[u] = []
        if v not in self.items:
            self.items[v] = []
        self.items[u].append(v)
        self.items[v].append(u)
    def dfs(self,start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                print(node,end=" ")
                visited.add(node)
                for nei in reversed(self.items[node]): # for nei in self.items[node]
                    if nei not in visited:
                        stack.append(nei)
                        
# Driver Code
d = Dfs()
d.add_edge(1,2)
d.add_edge(1,3)
d.add_edge(2,4)
d.add_edge(2,5)
print(d.dfs(1))

