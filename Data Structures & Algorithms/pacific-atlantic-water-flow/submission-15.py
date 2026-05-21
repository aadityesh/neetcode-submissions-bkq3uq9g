class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        pac = atl = False
        R, C = len(heights), len(heights[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def DFS(i, j, visited):

            nonlocal atl, pac

            if i == 0 or j == 0:
                pac = True
            
            if i == R - 1 or j == C - 1:
                atl = True

            visited.add((i, j))

            for x, y in DIRECTIONS:

                nr, nc = i + x, j + y

                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited or heights[i][j] < heights[nr][nc]:
                    continue
                
                DFS(nr, nc, visited)

        res = []
        for i in range(R):
            for j in range(C):
                    pac = atl = False
                    DFS(i, j, set())
                    if pac and atl:
                        res.append([i, j])
        return res