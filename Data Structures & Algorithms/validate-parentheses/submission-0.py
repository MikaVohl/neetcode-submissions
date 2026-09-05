class Solution:
    def isValid(self, s: str) -> bool:
        opening = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c in [')', '}', ']']:
                if len(stack) == 0 or stack[-1] != opening[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return len(stack) == 0