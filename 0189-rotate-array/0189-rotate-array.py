from typing import List


class Solution:
    #Approach 2: Preferred approach is using reverse
    # Time Complexity: O(n) because we reverse the array three times.
    # Space Complexity: O(1) as no extra space is used.
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k >= n

        # Helper function to reverse part of the array
        def reverse(start: int, end: int):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(0, n - 1)
        # Step 2: Reverse the first k elements
        reverse(0, k - 1)
        # Step 3: Reverse the remaining n - k elements
        reverse(k, n - 1)

    # Approach 1-using extra space
    # Time : o(n) and space:o(n)
    def rotateByCalculatingNewIndex(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n  # Handle cases where k >= n by taking the modulus
        
        # Create a new list of the same length as nums to store the result
        res = [0] * len(nums)
        
        # Iterate through the original array and place each element at its new rotated position
        for i in range(len(nums)):
            res[(i + k) % n] = nums[i]  # Calculate the new index for each element

        # Modify nums in-place to match res
        for i in range(len(nums)):
            nums[i] = res[i]
