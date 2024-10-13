from typing import List


class Solution:
    #Time Complexity: O(n) (where n is the number of elements in nums)
    # Space Complexity: O(k) (where k is the size of the subarray)
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # If the length of nums is less than k, return 0 as no subarray of size k can exist
        if len(nums) < k:
            return 0

        maxsum = 0  # Variable to store the maximum sum of distinct subarrays
        windowsum = 0  # Variable to store the current window sum
        hm = {}  # Hashmap to track the frequency of elements in the current window

        # Initialize the first window of size k
        for i in range(k):
            # Update frequency of the current number in the hashmap
            if nums[i] not in hm:
                hm[nums[i]] = 1
            else:
                hm[nums[i]] += 1

            # Calculate the sum of the first window
            windowsum += nums[i]

            # If the window contains k distinct elements, set maxsum to the current window sum
            if len(hm) == k:
                maxsum = windowsum
                break

        # Initialize pointers for sliding the window
        j = k  # Right pointer for the next element to add
        i = j - k  # Left pointer for the current element to remove

        # Start sliding the window
        while j < len(nums):
            # Remove the leftmost element from the hashmap
            hm[nums[i]] -= 1
            # If the frequency becomes zero, remove it from the hashmap
            if hm[nums[i]] == 0:
                del hm[nums[i]]

            # Current element to be added to the window
            curr = nums[j]

            # Update frequency of the new element in the hashmap
            if curr not in hm:
                hm[curr] = 1
            else:
                hm[curr] += 1

            # Update the current window sum by adding the new element and subtracting the removed element
            windowsum = windowsum + curr - nums[i]

            # Check if the current window contains k distinct elements
            if len(hm) == k:
                # Update maxsum if the current window sum is greater
                maxsum = max(windowsum, maxsum)

            # Move the sliding window pointers to the right
            j += 1
            i += 1

        return maxsum  # Return the maximum sum found


# Test the solution
if __name__ == "__main__":
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    sol = Solution()
    res = sol.maximumSubarraySum(nums, k)
    print("2461. Maximum Sum of Distinct Subarrays With Length K: ", res)
