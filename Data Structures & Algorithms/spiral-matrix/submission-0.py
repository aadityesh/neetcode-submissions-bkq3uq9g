class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        R, C = len(matrix), len(matrix[0])

        left, right = 0, C - 1 # tracks col
        top, bottom = 0, R - 1 # tracks row

        while left < right and top < bottom:

            for i in range(left, right + 1):
                res.append(matrix[top][i])

            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            
            right -= 1

            if not (left < right and top < bottom):
                break

            for i in range(right, left-1, -1):
                res.append(matrix[bottom][i])

            bottom -= 1


            for i in range(left, right + 1):
                res.append(matrix[top][i])

            left += 1 

        return res           

