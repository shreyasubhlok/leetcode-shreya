class Solution:
    '''
    Time: O(nlogk)
    The first step which counts the frequencies of each number in nums, takes O(n) time, where n is the number of elements in     nums.
    The second loop iterates through the counterMap, where the heappush operation takes O(log k) time.
    Space: o(n) ~= o(n+k), The space used by the min-heap is O(k)
    '''
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        # Step 1: Create a frequency counter map
        counterMap = {}
        for i in range(len(nums)):
            if nums[i] in counterMap.keys():
                counterMap[nums[i]] += 1
            else:
                counterMap[nums[i]] = 1
        print(counterMap)

        minHeap = []  # Initialize a min-heap to store the top k frequent elements
        # Step 2: Use a min-heap to maintain the top k frequent elements
        for num, count in counterMap.items():
            heapq.heappush(minHeap, (count, num))  # Push the current (count, num) pair onto the min-heap
            # If the heap size exceeds k, remove the least frequent element. Smallest count freq will be at root of heap
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        # Step 3: Extract the numbers from the min-heap into the result list
        while minHeap:
            count, num = heapq.heappop(minHeap)  # Get the least frequent element
            res.append(num)  # Add the number to the result list

        return res