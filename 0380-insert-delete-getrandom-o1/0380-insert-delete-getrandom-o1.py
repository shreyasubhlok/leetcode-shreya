
class RandomizedSet:
    '''
Explanation of Why a Hash Set Isn’t Suitable:
A hash set only stores unique values and does not maintain the index of each value. While a hash set could store values and check for existence in O(1), it does not allow access to specific elements or maintain any order, which is required here to remove elements in constant time by swapping with the last element.
A hash map (numMap) stores each value’s index, allowing O(1) index lookups during removal. This index is essential for efficiently swapping elements in numList during deletion, ensuring O(1) deletions without leaving gaps in the list.
numList allows us to select a random element in O(1), which a hash set cannot support directly, as it doesn’t maintain order or indexing.
Using both numMap and numList together ensures all operations—insert, delete, and get random—are O(1).
    '''
    def __init__(self):
        # Initialize a dictionary (hash map) to store the index of each value in numList
        # This allows for O(1) average-time complexity for insertions and deletions.
        self.numMap = {}
        # Initialize a list to store the values for quick access to a random element
        # This list will allow random access in O(1) for getRandom.
        self.numList = []

    def insert(self, val: int) -> bool:
        # Check if the value already exists in the map (O(1) average-time complexity)
        # If it exists, return False (no insertion needed since the value is already present)
        if val in self.numMap:
            return False
        # If it does not exist, add the value to numList and record its index in numMap
        self.numMap[val] = len(self.numList)  # Store index of val in numMap
        self.numList.append(val)  # Add value to the end of the list
        return True  # Return True to indicate successful insertion

    def remove(self, val: int) -> bool:
        # Check if the value exists in the map
        # If it does not exist, return False (cannot remove non-existent value)
        if val not in self.numMap:
            return False
        # Retrieve the index of the element to be removed
        idx = self.numMap[val]
        # Retrieve the last element in the list (for swapping with the element to be removed)
        lastval = self.numList[-1]
        # Replace the element to be removed with the last element in the list
        # This keeps the list compact without creating gaps
        self.numList[idx] = lastval
        # Update the map with the new index of lastval
        self.numMap[lastval] = idx
        # Remove the last element from the list, which is now redundant after the swap
        self.numList.pop()
        # Remove the deleted value from the map
        del self.numMap[val]
        return True  # Return True to indicate successful removal

    def getRandom(self) -> int:
        # Select and return a random element from numList using random.choice
        # Since numList holds all current elements, this operation is O(1)
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as follows:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


