
# https://www.youtube.com/watch?v=tp8JIuCXBaU
class Solution:
    # https://www.youtube.com/watch?v=tp8JIuCXBaU
    # (Dutch National Flag Algorithm )
    # time complexity = o(n)
    # space complexity = o(1)
    '''
    low=0,mid=0, high=len(nums)-1
    a[mid] == 0  -> swap(a[low], a[mid])
                    low++, mid++
    a[mid] == 1  -> mid++
    a[mid] == 2  -> swap(a[mid], a[high])
                    high--
    '''

    def sortColors(self, nums: List[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

    # (Counting Sort)
    # time complexity = o(2n)
    # space complexity = o(1)
    def sortColorsBetterApproach(self, nums: List[int]) -> None:
        count0 = 0
        count1 = 0
        count2 = 0
        # Count the number of 0s, 1s, and 2s
        for i in range(len(nums)):
            if nums[i] == 0:
                count0 += 1
            elif nums[i] == 1:
                count1 += 1
            else:
                count2 += 1
        # Fill the list with the correct number of 0s, 1s, and 2s
        # Fill the first 'count0' indices of the list with 0s
        for i in range(count0):
            nums[i] = 0
        # Fill the list with the correct number of 1s, starting from index 'count0' and ending at 'count0 + count1'
        for i in range(count0, count0 + count1):
            nums[i] = 1
        # Fill the list with the correct number of 2s, starting from index 'count0 + count1' to the end of the list
        for i in range(count0 + count1, len(nums)):
            nums[i] = 2


