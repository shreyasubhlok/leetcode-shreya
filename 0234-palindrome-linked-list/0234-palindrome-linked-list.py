# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time is o(n) and space is o(1)
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True  # Return True for empty or single-node list

        # Find the middle of the list
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half of the list
        slow = self.reverseList(slow)

        # Compare the first half with the reversed second half - palindrome logic check
        first_half = head
        second_half = slow
        while second_half != None:
            if first_half.val != second_half.val:
                return False
            first_half = first_half.next
            second_half = second_half.next

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