class Solution:
    # Time: o(nlogn)-> heapq.heapify(stones) takes O(n) and heappop/heappush operations takes O(log n). o(n) +o(logn)= o(nlogn)
    # space: o(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative to simulate a max-heap using Python's min-heap
        # This way, we can use heapq to always extract the heaviest stone
        for i in range(len(stones)):
            stones[i] = -stones[i]

        # Convert the list into a heap (min-heap, but we use negative values to simulate max-heap)
        # heapify creates min-heap by default in Python, which allows efficient access to the smallest element).
        heapq.heapify(stones)  
        
        while len(stones) > 1:
            # Pop the two heaviest stones (most negative values)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            # If the stones are not equal, push the remaining weight back into the heap
            if stone1 != stone2:
                diff = stone1 - stone2
                heapq.heappush(stones, diff)

        # If there is one stone left, return its positive weight
        if len(stones) != 0:
            return -1 * stones[0]

        # If no stones are left, return 0
        return 0


'''
Time Complexity
heapify:
The time complexity of heapify is O(n), where n is the number of elements in the list. 
This operation builds a heap in a bottom-up manner, ensuring each subtree is heapified starting from the leaves.

sort:
Sorting a list typically takes O(n log n).
'''
