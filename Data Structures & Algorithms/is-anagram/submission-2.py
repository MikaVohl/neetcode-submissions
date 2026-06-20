# from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ds = defaultdict(int)
#         dt = defaultdict(int)
#         for letter in s:
#             ds[letter] += 1
#         for letter in t:
#             dt[letter] += 1
#         return ds == dt

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)