# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #time is o(n) and space is o(1)->in-place reversal approach
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
    
     #time is o(n) and space is also o(n) coz of extra array. So approach 1 in-place reversal           approach is better
    def isPalindromeAnotherApproach(self, head: ListNode) -> None:
        arr = []
        curr = head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        '''
        Slicing in Python: Syntex-> sequence[start:stop:step]
        [::-1] Explanation:
        arr[::-1] is a slice of the entire list arr, but with a step size of -1.
        The step size -1 means "start from the end and move backwards."
        As a result, arr[::-1] gives you the reversed version of the list arr.
        '''
        if arr == arr[::1]: #checks if the original list arr is the same as reversed list.
            return True
        else:
            return False

def PrintList(head: ListNode) -> None:
    curr = head
    while curr != None:
        print(curr.val, end="->")
        curr = curr.next
    print("None")