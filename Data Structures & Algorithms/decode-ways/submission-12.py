class Solution:
    def numDecodings(self, s: str) -> int:

        # n = len(s)
        # dp = [-1] * (n+1)
        

        # fn(i) -> possible way of s from i to n
        # dp[i] -> same as fn(i)


        # def fn(i):

        #     if i == n: 
        #         return 1
            
        #     if s[i] == "0": 
        #         return 0
            
        #     if dp[i] != -1:
        #         return dp[i]

        #     lh, rh = 0, 0
            
        #     lh = fn(i + 1)
            
        #     if i+1 < n: 
        #         if (s[i] == "1" or (s[i] == "2" and s[i+1] <= '6')):
        #             rh = fn(i+2)

        #     dp[i] = (lh + rh)
        #     return dp[i]

        # return fn(0)

        n = len(s)
        dp = [0] * (n+1)

        dp[n] = 1


        for i in range(n - 1, -1, -1):

            if s[i] == "0": 
                dp[i] = 0
            
            else:
                dp[i] += dp[i+1]
                if i+1 < n: 
                    if (s[i] == "1" or (s[i] == "2" and s[i+1] <= '6')):
                        dp[i] += dp[i+2]

        return dp[0] 
        

        