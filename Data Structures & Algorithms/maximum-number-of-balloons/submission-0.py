class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        res = 0
        
        hash = {}

        requiredHash = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 1,
            'n': 1
        }

        for char in text:
            
            if char in ['b', 'a', 'o', 'n', 'l']:
                if char not in hash:
                    hash[char] = 0
                
                hash[char] += 1

            if len(hash) == len(requiredHash):

                for key, value in hash.items():
                    if hash[key] < requiredHash[key]:
                        break
                
                hash = {}
                res += 1

        
        return res


            


            
        