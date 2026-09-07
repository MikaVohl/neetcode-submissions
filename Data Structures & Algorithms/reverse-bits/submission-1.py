class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit = (n >> i) & 1 # extract the ith bit (from the left) from binary representation of n
            res += (bit << (31 - i))
        return res