# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        while l1 != None or l2 != None:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0

            val = val1 + val2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            curr=curr.next
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            
        if carry>0:
            curr.next=ListNode(carry)
            
        return dummy.next
