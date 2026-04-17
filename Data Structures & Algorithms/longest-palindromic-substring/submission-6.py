class Solution:

            
    # def longestPalindrome(self, s: str) -> str:

    #     n = len(s)
    #     substrings = []

    #     def palindrome(s):
    #         return s == s[::-1]

    #     def generate_substr(curr, i):

    #         if i >= n: 
    #             substrings.append(curr)
    #             return

    #         generate_substr(curr + s[i], i + 1)
    #         generate_substr(curr, i + 1)
        
    #     generate_substr("", 0)

    #     currLen = float("-inf")
    #     res = ""

    #     for strs in substrings:
    #         if palindrome(strs) and currLen < len(strs):
    #             currLen = len(strs)
    #             res = strs
        
    #     return res

    
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False] * n for _ in range(n) ]

        def fn(i, j):
            if i >= j:
                return True

            if dp[i][j]: return True

            if s[i] == s[j]:
                dp[i][j] = fn(i + 1, j - 1)
                return dp[i][j]

            return False


        sp, maxLen = -1, float("-inf")
        for i in range(n):
            for j in range(i, n):
                if fn(i, j) and (j - i + 1) > maxLen:
                    maxLen = j - i + 1
                    sp = i
        
        print(sp, maxLen)
        return s[sp:sp+maxLen]

        


