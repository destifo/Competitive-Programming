# Definition for singly-linked list.
from numpy import double


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        nodesPos = {}
        curr = headA
        index = 0
        while curr:
            nodesPos[curr] = index
            index +=1
            curr = curr.next

        curr = headB
        index = 0
        intersectionNodes = []
        while curr:
            if curr in nodesPos.keys():
                intersectionNodes.append((curr, index + nodesPos[curr]))
            index+=1
            curr = curr.next
        
        if not intersectionNodes:   return None
        ans = None
        lowest = float('inf')
        for node in intersectionNodes:
            if node[1] < lowest:
                ans = node[0]
                lowest = node[1]

        return ans
            
    
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode):
        nodesInA = set()
        curr = headA
        while curr:
            nodesInA.add(curr)
            curr = curr.next

        curr = headB
        while curr:
            if curr in nodesInA:
                return curr
            curr = curr.next

        return None


    def getIntersectionNode2(self, headA: ListNode, headB: ListNode):
        a_len, b_len = 0, 0
        curr = headA
        while curr:
            a_len +=1
            curr = curr.next

        curr = headB
        while curr:
            b_len +=1
            curr = curr.next

        isALarger = a_len >= b_len
        iter_len = abs(a_len - b_len)

        if isALarger:
            for i in range(iter_len):
                headA = headA.next
        else:
            for i in range(iter_len):
                headB = headB.next

        while headA != headB:
            headA = headA.next
            headB = headB.next

        return headA