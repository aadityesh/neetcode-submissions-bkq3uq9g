class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        """
        
        1. We consider 1 -> node
        2. Run a traversal on this
            - While traversing, I am going to count number of nodes
            present in each connected component
            - I will take maximum of all the counts and return
 
        Take care:
            - While moving, I can only move to cell marked "1"
            - I have to look in all four direction
            - Also, take care of the index I am standing on to make
            sure I dont step out of bounds.
            - Dont revisit already visited cell
        """

        R, C = len(grid), len(grid[0])
        print(R, C)
        visited = set()

        maxArea = 0
        self.curArea = 0

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def DFS(i, j):
            
            visited.add((i, j))
            self.curArea += 1

            for x, y in DIRECTIONS:

                nr, nc = i + x, j + y

                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited or grid[nr][nc] == 0:
                    continue # skip this neighbor

                DFS(nr, nc)


        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == 1:
                    DFS(i, j) 
                    maxArea = max(maxArea, self.curArea)
                    self.curArea = 0

        return maxArea
        