class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])  
        return self.parent[u]
    
    def union(self, u, v):
        parent_u, parent_v = self.find(u), self.find(v)
        rank_u, rank_v = self.rank[u], self.rank[v]
        if rank_u >= rank_v:
            self.parent[parent_v] = parent_u
        elif rank_u < rank_v:
            self.parent[parent_u] = parent_v
        else:
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += 1