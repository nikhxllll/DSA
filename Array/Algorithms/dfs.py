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
        