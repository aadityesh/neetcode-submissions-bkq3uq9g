class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for string in strs:
            res = res + string + ":@:"

        return res

    def decode(self, s: str) -> List[str]:

        n = len(s)
        L = 0
        R = 0

        result = []

        while R < n:
            while s[R] != ':': 
                R += 1
            if s[R:R+3] == ":@:":
                result.append(s[L:R])
                L = R + 3
                R = L
            elif s[R] == ':' and s[R:R+3] != ":@:":
                result.append(s[R])
                L = R + 4
                R = L
        return result


