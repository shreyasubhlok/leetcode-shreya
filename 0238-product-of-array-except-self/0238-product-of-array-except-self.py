class Solution:
    # Time: o(n) - check img leethub
    # space: o(1), The space complexity is O(1) for auxiliary space since the res array is considered the output and doesn't count toward extra space as given in question.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix  # Store the current prefix product at res[i]
            prefix = prefix * nums[i]  # Update the prefix product by multiplying with nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):  # Traverse the array in reverse
            res[i] = res[i] * postfix  # Multiply the current res[i] (which holds the prefix product) with the postfix product
            postfix = postfix * nums[i]  # Update the postfix product by multiplying with nums[i]
        return res
