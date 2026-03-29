class Solution:
    def climbStairs(self, n: int) -> int:

        # self.cnt = 0
        
        # dp = [-1] * (n + 1)

        # def recursion(n):

        #     if n < 0: return 0

        #     if n == 0: 
        #         return 1

        #     if dp[n] != -1: return dp[n]

        #     one_steps = recursion(n - 1)
        #     two_steps = recursion(n - 2)

        #     dp[n] = one_steps + two_steps

        #     return dp[n]

        # return recursion(n)

        a, b, c = 0, 1, 0

        for i in range(n):
            
            c = a + b

            temp = b
            b = c
            a = temp
        
        return c

