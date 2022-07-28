'''
https://leetcode.com/problems/most-frequent-subtree-sum/
'''


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    # O(n) time,
    # O(n + m) space,
    # Approach: DFS, hashmap
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> list[int]:
        sum_count = {}
        max_freq = [0]
        
        def dfs(root, prev_score):
            if root == None:
                if prev_score != 0:
                    sum_count[prev_score] = sum_count.get(prev_score, 0) + 1
                    max_freq[0] = max(max_freq[0], sum_count[prev_score])
                return prev_score
            
            left = root.left
            left_val = 0
            if left:
                left_val = left.val
                
            right = root.right
            right_val = 0
            if right:
                right_val = right.val
                
            children_val = dfs(left, left_val) + dfs(right, right_val)
            tot = children_val + root.val
            sum_count[tot] = sum_count.get(tot, 0) + 1
            max_freq[0] = max(max_freq[0], sum_count[tot])
            
            return tot
        
        dfs(root, root.val)
        
#         freq = 0
        
#         for key, value in sum_count.items():
#             freq = max(freq, value)
            
        result = []
        
        for key, value in sum_count.items():
            if value == max_freq[0]:
                result.append(key)
                
        return result