# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head
        
        curr=head
        length=1
        while curr.next!=None:
            curr=curr.next
            length=length+1
        curr.next=head
        
        k=k%length
        k=length-k
        print(k)
        
        while k>0:
            curr=curr.next
            k=k-1
        print(curr.val)
        newHead=curr.next
        curr.next=None
        return newHead