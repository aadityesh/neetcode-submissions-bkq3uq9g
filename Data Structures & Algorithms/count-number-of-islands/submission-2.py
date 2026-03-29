class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        R, C = len(grid), len(grid[0])
        visited = set()
        islands = 0
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):

            que = collections.deque()
            que.append((r,c))
            

            while que:
                
                fr, fc = que.popleft()

                for x, y in DIRECTIONS:

                    nr = fr + x
                    nc = fc + y

                    if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue

                    que.append((nr, nc))
                    visited.add((nr, nc))

        for r in range(R):
            for c in range(C):

                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
