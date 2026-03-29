class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        visited = set()

        def dfs(i, j):

            if not (0 <= i < rows) or not (0 <= j < cols) or grid[i][j] == '0' or (i, j) in visited:
                return 

            visited.add((i, j))
            
            dfs(i + 1, j) 
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)



        cnt = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs(i, j)
                    cnt += 1
        return cnt
