class Solution:
    # two pointer approach
    # time is o(n)-in place comparison and space is o(n)
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Initialize the result list with zeros, the same size as the input list
        res = [0] * len(nums)

        start = 0
        end = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):  # reverse order iteration (from the last index to the first)
            # Compare the absolute values of the elements at the start and end pointers.
            # The larger square will be placed at the current index `i` in the result list.
            if abs(nums[start]) > abs(nums[end]):
                res[i] = nums[start] * nums[start]  # Square the start element and place it at the current index
                start = start + 1  # Move the start pointer to the right
            else:
                # If the element at the end pointer is larger or equal in absolute value
                res[i] = nums[end] * nums[end]  # Square the end element and place it at the current index.
                end = end - 1  # Move the end pointer to the left.

        return res
    
'''
Dry run -
  nums = [-4, -1, 0, 3, 10]
           S             E
  res = [0 , 0 ,0, 0 ,0]
                      i
iteration 0:
  nums = [-4, -1, 0, 3, 10]
           S         E
  res = [0 , 0 ,0, 0 ,100]
                   i
abs(-4)>abs(10) ? No    res[4]=10*10   End=end-1

iteration 1:
  nums = [-4, -1, 0, 3, 10]
               S     E
  res = [0 , 0 ,0, 16 ,100]
                i
abs(-4)>abs(3) ? yes    res[3]=4*4   start=start+1

iteration 2:
  nums = [-4, -1, 0, 3, 10]
               S     E
  res = [0 , 0 ,9, 16 ,100]
                i
abs(-1)>abs(3) ? No    res[2]=3*3   End=end-1

iteration 1:
  nums = [-4, -1, 0, 3, 10]
               S  E
  res = [0 , 1 ,9, 16 ,100]
         i
abs(-1)>abs(0) ? No    res[1]=1*1   start=start+1


iteration 0:
  nums = [-4, -1, 0, 3, 10]
               S  E
  res = [0 , 1 ,9, 16 ,100]
         i
abs(0)>abs(0) ? No    res[0]=0*0   End=end-1

  res = [0 , 1 ,9, 16 ,100] OUTPUT



Additional=>
 for i in range(len(nums) - 1, -1, -1) : 
 Explanation
  for i in range(start,stop,step):
  len(nums) -> 1 (start) -> starting from reverse order
  -1 (stop) ->ensures that the loop includes index 0 (the first element) and stops before reaching -1
  -1(step) ->This step value of -1 indicates that the loop should move in reverse, decreasing the index by 1 in each iteration
'''
