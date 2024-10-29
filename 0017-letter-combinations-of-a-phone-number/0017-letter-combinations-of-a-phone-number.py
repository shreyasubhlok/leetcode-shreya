class Solution:
    '''
    See dry run https://pythontutor.com/render.html#mode=display here
    Time complexity: O(4^n), each digit has upto 4 possibile letter (example 7 and 9). Backtrack will general all possible combination so total
    combination is 4^n
    Space: O(4^n), res will hold 4^n combinations in worst case
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        # Backtracking helper function
        def backtrack(i, curStr):
            # Base case: if current string length equals the input digits' length, thn add to res
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            # Get the possible letters for the current digit
            values = digitToChar[digits[i]]

            # Recursive case: iterate over each possible letter and build the combination
            for char in values:
                backtrack(i + 1, curStr + char)  # Move to the next digit and add the letter to current string

        # Edge case: if digits string is empty, return an empty list
        if digits:
            backtrack(0, "")  # Start the backtracking with index 0 and an empty current string

        return res


