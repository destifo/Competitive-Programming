from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # O(nlogn) time,
    # O(nlogn) space,
    # Approach: dfs, backtracking, hashtable, binary tree, graph,
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.s = None
        self.t = None
        parentOf = {}
        parentOf[root.val] = None
        vstd = set()
        
        def buildGraph(root: Optional[TreeNode]) -> None:
            
            left = root.left
            right = root.right
            
            if root.val == startValue:  self.s = root
            if root.val == destValue:   self.t = root
            
            if left:
                parentOf[left.val] = root
                buildGraph(left)
                
            if right:
                parentOf[right.val] = root
                buildGraph(right)
                
        def dfs(root: Optional[TreeNode], direction: List[str]) -> str:
            if root in vstd:    return
            
            left = root.left
            right = root.right
            parent = parentOf[root.val]
            vstd.add(root.val)
            
            if root.val == self.t.val:
                ans = ''.join(direction)
                return ans
            
            found = False
            ans = ''
            
            if left and left.val not in vstd:
                direction.append('L')
                ans = dfs(left, direction)
                if ans != '':
                    found = True
                direction.pop()
                
            if found:   return ans
                
            if right and right.val not in vstd:
                direction.append('R')
                ans = dfs(right, direction)
                if ans != '':
                    found = True
                direction.pop()
                
            if found:   return ans
                
            if parent and parent.val not in vstd:
                direction.append('U')
                ans = dfs(parent, direction)
                if ans != '':
                    found = True
                direction.pop()
            
            if found:   return ans
            
            return ''
        
        buildGraph(root)
        return dfs(self.s, [])

    
    # O(nlogn) time,
    # O(nlogn) space,
    # Approach: dfs, backtracking, binary tree
    def getDirections2(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def findPath(root, path):
            
            if root.val == startValue:
                # print('yes')
                self.start_path = path[::]
            
            if root.val == destValue:
                self.dest_path = path[::]
            
            
            left = root.left
            right = root.right
            
            if left:
                path.append('L')
                findPath(left, path)
                path.pop()
                
            if right:
                path.append('R')
                findPath(right, path)
                path.pop()
                
        findPath(root, [])
        
        i = 0
        min_len = min(len(self.start_path), len(self.dest_path))
        while i < min_len and self.start_path[i] == self.dest_path[i]:
            i +=1
        
        leftside_path = (len(self.start_path)-i) * 'U'
        rightside_path = ''.join(self.dest_path[i:])
        
        return (leftside_path + rightside_path)