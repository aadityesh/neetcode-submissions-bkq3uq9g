class Solution:
    def countSubstrings(self, s: str) -> int:
        

        # i, j -> (0, 4) -> (1, 3) -> (2, 2)


        n = len(s)
        dp = [[False] * n for _ in range(n)]

        # def isPalindrome(i, j):

        #     if i >= j: return True

        #     if dp[i][j]: 
        #         return True

        #     if s[i] == s[j]:
        #         dp[i][j] =  isPalindrome(i+1, j -1)
        #         return dp[i][j]
            
        #     return False

        # cnt = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         if isPalindrome(i, j):
        #             cnt += 1

        # return cnt
        def print_dp(dp):
            for row in dp:
                print(" ".join(['T' if cell else '.' for cell in row]))
            print()

        cnt = 0
        for L in range(1, n+1):
            
            for i in range(n-L+1):  # i + L - 1 < n
                
                j = i + L - 1

                if i == j: 
                    dp[i][j] = True

                elif L == 2 and s[i] == s[j]:
                    dp[i][j] = True
                
                else:
                    dp[i][j] = (s[i] == s[j] and dp[i+1][j-1])
                
                
                if dp[i][j]: 
                    cnt += 1
                
                print(dp)
                print("-----")
        
        return cnt



                





