# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> [ListNode]:
        if lists == None or len(lists) == 0:
            return None

        # Loop until there's only one list remaining, which will be the fully merged list
        while len(lists) > 1:
            currMergedList = []  # Temporary list to store merged lists in each round

            # Iterate over the list of lists in pairs (step of 2)
            for i in range(0, len(lists), 2):
                l1 = lists[i]  # Odd-indexed list in the pair

                # Check if there is a second list (even-indexed) to pair with
                # If there's no list at even index (e.g., last single list in odd count), set l2 to None
                if (i + 1) < len(lists):
                    l2 = lists[i + 1]
                else:
                    l2 = None
                # Merge the two lists and add the result to currMergedList
                currMergedList.append(self.mergeTwoLists(l1, l2))
            # Update lists to the newly merged list to repeat merging process in the next round
            lists = currMergedList

        return lists[0]  # Return the only remaining list, which is the fully merged list

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
