class RandomizedSet:

    def __init__(self):
        self.numMap = {}  # Map to store the index of each value in numList
        self.numList = []  # List to store values for quick random access

    def insert(self, val: int) -> bool:
        # If val already exists in the set, return False
        if val in self.numMap:
            return False
        # Otherwise, add the value to numMap and numList
        self.numMap[val] = len(self.numList)  # Store the index in numMap
        self.numList.append(val)  # Add to the list
        return True

    def remove(self, val: int) -> bool:
        # If val does not exist in the set, return False
        if val not in self.numMap:
            return False
        # Retrieve the index of the value to be removed
        idx = self.numMap[val]
        # Get the last element in the list
        lastval = self.numList[-1]
        # Move the last element to the position of the element to be removed
        self.numList[idx] = lastval
        # Update the map with the new index of lastval
        self.numMap[lastval] = idx
        # Remove the last element from the list
        self.numList.pop()
        # Delete the value from the map
        del self.numMap[val]
        return True

    def getRandom(self) -> int:
        # Return a random element from numList
        return random.choice(self.numList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()