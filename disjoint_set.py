class DisjointSet:
    def __init__(self, n) -> None:
        self.parent = [i for i in range(0, (n + 1))]
        print(self.parent)
        self.rank = [0] * (n + 1)
    
    def find(self, u):
        parent = self.parent[u]
        while parent != u:
            parent = self.parent[u] 
            u = parent
        return parent
    
    def union(self, u, v):
        # check if both parents are same or not
        parent_u, parent_v = self.find(u), self.find(v)
        if parent_u == parent_v:
            return 
        else:
            rank_u, rank_v = self.rank[parent_u], self.rank[parent_v]
            if rank_u > rank_v:
                self.parent[parent_v] = parent_u
            elif rank_u < rank_v:
                self.parent[parent_u] = parent_v
            else:
                self.parent[parent_v] = parent_u
                self.rank[parent_u] += 1
    def same_set(self, u, v):
        return self.find(u) == self.find(v)     
    
# ds = DisjointSet(6)

# ds.union(0, 1)
# ds.union(1, 2)
# ds.union(3, 4)

# print(ds.same_set(0, 1))
# print(ds.same_set(1, 2))
# print(ds.same_set(2, 3))
# print(ds.same_set(3, 4))
# print(ds.same_set(4, 5))