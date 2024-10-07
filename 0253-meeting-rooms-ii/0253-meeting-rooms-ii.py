from typing import List
import heapq


class Solution:
    '''
    # Time Complexity: O(N log N) where N is the number of intervals. This is due to sorting bacsed on start time and min_heap.
      inserting/removing elements from the heap for each interval takes O(log N).
    # Space Complexity: O(N) for storing the start and end times, coz of min_heap
    # preferable approach is min_heap
    '''

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0

        if len(intervals) == 1:
            return 1

        # Sort intervals by their start time
        intervals = sorted(intervals, key=lambda x: x[0])
        print(intervals)

        # Initialize a min-heap and add the end time of the first meeting
        min_heap = []
        heapq.heappush(min_heap, intervals[0][1])

        # Iterate through all remaining intervals, starting from second interval.
        for i in range(1, len(intervals)):
            # If the current meeting starts after the earliest ending meeting
            if intervals[i][0] >= min_heap[0]:
                heapq.heappop(min_heap)
                
            # Push the end time of the current meeting onto the heap
            heapq.heappush(min_heap, intervals[i][1])

        return len(min_heap)

    
    
    # Time Complexity: O(N log N) where N is the number of intervals. This is due to sorting the start and end times.
    # Space Complexity: O(N) for storing the start and end times.
    def minMeetingRoomsAnotherApproach(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        if len(intervals) == 1:
            return 1

        # Separate the start and end times
        start_times = sorted(x[0] for x in intervals)
        print(start_times)
        end_times = sorted((x[1] for x in intervals))
        print(end_times)

        start, end = 0, 0
        roomsNeeded, maxRooms = 0, 0

        # Iterate over all start times to determine room requirements
        while start < len(intervals):
            # A new meeting starts before the current one ends, need a new room
            if start_times[start] < end_times[end]:
                roomsNeeded += 1
                start = start + 1
            else:
                # The current meeting ends, we can reuse a room
                roomsNeeded -= 1
                end = end + 1

            # Update the maximum number of rooms needed
            maxRooms = max(maxRooms, roomsNeeded)
        return maxRooms