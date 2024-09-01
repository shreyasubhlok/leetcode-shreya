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
    

if __name__ == "__main__":
    sol = Solution()

    # Test Case 1: No Overlap Before (Case 1)
    intervals1 = [[1, 2], [5, 6]]
    newInterval1 = [3, 4]
    print("57. Insert Interval : ")
    print("Test Case 1:", sol.insert(intervals1, newInterval1))  # Expected: [[1, 2], [3, 4], [5, 6]]

    # Test Case 2: Complete Overlap (Case 2)
    intervals2 = [[1, 3], [6, 9]]
    newInterval2 = [2, 7]
    print("Test Case 2:", sol.insert(intervals2, newInterval2))  # Expected: [[1, 9]]

    # Test Case 3: No Overlap After (Case 3)
    intervals3 = [[1, 2], [3, 5]]
    newInterval3 = [6, 7]
    print("Test Case 3:", sol.insert(intervals3, newInterval3))  # Expected: [[1, 2], [3, 5], [6, 7]]

    # Test Case 4: Partial Overlap (Combining Cases)
    intervals4 = [[1, 3], [5, 7], [8, 10]]
    newInterval4 = [6, 8]
    print("Test Case 4:", sol.insert(intervals4, newInterval4))  # Expected: [[1, 3], [5, 10]]

    # Test Case 5: New Interval Encapsulates Existing Interval (Case 2)
    intervals5 = [[1, 3], [7, 9]]
    newInterval5 = [2, 8]
    print("Test Case 5:", sol.insert(intervals5, newInterval5))  # Expected: [[1, 9]]

    # Test Case 6: New Interval Encapsulates Existing Interval (Case 2)
    intervals6 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval7 = [4, 8]
    print("Test Case 5:", sol.insert(intervals6, newInterval7))  # Expected: [[1, 2], [3, 10], [12, 16]]
