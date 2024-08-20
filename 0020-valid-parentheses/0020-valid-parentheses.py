class Solution:
    def isValid(self, s: str) -> bool:
        # time complexity is o(n)- The function iterates through each character in s exactly once (for char in s: loop).
        # space complexity is o(n)- use stack to store opening parentheses as it iterates through s
        stack = []  # Initialize an empty stack
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)  # Push opening parentheses onto the stack
            else:
                if len(stack) == 0:
                    return False  # If stack is empty and we encounter a closing parenthesis, it's invalid
                top = (stack.pop())  # Pop the top element from stack (last opened parenthesis)
                if ((char == ")" and top == "(") or (char == "]" and top == "[") or (char == "}" and top == "{")):
                    continue  # If current closing parenthesis matches the top of stack, continue checking
                else:
                    return False  # If mismatched parentheses, return False immediately
        return (len(stack) == 0)  # Ensure stack is empty after processing all characters in s


"""
len(stack) == 0: This checks if the stack is empty by comparing its length to 0.
If len(stack) == 0 evaluates to True, it means that the stack is empty, indicating that all opening parentheses have been matched with corresponding closing parentheses.
If len(stack) == 0 evaluates to False, it means that there are still unmatched opening parentheses left in the stack, so the string s is not valid.
"""
