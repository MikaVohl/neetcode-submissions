class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        start = 0
        end = len(s) - 1
        while start < end:
            if not self.alphanumeric(ord(s[start])):
                start += 1
                continue
            if not self.alphanumeric(ord(s[end])):
                end -= 1
                continue

            # while not self.alphanumeric(ord(s[start])) and start < end:
            #     start += 1
            # while not self.alphanumeric(ord(s[end])) and start < end:
            #     end -= 1
            if s[start] != s[end]: return False
            start += 1
            end -= 1
        return True


    def alphanumeric(self, s):
        return s >= ord('a') and s <= ord('z') or s >= ord('0') and s <= ord('9')