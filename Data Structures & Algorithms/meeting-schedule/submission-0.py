"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        starts = sorted(intervals, key = lambda x: x.start)
        lastEnd = 0
        for start in starts:
            if lastEnd != 0 and start.start < lastEnd: return False
            lastEnd = start.end
        return True