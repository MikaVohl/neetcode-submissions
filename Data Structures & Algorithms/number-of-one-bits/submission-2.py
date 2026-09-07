class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1 # bitwise and with n-1 will remove the lowest set 1 bit
            count += 1
        return count
