# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, t):
        
        # def findSuccessor(prev, curr):

        #     if curr.left:
        #         left_ans = findSuccessor(prev, curr.left)
        #         prev = left_ans[0]
        #         if prev == None:    return left_ans

        #     if prev == t:   return (None, curr.val)

        #     right_ans = float('-inf')
        #     if curr.right:
        #         right_ans = findSuccessor(curr.val, curr.right)
        #         if right_ans[0] == None:    return right_ans
            
        #     prev = right_ans[0] if right_ans != float('-inf') else curr.val
        #     return (prev, None)

        # return findSuccessor(float('inf'), root)[1]


        # def findSuccessor(curr, successor):
        #     if curr is None:    return successor

        #     if curr.val > t:
        #         return findSuccessor(curr.left, curr.val)
        #     else:   return findSuccessor(curr.right, successor)

        # return findSuccessor(root, float('inf'))

        successor = None
        while root:
            if root.val <= t:
                root = root.right
            else:
                successor = root.val
                root = root.left
        
        return successor