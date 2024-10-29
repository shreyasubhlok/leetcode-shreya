# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Time is o(n) and space is o(1)
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Dummy node is used to simplify edge cases, such as removing the first node
        dummy = ListNode(0)
        dummy.next = head  # Link dummy node to the head of the list

        first = dummy  # Pointer to find the end of the list
        second = dummy  # Pointer to find the (N+1)-th last node

        # Move the 'first' pointer n+1 steps ahead to maintain a gap of 'n' nodes
        for i in range(n + 1):
            first = first.next  # Advance 'first' by 1 step each time

        # Move both pointers until 'first' reaches the end
        # At this point, 'second' will be just before the target node, gap between first and second will remain same--technique
        while first != None:
            first = first.next  # Move 'first' to the end of the list
            second = second.next  # Move 'second' in sync with 'first'

        # Skip the node that is nth from the end
        second.next = second.next.next

        # Return the modified list, starting from the original head
        return dummy.next
