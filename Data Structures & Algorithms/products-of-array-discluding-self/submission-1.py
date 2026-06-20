class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            prod = 1
            for j, n in enumerate(nums):
                if i != j:
                    prod *= n
            out.append(prod)
        return out