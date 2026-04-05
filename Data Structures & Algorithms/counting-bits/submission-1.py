class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0
        while n:
            n = n & n - 1
            cnt += 1
        return cnt


    def countBits(self, n: int) -> List[int]:
        
        # res = []

        # for num in range(n+1):
        #     res.append(self.hammingWeight(num))

        # return res

        dp = [0] * (n+1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            
            dp[i] = 1 + dp[i - offset]
        

        return dp

        