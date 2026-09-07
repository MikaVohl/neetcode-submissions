class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for bit in bin(n)[2:]:
            count += int(bit)
        return count
