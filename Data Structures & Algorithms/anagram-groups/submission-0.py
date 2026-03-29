class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = {}

        for string in strs:
            copy_str = string
            key = str(sorted(copy_str))
            
            if key not in result:
                result[key] = []

            result[key].append(string)
        
        return list(result.values())