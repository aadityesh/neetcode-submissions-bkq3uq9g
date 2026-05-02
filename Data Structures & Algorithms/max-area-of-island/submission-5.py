from collections import deque

class Solution:

    """
    
    Approach - 1 (DFS)

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
    
    Approach - 2 (BFS):

        R, C = len(grid), len(grid[0])
        print(R, C)
        visited = set()

        maxArea = 0
        self.curArea = 0

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        def BFS(i, j):

            q = deque([(i, j)])
            visited.add((i, j))

            while q:

                a, b = q.popleft()
                self.curArea += 1

                for x, y in DIRECTIONS:

                    nr, nc = a + x, b + y

                    if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))


        for i in range(R):
            for j in range(C):
                if (i, j) not in visited and grid[i][j] == 1:
                    BFS(i, j) 
                    maxArea = max(maxArea, self.curArea)
                    self.curArea = 0

        return maxArea
    """

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

        maxArea = 0

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def BFS(i, j):

            q = deque([(i, j)])
            grid[i][j] = 0 # mark visited

            curArea = 0

            while q:

                a, b = q.popleft()
                curArea += 1

                for x, y in DIRECTIONS:

                    nr, nc = a + x, b + y

                    if not (0 <= nr < R) or not (0 <= nc < C) or grid[nr][nc] == 0:
                        continue
                    
                    q.append((nr, nc))
                    grid[nr][nc] = 0


            return curArea


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1: 
                    maxArea = max(maxArea, BFS(i, j))
        return maxArea
        