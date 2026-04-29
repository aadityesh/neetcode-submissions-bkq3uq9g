from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R, C = len(grid), len(grid[0])
        visited = set()
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def BFS(i, j):

            q = deque([(i, j)])
            visited.add((i, j))

            while q:

                a, b = q.popleft()

                for x, y in DIRECTIONS:

                    nr, nc = a + x, b + y

                    if not (0 <= nr < R) or (not (0 <= nc < C)) or ((nr, nc) in visited) or (grid[nr][nc] == "0"):
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))

        cnt = 0
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == "1":
                    cnt += 1
                    BFS(r, c)

        return cnt
