class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)
        digits = len(binary)
        total = 0
        i = 32 - digits
        for bit in bin(n):
            if bit == "1":
                total += 2**i
            i += 1
        return total