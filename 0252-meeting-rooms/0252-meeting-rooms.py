class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort the intervals based on start time
        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(intervals)
        for i in range(len(intervals) - 1):
            # Check if the current meeting's end time is greater than the next meeting's start time
            if intervals[i][1] > intervals[i + 1][0]:
                return False  # If true, an overlap is detected, meaning it's impossible to attend both meetings
            
        return True  # No overlap, that means can attend all meetings
        
        