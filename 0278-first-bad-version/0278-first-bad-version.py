# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
     #Time complexity- olog(n) as its binary search prob
     #space complexity - o(1)
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = ( left + (right - left) // 2)  # need to ensure exact midpoint calculation in all cases.
            # mid = (left+right) // 2
            # both mid are right.  mid = (left+right) // 2 can cause integer overflow in case of large numbers

            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left

    
'''
working
n=9

bad version list have [5,6,9]

1 2 3 4 5 6 7 8 9 
L               R
mid = 1+(9-1) // 2 = 9//2 4

is 4 badversion - No
so left=mid+1
left=5

is 5 bad version - yes
so right=mid-1
right=4

left is no longer smaller then right so return left
hence output is 5
'''