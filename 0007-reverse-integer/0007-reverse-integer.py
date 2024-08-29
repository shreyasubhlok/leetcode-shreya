class Solution:
    # Time Complexity: O(log10(n)) and Space Complexity: O(1)
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1

        reversedNo = 0
        x = abs(x)

        while x != 0:
            remainder = x % 10  # Get the last digit of the number
            # Check for overflow before multiplying by 10
            if reversedNo > (2**31 - 1) // 10: 
                return 0
            reversedNo = reversedNo * 10 + remainder # Build the reversed number
            x = x // 10 # Remove the last digit from the original number

        return sign * reversedNo
