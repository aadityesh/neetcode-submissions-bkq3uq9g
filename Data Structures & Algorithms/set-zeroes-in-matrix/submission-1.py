class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        # R, C = len(matrix), len(matrix[0])

        # identify which (r,c) contain zero and set them to zero
        # rows = [False] * R
        # cols = [False] * C

        # for i in range(R):
        #     for j in range(C):
        #         if matrix[i][j] == 0:
        #             rows[i], cols[j] = True, True
        

        # for i in range(R):
        #     for j in range(C):
        #         if rows[i] or cols[j]:
        #             matrix[i][j] = 0
        
        ##############################################

        R, C = len(matrix), len(matrix[0])
        rowZero = False

        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:

                    # mark in zeroth col
                    matrix[0][j] = 0

                    if i == 0: 
                        rowZero = True
                    else:
                        matrix[i][0] = 0
        
        for i in range(1, R):
            for j in range(1, C):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0: # Oth Column should be marked zero
            for i in range(R):
                matrix[i][0] = 0
        
        if rowZero:
            for j in range(C):
                matrix[0][j] = 0

        

                
