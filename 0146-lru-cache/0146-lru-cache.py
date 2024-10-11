class Node:
    def __init__(self, key, val):
        # Initialize a node for the doubly linked list along with next and prev pointers
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    # time: O(1) for get and put
    # space: o(capacity)  because the cache stores at most capacity nodes in the doubly linked list and the same number of mappings in the dictionary.
    def __init__(self, capacity: int):
        self.cap = capacity  # Initialize the cache with given capacity
        self.cacheMap = {}  # Dictionary to store key-node mappings
        self.head = Node(0, 0)  # Dummy head node for the doubly linked list
        self.tail = Node(0, 0)  # Dummy tail node for the doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head

    # Remove a node from the doubly linked list
    def remove(self, node):
        node.prev.next = node.next  # forward link
        node.next.prev = node.prev  # backword lin

    # Insert a node at the tail (most recent)
    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        node.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        # Get the value of the key if it exists in the cache
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])  # Move accessed node to the end (most recent)
            self.insert(self.cacheMap[key])
            return self.cacheMap[key].val
        return -1  # Return -1 if key does not exist

    def put(self, key: int, value: int) -> None:
        # Add or update a key-value pair in the cache
        if key in self.cacheMap:
            self.remove(self.cacheMap[key])  # Remove old node if key exists
        self.cacheMap[key] = Node(key, value)  # Create a new node and add it to the map
        self.insert(self.cacheMap[key])  # Insert node at the end (most recent)
        if len(self.cacheMap) > self.cap:
            # If capacity is exceeded, remove the least recently used (LRU) node
            leastRecentlyUsed = self.head.next  # Head's next is the LRU node
            self.remove(leastRecentlyUsed)
            del self.cacheMap[leastRecentlyUsed.key]  # Remove LRU node from the map


if __name__ == "__main__":
    lruCache = LRUCache(2)  # Initialize cache with capacity of 2
    lruCache.put(1, 1)  # Cache: {1=1}
    lruCache.put(2, 2)  # Cache: {1=1, 2=2}
    print(lruCache.get(1))  # Access 1 -> returns 1, Cache: {2=2, 1=1}
    lruCache.put(3, 3)  # Adds 3 -> Cache: {1=1, 3=3}, removes LRU 2
    print(lruCache.get(2))  # Access 2 -> returns -1 (not found)
    lruCache.put(4, 4)  # Adds 4 -> Cache: {3=3, 4=4}, removes LRU 1
    print(lruCache.get(1))  # Access 1 -> returns -1 (not found)
    print(lruCache.get(3))  # Access 3 -> returns 3, Cache: {4=4, 3=3}
    print(lruCache.get(4))  # Access 4 -> returns 4, Cache: {3=3, 4=4}
