class Solution:
    # time is o(n) and space is o(1)
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize j as -1 to identify if there is any zero in the list
        j = -1

        # First pass: Find the first zero in the list.
        for i in range(len(nums)):
            if nums[i] == 0:
                j = i
                break  # Stop after finding the first zero.

        # If no zero is found, return the list as it is.
        if j == -1:
            return

        # Second pass: Move all non-zero elements after the first zero to the front.
        for i in range(j + 1, len(nums)):
            if nums[i] != 0:
                # Swap the current non-zero element with the zero at index j.
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                # Move j to the next zero position.
                j = j + 1


"""

Brute force will be use of extra temp variable so space o(n) and time o(1)
so better approach is two pointer approach (written above code).

Explanation of the Code:
Step 1: Initial Setup (j = -1):

step 2: This is used to track the position of the first zero in the list. If no zero is found, j remains -1, and the function returns the original list.
First Loop (Finding the First Zero):

step 3:The loop iterates over the list to find the first occurrence of zero. Once found, the loop breaks, and j is set to the index of that zero.
Second Loop (Swapping Non-Zero Elements):

step 4: This loop starts from j + 1 and checks for non-zero elements.
When a non-zero element is found, it is swapped with the zero at position j, and j is incremented to point to the next zero.

Dry Run:
nums = [0,1,0,3,12]
j=0
i=j+1=1 

0 1 0 3 12 (swap)
j i
step 3- 
iteration 1: 1 0 0 3 12 (no swap)
               j i

iteration2: 1 0 0 3 12 (swap)
              j   i     
iteration2: 1 3 0 0 12  (swap)   
                j   i
final 1 3 12 0 0 
              







"""
