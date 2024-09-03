
class Solution:
    # time is o(n):Pushing and popping operations from the stack are O(1), so overall, the time complexity is O(n), where n is the number of tokens.
    # space is o(n):In the worst case, all tokens could be stored in the stack, so the space complexity is O(n), where n is the number of tokens.
    def evalRPN(self, tokens: List[int]) -> int:
        if len(tokens) == 0:
            return 0

        stack = []
        for t in tokens:
            # Check if the token is an operator
            if t in "+-*/":
                # Pop the top two elements from the stack; b is the second operand, a is the first operand
                b = int(stack.pop())
                a = int(stack.pop())

                # Perform the appropriate arithmetic operation based on the operator
                if t == "+":
                    res = a + b
                elif t == "-":
                    res = a - b
                elif t == "*":
                    res = a * b
                else:
                    # Perform integer division and truncate towards zero to handle cases like ["0", "3", "/"]
                    res = int(a / b)
                stack.append(res)  # push res to stack
            else:
                stack.append(int(t))  # convert to int and push it to stack to perform arithmatic operation
        return stack[0]  # final result will be only one element left in stack which is stack[0]


                    
                