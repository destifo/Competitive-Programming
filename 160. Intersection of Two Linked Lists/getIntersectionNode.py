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
            