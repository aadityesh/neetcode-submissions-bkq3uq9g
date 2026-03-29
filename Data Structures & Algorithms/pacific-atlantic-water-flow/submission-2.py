class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        R, C = len(heights), len(heights[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j):

            self.result.append((i, j))
            self.visited.add((i, j))

            for x, y in directions:

                nr = i + x
                nc = j + y

                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in self.visited or heights[nr][nc] > heights[i][j]:
                    continue

                dfs(nr, nc)
        
        res = []
        for r in range(R):
            for c in range(C):

                self.result = []
                self.visited = set()
                
                dfs(r,c)

                pacific = False
                atlantic = False

                for x, y in self.result:

                    if x == 0 or y == 0: pacific = True
                    if x == (R - 1) or y == (C - 1): atlantic = True

                    if pacific and atlantic:
                        res.append([r,c])
                        break
        
        return res
                


        