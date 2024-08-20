class Solution:
    # Time complexity is o(n)
    # Space complexity is o(n) - coz of dictionary myMap
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}  # Initialize an empty dictionary to store indicies of each nums[i]
        for i in range(len(nums)):
            difference = target - nums[i]  # calculate the difference
            if difference in myMap:
                # if difference already exists in myMap then return current indicies and no that matches the difference
                return [
                    i,
                    myMap[difference],
                ]  # or return [i,myMap.get(difference)] -this is also correct
            myMap[nums[i]] = i


"""
myMap[difference] VS myMap.get(difference)
myMap[difference] -> raise a keyError if difference not found in dictionary
myMap.get(difference) -> return None if difference not found in dictionary, rather then raising the keyError
For your current code - Since you are already checking whether difference exists in myMap or not, so you can use both.
But stick to myMap[difference] as it's more direct and efficient.
Another way- same time and space
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict ={}
        res=[-1,-1]
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in myDict:
                res[0]=i
                res[1]=myDict[diff]
            myDict[nums[i]]=i   
        return res     
'''
"""
