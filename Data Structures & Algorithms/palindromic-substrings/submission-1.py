class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        dp = [[False] * n for _ in range(n)]

        def isPalindrome(i, j):

            if i >= j: return True

            if dp[i][j]: 
                return True

            if s[i] == s[j]:
                dp[i][j] =  isPalindrome(i+1, j -1)
                return dp[i][j]
            
            return False

        cnt = 0
        for i in range(n):
            for j in range(i, n):
                if isPalindrome(i, j):
                    cnt += 1

        return cnt