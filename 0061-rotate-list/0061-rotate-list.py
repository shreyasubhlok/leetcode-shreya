# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time O(n)
    # space O(1)
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Check if the list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Calculate the length of the list and connect the tail to the head
        length = 1
        curr = head
        while curr.next is not None:
            curr = curr.next
            length += 1
        curr.next = head  # Form a circular list

        # Find the new head after k rotations
        k = length - (k % length)
        while k > 0:
            curr = curr.next
            k -= 1

        # Disconnect the circular list and set the new head
        newHead = curr.next
        curr.next = None
        return newHead

    def printList(self, head: ListNode):
        curr = head
        while curr is not None:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
