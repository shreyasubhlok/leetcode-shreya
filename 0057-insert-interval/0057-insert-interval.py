class Solution:
    # time complexity: o(n)
    # space complexity : o(n)

    def insert(self, intervals: List[List[int]], newInteval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInteval]  # Return the new interval as the only interval

        res = []
        start = newInteval[0]
        end = newInteval[1]
        n = len(intervals)
        i = 0
        # case:1: current interval ends before the new interval starts (Add all intervals that             end before the new interval starts- No overlapping before merging newInterval)
        while i < n and intervals[i][1] < start:  # checks currInterval end < start ?
            res.append(intervals[i])
            i = i + 1

        # case 2: there is an overlap and needs merging
        while i < n and intervals[i][0] <= end:  # checks currInterval start <= end ?
            start = min(intervals[i][0], start)  # Adjust start to the smallest starting point
            end = max(intervals[i][1], end)  # Adjust end to the largest ending point
            i = i + 1
        res.append([start, end])

        # case 3: current interval starts after the new interval ends (Add all the intervals               that starts after the new interval ends - No overlapping after merging newInterval)
        while i < n:
            res.append(intervals[i])
            i = i + 1

        return res