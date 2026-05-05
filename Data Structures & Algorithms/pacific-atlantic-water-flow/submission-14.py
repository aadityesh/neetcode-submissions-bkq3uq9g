class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def DFS(i, j, visited):

            visited.add((i, j))

            for x, y in DIRECTIONS:

                nr, nc = i + x, j + y

                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited or heights[i][j] > heights[nr][nc]:
                    continue
                
                DFS(nr, nc, visited)
        
        #row0, rowN-1
        for j in range(C):
            DFS(0, j, pac)
            DFS(R-1, j, atl)
        
        #col0, col1
        for i in range(R):
            DFS(i, 0, pac)
            DFS(i, C-1, atl)
        
        res = []
        for i in range(R):
            for j in range(C):
                if (i,j) in pac and (i, j) in atl:
                    res.append([i, j])
        
        return res
