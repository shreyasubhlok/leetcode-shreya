class Solution:

    # Exponentiation by squaring, which reduces time complexity to O(log n) and space complexity to O(1)
    # Iterative approach, which is generally more preferable for space efficiency.
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x  # Invert the base
            n = -n  # Make exponent positive

        res = 1.0
        while n != 0:
            if n % 2 == 1:  # Check if n is odd
                res = res * x  # Multiply by x for odd power
            x = x * x  # Square the base for the next iteration
            n = n // 2  # Reduce n by half (integer division)

        return res

    # This method calculates x raised to the power n using a recursive approach
    # Time Complexity: O(log n) due to halving n with each recursive call.
    # Space Complexity: O(log n) due to the recursive call stack.
    def myPowRecursive(self, x: float, n: int) -> float:
        # Helper function to perform recursive power calculation
        def pow(x: float, n: int) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            temp = pow(x, n // 2)  # Recursively calculate the power for half of n
            # If n is even, multiply temp by itself
            if n % 2 == 0:
                return temp * temp
            else:
                return x * temp * temp  # If n is odd, multiply by an extra x

        if n < 0:
            return pow(1 / x, -n)  # Invert x and make n positive
        else:
            return pow(x, n)  # Call the helper function for positive n

    # This method calculates x raised to the power n using a brute force iterative approach
    # Time Complexity: O(n) as it multiplies x n times.
    # Space Complexity: O(1) since it uses a constant amount of space.
    def myPowBruteForceIterative(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n != 0:
            res = res * x
            n = n - 1

        return res



