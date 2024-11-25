# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:


class Solution:
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """

    def findCelebrity(self, n: int) -> int:
        if n == 0:
            return -1
        # Step 1: Identify a potential candidate for the celebrity
        candidate = 0
        for i in range(1, n):
            # If the candidate knows i, candidate cannot be a celebrity
            if knows(candidate, i):
                candidate = i

        # Step 2: Verify if the candidate is a valid celebrity
        for i in range(n):
            if i != candidate:
                # Check if the candidate knows i
                if knows(candidate, i):
                    return -1  # Candidate knows someone, not a celebrity
                # Check if i doesn't know the candidate
                elif not knows(i, candidate):
                    return -1  # Not everyone knows the candidate

        return candidate
