from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        if n == 0: return 0

        L, R, longest = 0, 0, 1
        current_hash = defaultdict(int)

        while R < n:

            if current_hash[s[R]] >= 1:
                current_hash = defaultdict(int)
                L = L + 1
                R = L
                continue

            longest = max(longest, R - L + 1)
            current_hash[s[R]] += 1
            R += 1

        return longest
                
        