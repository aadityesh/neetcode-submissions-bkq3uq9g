class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
            Brute:
                Sort both strings and compare
                T/S: O(NlogN)/O(N)
            
            Better:
                Hash both strings and compare whether both hashmaps
                are equal or not

                T/S: O(2N)/O(2N)

            
            
        """
        if len(s) != len(t): return False

        # Brute:
        # return sorted(s) == sorted(t)

        # Better
        hash_s = {}
        hash_t = {}

        for index in range(len(s)):
            hash_s[s[index]] = hash_s.get(s[index], 0) + 1
            hash_t[t[index]] = hash_t.get(t[index], 0) + 1
        
        return hash_s == hash_t
            












