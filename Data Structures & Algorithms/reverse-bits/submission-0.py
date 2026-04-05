class Solution:
    def reverseBits(self, n: int) -> int:
        
        rev = 0

        while n:

            lastBit = n & 1 # extract last bit
            n = n >> 1 # remove last bit

            if lastBit == 1: # set bit
                rev = rev | 1

            rev = rev << 1
        
        return rev