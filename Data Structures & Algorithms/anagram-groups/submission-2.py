class Solution:

    def sorted_str(s):
        sorted_str_ls = sorted(copy_str)
        key = "".join(sorted_str_ls)
        return key
    
    def customKey(self, s):
        
        hashtable = [0] * 26
        result = ""

        for ch in s:
            hashtable[ord(ch) - ord('a')] += 1
        
        for index, count in enumerate(hashtable):
            if count > 0:
                result += f"{count}{chr(ord('a') + index)}"
        
        return result


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        """

        # Strings which share same length, letters and letters' frequency
        # Order is different

        # [pat, tap, pta] -> sorting -> apt
        # Hashing & Traversal
        
        {
            "apt": [pat, tap, pta]
        }

        hashtable = [0, 0, ... 0], size = 26

        apptt
        [1,..0, 1, 1] -> 1a2p2t 
         0, 14, 19

        if hash[i] > 1: freqELemFreqElemFreqElem



        """

        result = {}

        for string in strs:

            # key = sorted_str(string) T -> N * (mlogm)
            key = self.customKey(string)
            
            if key not in result:
                result[key] = []

            result[key].append(string)
        
        return list(result.values())