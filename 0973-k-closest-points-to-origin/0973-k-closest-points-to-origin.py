class Solution:
    #sort() takes onlogn. So better to use heap implementation. onlogk is better then onlogn
    # Time complexity: O(nlogK), the heap can have at most k elements, each insertion takesOlogk time so o(n)+ologk
    # space complexity : O(K), The heap stores at most k points, so the space complexity is proportional to k
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Define a function to calculate the squared distance from the origin
        def distance(x: int, y: int) -> int:
            return x**2 + y**2

        max_heap = []
        for point in points:
            x = point[0]
            y = point[1]

            # Calculate the negative of the distance (to simulate max heap behavior)
            d = -distance(x, y)

            # Push the (negative distance, point) tuple onto the heap
            heapq.heappush(max_heap, (d, point))

            # If the heap size exceeds k, pop the largest element (i.e., the farthest point) -only k smallest will be remaining in max_heap
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        # Extract the k closest points from the heap
        return [point for (d, point) in max_heap]
        """
        Another way to return res:
        res = []
        while len(max_heap) != 0:
            _, val = heapq.heappop(max_heap)
            res.append((val))
        print("res ->", res)
        Note: In Python, _, point is a way of unpacking a tuple where you only care about one of the values.
        Explanation: Tuple Unpacking: When you have a tuple like (distance, point) and you only care about point, 
        you use _ as a placeholder for the value you want to ignore. _ is a conventional way to indicate that the variable is intentionally unused.
        """


if __name__ == "__main__":
    """
    Heap Visualization :
             [-18, [3, 3]]
                /    \
     [-5, [1, 2]]    [-1, [0, 1]]
    """
    # points = [[3, 3], [5, -1], [-2, 4]]
    points = [[1, 2], [2, 3], [3, 4], [4, 5], [5, -1]]
    k = 3
    sol = Solution()
    res = sol.kClosest(points, k)
    print("973. K Closest Points to Origin: ", res)


"""
Why Max Heap:
Max Heap vs. Min Heap: In this problem, we need to keep track of the k closest points to the origin. By using a max heap, we can efficiently discard 
the farthest point when the heap size exceeds k. If we used a min heap, we would have to maintain all points and extract the k closest points 
in a more complex manner.
Efficiency: By simulating a max heap using negative distances, we maintain a fixed size heap of size k, where insertion and deletion operations are 
O(logk). This approach ensures that we only store k points in the heap at any time, which is efficient both in terms of time and space.
"""
