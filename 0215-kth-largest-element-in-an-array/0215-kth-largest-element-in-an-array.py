class Solution:
    # sort() takes onlogn. So better to use heap implementation. onlogk is better then onlogn
    # Time complexity: O(nlogK), the heap can have at most k elements, each insertion takes Ologk time so o(n)+ologk
    # space complexity : O(K), The heap stores at most k points, so the space complexity is proportional to k
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)

            # If the size of the heap exceeds k, remove the smallest element
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]  # The root of the min-heap is the k-th largest element
