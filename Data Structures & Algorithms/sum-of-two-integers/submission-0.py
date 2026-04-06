class Solution:
    
    def getSum(self, a: int, b: int) -> int:

        # 111
        # 110

        while b:
            tmp = a
            a = a ^ b
            b = (tmp & b) << 1
        
        return a
        