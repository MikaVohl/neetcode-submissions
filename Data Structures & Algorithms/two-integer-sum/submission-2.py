from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = defaultdict(int)
        for i, num in enumerate(nums):
            if num in remaining:
                return [min(i, remaining[num]), max(i, remaining[num])]
            remaining[target-num] = i