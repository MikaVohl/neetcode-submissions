class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        remainder = 1
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += remainder
            if digits[i] > 9:
                digits[i] -= 10
                remainder = 1
            else:
                return digits
        if remainder:
            return [1] + digits