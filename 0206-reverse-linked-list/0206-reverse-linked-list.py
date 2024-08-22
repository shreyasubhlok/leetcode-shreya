# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time is o(n) 
    #space is o(1) - using pointers like prev or current is o(1) 
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        prev = None
        '''
         In Python, when you pass an object (like head in this case) to a function, you're passing a reference to that object.
         Any  modifications made to the object inside the function will affect the original object outside the function. So use current
        '''
        current = head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev
