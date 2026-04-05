class Solution:

    def reverseBits(self, n: int) -> int:

        res = ""
        while n:
            res += str(n % 2)
            n //= 2
        
        zeroes = "0" * (32 - len(res))
        binary_n = res[::-1] + zeroes

        print(f"bin_n: {binary_n}")

        res = 0
        offset = 31

        for bit in binary_n:
            res += (2**offset) * int(bit)
            offset -= 1

        return res

