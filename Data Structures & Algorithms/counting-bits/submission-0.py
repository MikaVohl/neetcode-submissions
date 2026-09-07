class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        dp[0] = 0
        offset = 1
        for i in range(1, n+1):
            if offset * 2 == i: offset = i
            dp[i] = 1 + dp[i - offset]
        return dp

"""
1 2 4 8 16 32

if 2^n <= i < 2^(n+1):
    dp[i] = dp[i - 2^n]

1 -> n=0
2 -> n=1
3 -> n=1
4 -> n=2
5 -> n=2
6 -> n=2
7 -> n=2
8 -> n=3
9 -> n=3
10 -> n=3


0: 0  -> 0
1: 1  -> 1
2: 10  -> 1
3: 11  -> 2
4: 100  -> 1
5: 101  -> 2
6: 110  -> 2
7: 111  -> 3
8: 1000  -> 1
9: 1001  -> 2
10: 1010  -> 2
11: 1011  -> 3
12: 1100  -> 2


add 1, minus 1 for the length of repeating ones in the back

even numbers will have 0 in the back
odd numbers will have 1 in the back

"""