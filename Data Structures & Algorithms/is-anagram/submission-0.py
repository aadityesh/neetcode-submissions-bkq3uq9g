class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Brute:
                Sort both strings and compare
        """
        
        # Brute:
        return sorted(s) == sorted(t)