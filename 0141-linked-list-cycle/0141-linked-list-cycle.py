# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #Time - o(n)
        #space -o(1)
        if head is None or head.next is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next       # Move slow pointer one step
            fast = fast.next.next  # Move fast pointer two steps
            if slow == fast:   # If slow meets fast, cycle detected
                return True

        return False
