class Solution:

    def reverseBits(self, n: int) -> int:

        res = 0
        i = 0
        
        while n:
            lastBit = n & 1
            res = res | (lastBit << (31-i))
            n = n >> 1
            i += 1

        return res
