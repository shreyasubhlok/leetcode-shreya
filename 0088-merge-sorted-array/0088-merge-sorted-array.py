from typing import List


class Solution:
    # time is o(n+m)
    # space is o(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start merging from the back of both nums1 and nums2
        i = m - 1 # Pointer for the last valid element in nums1
        j = n - 1 # Pointer for the last element in nums2
        k = m + n - 1  # Pointer for the last position in nums1 where elements should go

        # Merge from back to front to avoid overwriting nums1's values
        while i >= 0 and j >= 0:
            if nums1[i] < nums2[j]:
                nums1[k] = nums2[j]
                j = j - 1
            else:
                nums1[k] = nums1[i]
                i = i - 1
            k = k - 1

        # If there are remaining elements in nums2, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1


