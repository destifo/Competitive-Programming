'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


from collections import deque


class Solution:
    def connect(self, root):
        trvrsd = deque()
        def bfs(root):
            trvrsd.append(root)

            while trvrsd:
                n = len(trvrsd)
                if n > 1:
                    for i in range(n - 1):
                        curr_node = trvrsd[0]
                        curr_node.next = trvrsd[1]
                        if curr_node.left:
                            trvrsd.append(curr_node.left)
                        if curr_node.right:
                            trvrsd.append(curr_node.right)
                        trvrsd.popleft()
                    
                lastNodeOfDepth = trvrsd.popleft()
                if lastNodeOfDepth and lastNodeOfDepth.left:
                    trvrsd.append(lastNodeOfDepth.left)
                if lastNodeOfDepth and lastNodeOfDepth.right:
                    trvrsd.append(lastNodeOfDepth.right)

        bfs(root)
        return root

    
    # a simple, problem based solution done on a different occassion
    def connect2(self, root: 'Node') -> 'Node':
        qu = deque()
        qu.append(root)
        if not root:
            return root
        
        def bfs():
            while qu:
                n = len(qu)
                for i in range(n):
                    nod = qu.popleft()
                    if nod.left:
                        qu.append(nod.left)
                        qu.append(nod.right)
                    if i < n-1:
                        nod.next = qu[0]
                        
        bfs()
        return root