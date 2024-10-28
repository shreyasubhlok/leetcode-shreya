class Solution:
    # time o(n) and space o(1)
    def trap(self, height: List[int]) -> int:
        # Initialize pointers to start (left) and end (right) of the height array.
        left = 0
        right = len(height) - 1

        # Variables to store the maximum height seen from the left and right sides.
        maxLeft = 0
        maxRight = 0

        # Variable to accumulate the total amount of trapped water.
        ans = 0
        # Iterate while the left pointer is less than the right pointer.
        while left < right:
            # Check if the current height at the left pointer is less than or equal to the height at the right pointer.
            if height[left] <= height[right]:
                # Update the max height encountered so far from the left side.
                maxLeft = max(maxLeft, height[left])
                # Calculate water trapped at the current left position and add it to the answer.
                ans = ans + maxLeft - height[left]
                # Move the left pointer one step to the right
                left = left + 1
            else:
                # Update the max height encountered so far from the right side.
                maxRight = max(maxRight, height[right])
                # Calculate water trapped at the current right position and add it to the answer.
                ans = ans + maxRight - height[right]
                # Move the right pointer one step to the left.
                right = right - 1
        return ans  # total amount of trapped water.

