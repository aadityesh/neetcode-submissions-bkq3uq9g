class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        cnt = 0

        for i in range(n):
            if s[i] == "0": continue
            for j in range(i, n):
                # cnt += 1
                print(s[j], end=" ")
            if s[i-1] != '0': cnt += 1
            print("")

        return cnt