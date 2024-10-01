class Solution:
    # time: o(n)
    # space: o(1)
    def myAtoi(self, s: str) -> int:
        # Step 1: Handle leading whitespace by removing spaces at the beginning
        s = s.lstrip()

        # If the string is empty after removing leading spaces, return 0
        if not s:
            return 0

        # Step 2: Handle the sign
        i = 0
        sign = 1  # Default sign is positive
        if s[i] == '+':  # If the first character is '+', move to the next character
            i = i + 1
        elif s[i] == '-':  # If the first character is '-', set sign to negative and move to the next character
            i = i + 1
            sign = -1

        # Step 3: Convert the remaining part to an integer
        parsed = 0  # Variable to hold the resulting integer value
        while i < len(s):
            curr = s[i]
            if not curr.isdigit():  # If the current character is not a digit, stop the conversion
                break
            else:
                parsed = parsed * 10 + int(curr)
            i = i + 1

        # Multiply the parsed number by its sign
        parsed = parsed * sign

        # Step 4: Handle overflow and underflow cases
        # If the parsed value exceeds the 32-bit signed integer range, return the appropriate boundary value
        if parsed > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif parsed <= -2 ** 31 - 1:
            return -2 ** 31
        else:
            return parsed

