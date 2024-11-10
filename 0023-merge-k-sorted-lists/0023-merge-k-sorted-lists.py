# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if list==None or len(lists)==0:
            return None
        
        while len(lists)>1:
            currMergedList=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                currMergedList.append(self.mergeTwoList(l1,l2))
            lists=currMergedList
        
        return lists[0]
    
    def mergeTwoList(self, l1:ListNode, l2:ListNode)->ListNode:
        dummy=ListNode(-1)
        head=dummy
        
        while l1!=None and l2!=None:
            if l1.val<l2.val:
                head.next=l1
                l1=l1.next
            else:
                head.next=l2
                l2=l2.next
            head=head.next
            
        if l1==None:
            head.next=l2
            
        if l2==None:
            head.next=l1
            
        return dummy.next