# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def isPalindrome(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return head

        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverseList(slow)

        while head != None and slow != None :
            if head.val != slow.val:
                return False
            head = head.next
            slow = slow.next

        return True

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        curr = head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


def PrintList(head: ListNode) -> None:
    curr = head
    while curr != None:
        print(curr.val, end="->")
        curr = curr.next
    print("None")