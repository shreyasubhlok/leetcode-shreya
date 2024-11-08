# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 1
        lenB = 1
        currA = headA
        currB = headB

        while currA != None:
            currA = currA.next
            lenA += 1

        while currB != None:
            currB = currB.next
            lenB += 1

        currA = headA
        currB = headB
        if lenA > lenB:
             for i in range(lenA-lenB):
                currA=currA.next
        else:
            for i in range(lenB-lenA):
                currB=currB.next
    
        
        while currA!=currB:
            currA=currA.next
            currB=currB.next
            
        return currA