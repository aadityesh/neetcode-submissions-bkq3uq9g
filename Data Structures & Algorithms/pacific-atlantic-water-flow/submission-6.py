class Solution:

    """
    Approach 1 - (DFS, class variables)

        R, C = len(heights), len(heights[0])

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def DFS(i, j):

            if i == 0 or j == 0:
                self.pacific = True
            
            if i == (R - 1) or j == (C - 1):
                self.atl = True

            self.visited.add((i, j))

            for x, y in DIRECTIONS:

                nr, nc = i + x, j + y
                
                if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in self.visited or heights[i][j] < heights[nr][nc]:
                    continue

                DFS(nr, nc)

        results = []
        for i in range(R):
            for j in range(C):
                
                self.visited = set()
                self.pacific = False
                self.atl = False

                DFS(i, j)

                if self.pacific and self.atl:
                    results.append((i, j))

        return results

    
    Approach 2 - (BFS, class variables)
    
    """

    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        R, C = len(heights), len(heights[0])

        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def BFS(i, j):

            q = deque()
            q.append((i, j))
            self.visited.add((i, j))

            pacific, atlantic = False, False

            while q:

                a, b = q.popleft()

                if a == 0 or b == 0:
                    pacific = True
            
                if a == (R - 1) or b == (C - 1):
                    atlantic = True

                if pacific and atlantic:
                    break

                for x, y in DIRECTIONS:

                    nr, nc = a + x, b + y
                    
                    if not (0 <= nr < R) or not (0 <= nc < C) or (nr, nc) in self.visited or heights[a][b] < heights[nr][nc]:
                        continue

                    q.append((nr, nc))
                    self.visited.add((nr, nc))
            
            return pacific and atlantic

        results = []
        for i in range(R):
            for j in range(C):
                
                self.visited = set()
                if BFS(i, j):
                    results.append((i, j))

        return results