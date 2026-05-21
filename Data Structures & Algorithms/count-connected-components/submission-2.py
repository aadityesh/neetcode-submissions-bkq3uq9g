class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent = [v for v in range(n)]
        size = [1 for _ in range(n)]

        def find(v):

            if v == parent[v]: return v
            return find(parent[v])

        def union(a, b):

            p1 = find(a)
            p2 = find(b)

            if p1 != p2:
                if p1 < p2:
                    p1, p2 = p2, p1
                    
            parent[p2] = p1
            size[p1] += size[p2]
        
        # build parent array
        for x, y in edges:
            union(x, y)
        
        # iterate over parent and count all v = parent[v]

        cnt = 0
        for ind, elem in enumerate(parent):
            if ind == elem:
                cnt += 1
        
        return cnt


