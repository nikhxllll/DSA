class Graph:
    def __init__(self,vno):
        self.vertex_count = vno
        self.adj_matrix = [[0]*vno for i in range(vno)]
    