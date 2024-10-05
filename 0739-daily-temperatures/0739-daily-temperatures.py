class Solution:
    # time is o(n)
    # space is o(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  # Stores pairs of [temperature, index] ->[[][][]]
        for i in range(len(temperatures)):
            # Compare current temperature with the temperature at the top of the stack
            # The stack only contains temperatures that haven't yet found a warmer day
            current_temp = temperatures[i]
            while stack and stack[-1][0] < current_temp:
                temp, index = stack.pop()  # Pop from the stack since we found a warmer day
                res[index] = i - index  # Calculate the number of days it took to find a warmer day
            stack.append([current_temp, i])  
        return res



'''
Algorithm Overview
Initialize:
Create a result list res to store the number of days until a warmer temperature for each day.
Use a stack to keep track of the indices of temperatures that haven't found a warmer day.
Iterate Through Each Day:

For each temperature, check if the current temperature is warmer than the temperatures represented by the indices in the stack.
If it is warmer, pop indices from the stack and update the res list with the number of days until the warmer temperature.
Update the Stack:

Push the current day's index onto the stack for future comparisons.
Return the Result:

After processing all temperatures, return the result list.

'''