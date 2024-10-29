# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node acts as the starting point of the result list
        dummy = ListNode(0)
        curr = dummy  # Current pointer to build the result list
        carry = 0  # Initialize carry for addition
        
        # Iterate while there are nodes in l1 or l2, or there is a carry left
        while l1 != None or l2 != None:
            # Get the values of the current nodes of l1 and l2, or 0 if the node is None
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            
            # Calculate the sum of values and the carry
            val = val1 + val2 + carry
            carry = val // 10  # Update carry for the next step (quotient) of val is carry value
            val = val % 10  # Value for the current node is the (remainder) of val
            
            # Create a new node with the calculated value and move current pointer
            curr.next = ListNode(val)
            curr = curr.next
            
            # Move to the next nodes in l1 and l2 if they exist
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
        
        # After the loop, if there's a carry left, add a new node for it
        if carry > 0:
            curr.next = ListNode(carry)
        
        # Return the head of the resultant list
        return dummy.next