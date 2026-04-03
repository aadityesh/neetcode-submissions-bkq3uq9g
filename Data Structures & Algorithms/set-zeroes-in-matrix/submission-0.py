class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        R, C = len(matrix), len(matrix[0])

        # identify which (r,c) contain zero and set them to zero
        rows = [False] * R
        cols = [False] * C

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows[i], cols[j] = True, True
        

        for i in range(R):
            for j in range(C):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0
        
        