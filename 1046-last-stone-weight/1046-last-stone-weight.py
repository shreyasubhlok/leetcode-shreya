class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        min_heap = []
        k = 2
        while len(stones)!=1:
            for stone in stones:
                heapq.heappush(min_heap, stone)
                if len(min_heap) > k:
                    heapq.heappop(min_heap)

            diff = min_heap[1] - min_heap[0]
            stones.append(diff)
            stones.remove(min_heap[1])
            stones.remove(min_heap[0])
            min_heap=[]

        return stones[0]