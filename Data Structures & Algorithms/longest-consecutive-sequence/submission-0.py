class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        first = set(nums)
        for n in nums:
            first.discard(n+1)

        nums_set = set(nums)
        best = 0
        for start in first:
            count = 1
            i = start
            while True:
                i += 1
                if i in nums_set:
                    count += 1
                else:
                    break
            best = max(best, count)
        return best
