class Solution:

    def encode(self, strs: List[str]) -> str:
        
        res = ""

        for string in strs:
            res = res + string + "#@#"

        return res

        # for string in strs:
        #     res = res + str(len(string)) + "#" + string
        # print(res)
        # return res

    def decode(self, s: str) -> List[str]:

        n = len(s)
        L = 0
        R = 0

        result = []

        while R < n:
            while s[R] != '#': 
                R += 1
            if s[R] == "#":
                if s[R:R+3] == "#@#":
                    result.append(s[L:R])
                    L = R + 3
                    R = L
                else:
                    R += 1
        return result

        # while L < n:
        #     R = L
        #     while s[R] != "#": R += 1
        #     length = int(s[L:R])
        #     result.append(s[R+1:R+length+1])
        #     L = R + length + 1
        # print(result)
                    

        return result    








