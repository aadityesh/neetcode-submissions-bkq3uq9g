class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1 for _ in range(n)]
    
    def find(self, v):
        
        if v == self.parent[v]:
            return v
        
        self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, A, B):

        parentOfA = self.find(A)
        parentOfB = self.find(B)

        if parentOfA != parentOfB:
            if self.size[parentOfA] < self.size[parentOfB]:
                parentOfA, parentOfB = parentOfB, parentOfA
            
            self.parent[parentOfB] = parentOfA
            self.size[parentOfA] += self.size[parentOfB]
        
            return True
        
        else:
            return False



class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R, C = len(grid), len(grid[0])
        obj = DSU(R * C)
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def normalize_index(i, j):
            return (i * C) + j

        cnt = 0
        for i in range(R):
            for j in range(C):

                if grid[i][j] == "1":
                    
                    cnt += 1
                    # Explore the neighbors 
                    normCurr = normalize_index(i, j)

                    for x, y in DIRECTIONS:

                        nr, nc = i + x, j + y

                        if not (0 <= nr < R) or not (0 <= nc < C) or grid[nr][nc] == "0":
                            continue

                        # grid[nr][nc] = "#"
                        normNeighbor = normalize_index(nr, nc)
                        if obj.union(normCurr, normNeighbor):
                            cnt -= 1

        return cnt

                



      