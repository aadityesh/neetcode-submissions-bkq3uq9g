class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        R, C = len(matrix), len(matrix[0])

        for i in range(R):
            
            for j in range(i+1):

                if i == j: continue
                # swap
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(R):
            
            r, c = 0, C - 1
            while r < c:
                matrix[i][r], matrix[i][c] = matrix[i][c], matrix[i][r]
                r += 1
                c -= 1