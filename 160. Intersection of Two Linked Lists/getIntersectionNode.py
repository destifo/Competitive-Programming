# Definition for singly-linked list.
from typing import Optional
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


    def getIntersectionNode3(self, headA: ListNode, headB: ListNode):
        # an O(1) space solution
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

    
    def getIntersectionNode4(self, headA: ListNode, headB: ListNode):
        # an O(m + n) time and O(1) space solution
        # the intution is that the shorter one will rollback to head of the longer
        # linked list and the larger one the vice versa 
        currA, currB = headA, headB
        while currA != currB:
            currA = currA.next if currA else headB
            currB = currB.next if currB else headA
            
        return currA

    
    # O(m+n) time,
    # O(1) space,
    # Approach: linked list, array, 
    def getIntersectionNode5(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        a_len, b_len = self.getLen(headA), self.getLen(headB)
        diff = abs(a_len-b_len)
        
        longer, shorter = (headA, headB) if a_len >= b_len else (headB, headA)
        
        curr_long = longer
        curr_short = shorter
        
        while diff:
            curr_long = curr_long.next
            diff -= 1
        
        while curr_long != curr_short:
            curr_long = curr_long.next
            curr_short = curr_short.next
        
        return curr_long