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
            diff = lenA - lenB
            while diff != 0:
                currA = currA.next
                diff -= 1
        else:
            diff = lenB - lenA
            while diff != 0:
                currB = currB.next
                diff -= 1
        
        while currA!=currB:
            currA=currA.next
            currB=currB.next
            
        return currA