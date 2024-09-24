# https://neetcode.io/problems/meeting-schedule


class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals=sorted(intervals , key=lambda intervals: intervals.start)
        # print(intervals)
        for i in range(1,len(intervals)):
            if intervals[i-1].end>intervals[i].start:
                # print(i)
                return False
        return True
            