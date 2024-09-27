class Solution:
    # time complexity: o(nlogn) due to sorting
    # space complexity : o(n) for storing the merged intervals
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda interval: interval[0])
        print(intervals)
        
        res = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        # Iterate through the sorted intervals from index 1
        for i in range(1, len(intervals)):
            
            # If overlaps. Update end to the maximum of the current end and the end of the overlapping interval
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                # No overlap, add the merged interval to the result. Update start and end to the current interval
                res.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]

        # Add the last merged interval
        res.append([start, end])
        return res