class Solution:

    # Exponentiation by squaring, which reduces time complexity to O(log n) and space complexity to O(1)
    # Iterative approach, which is generally more preferable for space efficiency.
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n != 0:
            if n % 2 == 1:  # Check if n is odd
                res = res * x  # Multiply by x for odd power    
            x = x * x
            n = n // 2  # Reduce n by half (integer division)

        return res

    # Time Complexity: O(log n) due to halving n with each recursive call.
    # Space Complexity: O(log n) due to the recursive call stack.
    def myPowRecursive(self, x: float, n: int) -> float:

        def pow(x: float, n: int) -> float:
            if x == 0:
                return 0
            if n == 0:
                return 1
            if n == 1:
                return x
            temp = pow(x, n // 2)
            if n % 2 == 0:
                return temp * temp
            else:
                return x * temp * temp

        if n < 0:
            return pow(1 / x, -n)
        else:
            return pow(x, n)

    # Time Complexity: O(n), space complexity: O(1)
    def myPowBruteForceIterative(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n

        res = 1.0
        while n != 0:
            res = res * x
            n = n - 1

        return res
