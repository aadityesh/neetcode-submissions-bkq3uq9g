class Solution:
    def longestPalindrome(self, s: str) -> str:

        dt = {}
        n = len(s)
        self.maxLen = 0
        self.res = ""

        def isPalindrome(cur):
            return cur == cur[::-1]
        
        def helper(cur, i):

            if i >= n: 
                if isPalindrome(cur) and len(cur) > self.maxLen:
                    self.res = cur
                    self.maxLen = len(cur)
                return
                            
            helper(cur + s[i], i + 1)
            helper(cur, i + 1)
        
        helper("", 0)
        return self.res
        