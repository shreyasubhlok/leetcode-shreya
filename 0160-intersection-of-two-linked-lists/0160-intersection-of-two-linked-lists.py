# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        myset=set()
        curr=headA
        while curr!=None:
            myset.add(curr)
            curr=curr.next
            
      
        
        newCurr=headB
        while newCurr!=None:
            if newCurr in myset:
                return newCurr
            newCurr=newCurr.next
        
        return None