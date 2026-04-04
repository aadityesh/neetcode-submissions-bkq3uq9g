class Solution:
    def hammingWeight(self, n: int) -> int:

        cnt = 0
        while n:
            n = n & n - 1
            cnt += 1
        return cnt


    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n+1):
            res.append(self.hammingWeight(num))

        return res