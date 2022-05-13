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

                    