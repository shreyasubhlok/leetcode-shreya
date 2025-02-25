class BucketNode:
    def __init__(self, count):  # constructor for bucket
        self.count = count  # store the count for this bucket
        self.keys = set()  # keep track of all keys with this count
        self.prev = None  # pointer to the previous node
        self.next = None  # pointer to the next node


class AllOne:
    def __init__(self):  # constructor for the main class
        self.head = BucketNode(float('-inf'))  # create a sentinel head
        self.tail = BucketNode(float('inf'))  # create a sentinel tail
        self.head.next = self.tail  # connect head's next to tail
        self.tail.prev = self.head  # connect tail's prev to head
        self.keyCount = {}  # map key -> bucket node

    def _addBucketAfter(self, newBucket, prevBucket):
        # add a bucket node right after prevBucket in the linked list
        newBucket.prev = prevBucket  # set new bucket's prev
        newBucket.next = prevBucket.next  # set new bucket's next
        prevBucket.next.prev = newBucket  # link the old next to the new bucket
        prevBucket.next = newBucket  # link prevBucket to newBucket

    def _removeBucket(self, bucket):
        # remove this bucket node from the doubly linked list
        bucket.prev.next = bucket.next  # link prev node's next pointer
        bucket.next.prev = bucket.prev  # link next node's prev pointer

    def inc(self, key: str) -> None:
        # increase the count of the given key
        if key in self.keyCount:  # key is already present in some bucket
            currBucket = self.keyCount[key]  # find the bucket
            nxtBucketCount = currBucket.count + 1  # new count
            currBucket.keys.remove(key)
            if currBucket.next.count != nxtBucketCount:
                newBucket = BucketNode(nxtBucketCount)
                self._addBucketAfter(newBucket, currBucket)
            else:
                newBucket = currBucket.next
            newBucket.keys.add(key)
            self.keyCount[key] = newBucket
            if len(currBucket.keys) == 0:
                self._removeBucket(currBucket)
        else:
            if self.head.next.count != 1:
                newBucket = BucketNode(1)
                self._addBucketAfter(newBucket, self.head)
            else:
                newBucket = self.head.next
            newBucket.keys.add(key)
            self.keyCount[key] = newBucket

    def dec(self, key: str) -> None:
        # decrease the count of the given key
        currBucket = self.keyCount[key]
        newCount = currBucket.count - 1
        currBucket.keys.remove(key)
        if newCount == 0:
            del self.keyCount[key]
        else:
            if currBucket.prev.count != newCount:
                newBucket = BucketNode(newCount)
                self._addBucketAfter(newBucket, currBucket.prev)
            else:
                newBucket = currBucket.prev
            newBucket.keys.add(key)
            self.keyCount[key] = newBucket
        if len(currBucket.keys) == 0:
            self._removeBucket(currBucket)

    def getMaxKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        maxBucket = self.tail.prev
        if len(maxBucket.keys) == 0:
            return ""
        return next(iter(maxBucket.keys))

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        minBucket = self.head.next
        if len(minBucket.keys) == 0:
            return ""
        return next(iter(minBucket.keys))

    # ---- MAIN FUNCTION ----


def main():
    obj = AllOne()

    print("Increment 'apple'")
    obj.inc("apple")  # apple = 1
    print("Max Key:", obj.getMaxKey())  # Expected: "apple"
    print("Min Key:", obj.getMinKey())  # Expected: "apple"

    print("\nIncrement 'banana' twice")
    obj.inc("banana")  # banana = 1
    obj.inc("banana")  # banana = 2
    print("Max Key:", obj.getMaxKey())  # Expected: "banana"
    print("Min Key:", obj.getMinKey())  # Expected: "apple"

    print("\nIncrement 'cherry' three times")
    obj.inc("cherry")  # cherry = 1
    obj.inc("cherry")  # cherry = 2
    obj.inc("cherry")  # cherry = 3
    print("Max Key:", obj.getMaxKey())  # Expected: "cherry"
    print("Min Key:", obj.getMinKey())  # Expected: "apple"

    print("\nDecrement 'banana'")
    obj.dec("banana")  # banana = 1
    print("Max Key:", obj.getMaxKey())  # Expected: "cherry"
    print("Min Key:", obj.getMinKey())  # Expected: "apple"

    print("\nDecrement 'apple' (removes apple)")
    obj.dec("apple")  # apple = 0, removed
    print("Max Key:", obj.getMaxKey())  # Expected: "cherry"
    print("Min Key:", obj.getMinKey())  # Expected: "banana"

    print("\nDecrement 'cherry' twice")
    obj.dec("cherry")  # cherry = 2
    obj.dec("cherry")  # cherry = 1
    print("Max Key:", obj.getMaxKey())  # Expected: "banana" or "cherry"
    print("Min Key:", obj.getMinKey())  # Expected: "banana" or "cherry"

    print("\nDecrement 'cherry' to remove it")
    obj.dec("cherry")  # cherry = 0, removed
    print("Max Key:", obj.getMaxKey())  # Expected: "banana"
    print("Min Key:", obj.getMinKey())  # Expected: "banana"


if __name__ == "__main__":
    main()
