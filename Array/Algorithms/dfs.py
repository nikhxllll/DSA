class Dfs:
    def __init__(self):
        self.items = {}
    def add_edge(self,u,v):
        if u not in self.items:
            self.items[u] = []
        if v not in self.items:
            self.items[v] = []
        self.items[u].append[v]
        self.items[v].append[u]
    def dfs(self,start):
        visited = set()
        stack = [start]
        while stack:
            node = stack.pop()
            print(node,end=" ")
            visited.add(node)
            for nei in self.items[node]:
                visited.add(nei)
                stack.append(nei)
d = Dfs()

