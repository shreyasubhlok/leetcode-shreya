# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time o(n) and space o(1) (better thn recursion coz recursion uses o(n) space and time is o(n))
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        '''
         In Python, when you pass an object (like head in this case) to a function, you're passing a reference          to that object. Any modifications made to the object inside the function will affect the original              object outside the function. So use current
        '''
        curr=head
        while curr!=None:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        return prev
        
            