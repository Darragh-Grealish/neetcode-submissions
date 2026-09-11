"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)
        for i in range(0, len(intervals)-1):
            print(intervals[i+1].start)
            a = intervals[i].end
            b = intervals[i+1].start
            if a > b:
                return False

        return True