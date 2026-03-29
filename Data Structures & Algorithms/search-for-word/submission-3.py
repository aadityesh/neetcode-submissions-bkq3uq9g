class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        
        # def dfs(curr, i, j):

        #     if curr == word:
        #         return True
            
        #     if len(curr) > len(word) or not (0 <= i < rows) or not (0 <= j < cols):

        #         return False

        #     if (i, j) in self.visited: return False
            
        #     curr = curr + board[i][j]
        #     self.visited.add((i,j))
            
        #     res =  (
        #         # 0, 2
        #         # 1, 2
        #         dfs(curr, i + 1, j) or
        #         dfs(curr, i, j + 1) or
        #         dfs(curr, i - 1, j) or 
        #         dfs(curr, i, j - 1)
        #     )

        #     self.visited.remove((i,j))

        #     return res
        

        # for i in range(rows):
        #     for j in range(cols):
        #         self.visited = set()
        #         if board[i][j] == word[0] and dfs("", i, j): return True
        
        # return False

                
        def dfs(curr, i, j):

            if curr == word:
                return True
            
            if len(curr) >= len(word) or not (0 <= i < rows) or not (0 <= j < cols) or board[i][j] == "#":
                return False
            
            curr = curr + board[i][j]
            board[i][j] = '#'
            
            res =  (
                # 0, 2
                # 1, 2
                dfs(curr, i + 1, j) or
                dfs(curr, i, j + 1) or
                dfs(curr, i - 1, j) or 
                dfs(curr, i, j - 1)
            )

            board[i][j] = curr[-1]

            return res
        

        for i in range(rows):
            for j in range(cols):
                self.visited = set()
                if board[i][j] == word[0] and dfs("", i, j): return True
        
        return False
        
        