class Solution:
    '''
    Time Complexity: In the worst case, we might push up to k elements   into the heap, and each push/pop operation takes O(log k). 
So the time is approximately O(k log k). That’s a big improvement over the naive O(nm log(nm)).
Space Complexity: O(k) for the heap and O(k) for the result array and visited set, giving us overall O(k).
'''
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Create a list to hold the resulting pairs
        result = []  # empty for now
        # Edge case: if either list is empty or if k=0, just return empty result
        if not nums1 or not nums2 or k == 0:  # check for boundary conditions
            return result  # return empty

        # Initialize a min heap to always pop the pair with smallest sum
        min_heap = []  # we'll push tuples of (sum, i, j)

        # Use a set to keep track of which (i, j) are already visited
        visited = set()  # store index pairs (i, j)

        # Push the first pair (0,0) into the heap, if not visited
        first_sum = nums1[0] + nums2[0]  # compute the sum
        heapq.heappush(min_heap, (first_sum, 0, 0))  # push tuple
        visited.add((0, 0))  # mark (0,0) as visited

        # We need to pop from the heap k times or until we run out of pairs
        while k > 0 and min_heap:  # as long as k is not exhausted and heap not empty
            # Pop the current smallest sum pair
            current_sum, i, j = heapq.heappop(min_heap)  # extract top
            # Add the actual pair (nums1[i], nums2[j]) to result
            result.append([nums1[i], nums2[j]])  # pair with smallest sum so far
            # Decrement k since we found a valid pair
            k -= 1  # one pair used

            # Next potential pairs can be (i+1, j) or (i, j+1), if valid
            next_i = i + 1  # potential next in nums1
            if next_i < len(nums1):  # check boundary
                if (next_i, j) not in visited:  # ensure not visited
                    new_sum = nums1[next_i] + nums2[j]  # sum for new pair
                    heapq.heappush(min_heap, (new_sum, next_i, j))  # push to heap
                    visited.add((next_i, j))  # mark as visited

            next_j = j + 1  # potential next in nums2
            if next_j < len(nums2):  # check boundary
                if (i, next_j) not in visited:  # ensure not visited
                    new_sum = nums1[i] + nums2[next_j]  # sum for new pair
                    heapq.heappush(min_heap, (new_sum, i, next_j))  # push to heap
                    visited.add((i, next_j))  # mark as visited

        return result  # return final pairs with smallest sums
            