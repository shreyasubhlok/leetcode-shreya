class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left = 0  # Pointer to the left boundary of the window
        right = 0  # Pointer to the right boundary of the window
        odd_count = 0  # To count the number of odd numbers in the window
        final_count = 0  # To store the total number of valid subarrays
        temp_count = 0  # To store the number of subarrays for a given window

        while right < len(nums):
            # Check if nums[right] is odd
            if nums[right] % 2 != 0:
                odd_count += 1  # Increment odd count if current number is odd
                temp_count = 0  # Reset temp_count whenever a new odd number is encountered

            # When odd_count equals k, check how many subarrays can be formed
            while odd_count == k:
                temp_count += 1  # We can form a subarray ending at 'right' with exactly k odd numbers
                # If nums[left] is odd, decrement the odd count as we move 'left' pointer
                if nums[left] % 2 != 0:
                    odd_count -= 1
                left += 1  # Move left pointer to shrink the window

            # Add the number of valid subarrays for this window ending at 'right'
            final_count += temp_count

            right += 1  # Expand the window by moving right pointer

        return final_count
