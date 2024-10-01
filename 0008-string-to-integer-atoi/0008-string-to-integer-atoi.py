class Solution:
    def myAtoi(self, s: str) -> int:
        # case whitespace handling
        s = s.lstrip()
        if not s:
            return 0

        # case sign handling
        i = 0
        sign = 1
        if s[i] == '+':
            i = i + 1
        elif s[i] == '-':
            i = i + 1
            sign = -1

        # convertion
        parsed = 0
        while i < len(s):
            curr = s[i]
            if not curr.isdigit():
                break
            else:
                parsed = parsed * 10 + int(curr)
            i = i + 1

        parsed = parsed * sign

        # rounding
        if parsed > 2 ** 31 - 1:
            return 2 ** 31 - 1
        elif parsed <= -2 ** 31:
            return -2 ** 31
        else:
            return parsed