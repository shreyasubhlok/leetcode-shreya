   
class Solution:
    ''''
    Problem Understanding:
    You need to find the minimum eating speed K that allows Koko to eat all the piles of bananas within h hours.
    Remember: Koko can only eat 1 pile per hour

    Time: o(nlogn) => log(n) binary search + O(n)
         Time Complexity: O(n * log m)
         n: The number of piles.
         m: The value of the largest pile (max(piles)).
         The binary search runs in O(log m) time.
         For each possible speed, calculating the total hours takes O(n) time.
         Therefore, the overall time complexity is O(n * log m).

    Space: o(1), very few variables have been used.
    '''

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # If no piles or piles are more than hours available, return 0 as impossible
        if len(piles) == 0 or len(piles) > h:
            return 0

        # If hours match the number of piles, Koko has to eat the largest pile each hour
        if h == len(piles):
            return max(piles)

        left = 1
        right = max(piles)
        res = max(piles)
        while left <= right:
            mid = (left + right) // 2
            totalHour = 0

            # Calculate total hours needed with current speed 'mid'
            for num in piles:
                currHour = math.ceil(num / mid)
                totalHour += currHour

            if totalHour <= h:
                # Update the result with the current minimum eating speed
                res = min(res, mid)
                right = mid - 1  # Try to find a lower speed
            else:
                left = mid + 1  # Increase the eating speed

        return res


