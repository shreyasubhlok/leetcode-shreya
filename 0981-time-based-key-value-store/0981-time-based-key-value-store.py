class TimeMap:

    def __init__(self):
        # Initialize the keystore dictionary to hold lists of [value, timestamp] pairs for each key
        self.keystore={}
    
    #Time is o(1) and space o(n)
    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key does not exist in the keystore, initialize it with an empty list
        if key not in self.keystore:
            self.keystore[key]=[]
        # Append the value-timestamp pair to the list associated with the key
        self.keystore[key].append([value,timestamp])
        
    #Time o(logn) and space o(1)
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keystore:
            return ""
        
        res=""
        values=self.keystore[key] # Retrieve the list of [value, timestamp] pairs for the given key
        l=0
        r=len(values)-1
        while l<=r:
            mid=(l+r)//2
            if values[mid][1]<=timestamp:
                # If mid timestamp is <= target, move right to find later timestamps
                res=values[mid][0]
                l=mid+1
            else:
                # If mid timestamp is greater than target, move left
                r=mid-1
        
        return res
                

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)