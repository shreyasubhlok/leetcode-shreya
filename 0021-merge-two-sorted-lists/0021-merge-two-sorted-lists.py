# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # time complexity = o(n+m)=o(n)
    # space complexity = o(1) - dummy node creation just take o(1)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # Create a dummy node to simplify the code
        dummy = ListNode(-1)
        head = dummy

        # Traverse both lists and merge them
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next

        # Append remaining nodes of list1 or list2
        if list1 == None:
            head.next = list2

        if list2 == None:
            head.next = list1

        # Return the merged list starting from the next of dummy node
        return dummy.next