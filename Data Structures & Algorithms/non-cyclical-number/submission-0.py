class Solution:
    def isHappy(self, n: int) -> bool:
        def squareDigits(num):
            total = 0
            for i in str(num):
                total += int(i)**2
            return total
        
        seen = set()
        curr = n
        while curr not in seen and curr != 1:
            seen.add(curr)
            curr = squareDigits(curr)
        return curr == 1
            
        