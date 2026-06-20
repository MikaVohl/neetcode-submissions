from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = defaultdict(int)
        dt = defaultdict(int)
        for letter in s:
            ds[letter] += 1
        for letter in t:
            dt[letter] += 1
        return ds == dt

# from collections import defaultdict

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         ds = defaultdict(int)
#         dt = defaultdict(int)
#         for letter in s:
#             ds[letter] += 1
#         for letter in t:
#             dt[letter] += 1
#         if ds.keys() != dt.keys():
#             return False
#         for key, value in ds.items():
#             if dt[key] != value:
#                 return False
#         return True