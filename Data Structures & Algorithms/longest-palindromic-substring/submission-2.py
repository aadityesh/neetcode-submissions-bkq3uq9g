class Solution:

    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        substrings = []

        def palindrome(s):
            return s == s[::-1]

        def generate_substr(curr, i):

            if i >= n: 
                substrings.append(curr)
                return

            generate_substr(curr + s[i], i + 1)
            generate_substr(curr, i + 1)
        
        generate_substr("", 0)

        currLen = float("-inf")
        res = ""

        for strs in substrings:
            if palindrome(strs) and currLen < len(strs):
                currLen = len(strs)
                res = strs
        
        return res


