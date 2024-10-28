class TimeMap:

    def __init__(self):
        # Initialize the keystore dictionary to hold lists of [value, timestamp] pairs for each key
        self.keystore = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key does not exist in the keystore, initialize it with an empty list
        if key not in self.keystore:
            self.keystore[key] = []
        # Append the value-timestamp pair to the list associated with the key
        self.keystore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # If the key doesn't exist in keystore, return an empty string
        if key not in self.keystore:
            return ""
        
        values = self.keystore[key]  # Retrieve the list of [value, timestamp] pairs for the given key
        l, r = 0, len(values) - 1
        res = ""  # Default result if no timestamp matches

        # Binary search for the largest timestamp <= the given timestamp
        while l <= r:
            mid = (l + r) // 2
            if values[mid][1] <= timestamp:
                # If mid timestamp is <= target, move right to find later timestamps
                res = values[mid][0]  # Tentatively set res to the current value
                l = mid + 1
            else:
                # If mid timestamp is greater than target, move left
                r = mid - 1

        return res
                

# Usage Example:
# obj = TimeMap()
# obj.set("foo", "bar", 1)
# print(obj.get("foo", 1)) # Outputs "bar"
# print(obj.get("foo", 3)) # Outputs "bar" since the closest timestamp <= 3 is 1
