class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        
        def fn(i):

            if i == n: 
                return 1
            
            if s[i] == "0": 
                return 0
            
            lh, rh = 0, 0
            
            lh = fn(i + 1)
            
            if i+1 < n: 
                if (s[i] == "1" or (s[i] == "2" and s[i+1] <= '6')):
                    rh = fn(i+2)

            return (lh + rh)

        return fn(0)
        