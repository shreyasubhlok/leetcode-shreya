
class Solution:
    #time: o(n)
    #space: o(n)
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)  # Convert the input list to a set to allow O(1) lookup time
        longest = 0
        for num in numSet:
            # Check if the number is the start of a sequence.
            if num - 1 not in numSet:  #Only start from the beginning of a sequence
                length = 0

                # Count the length of the consecutive sequence starting from num
                while (num + length) in numSet:
                    length = length + 1

                longest = max(longest, length) # Update the longest sequence length found so far
        return longest