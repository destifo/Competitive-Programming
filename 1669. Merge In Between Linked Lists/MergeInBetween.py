# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # O(n) time,
    # O(1) space,
    # Approach: linked list,
    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        dummy = ListNode(0, list1)
        prev, curr = dummy, list1

        index = 0
        while index < a:
            index += 1

            prev = curr
            curr = curr.next
        front_cut_point = prev

        while index <= b:
            index += 1

            prev = curr
            curr = curr.next
        rear_cut_point = curr
        prev.next = None

        # insert list2
        front_cut_point.next = list2
        curr = list2

        # get last node in list2
        while curr.next:
            curr = curr.next

        curr.next = rear_cut_point

        return dummy.next
