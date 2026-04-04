class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        """
        
        The key insight is that the first two legs are 
        always safe (guarded by the while), 
        but the last two legs need their own checks 
        because top and right were already mutated mid-loop.
        
        """


        res = []
        R, C = len(matrix), len(matrix[0])

        left, right = 0, C - 1 # tracks col
        top, bottom = 0, R - 1 # tracks row

        while left <= right and top <= bottom:

            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            
            right -= 1

            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    res.append(matrix[bottom][i])

                bottom -= 1


            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])

                left += 1 

        return res           

