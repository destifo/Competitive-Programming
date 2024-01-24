"""
https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/
"""


from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: dfs, hashtable
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        count = {}

        def isPseudoPali() -> bool:
            pas = 1

            for key, value in count.items():
                if value % 2 == 0:
                    continue
                if pas > 0:
                    pas -= 1
                    continue
                return False

            return True

        def countPseudoPali(root: Optional[TreeNode]) -> int:
            if not root.left and not root.right:
                count[root.val] = count.get(root.val, 0) + 1
                if isPseudoPali():
                    count[root.val] -= 1
                    return 1
                count[root.val] -= 1
                return 0

            count[root.val] = count.get(root.val, 0) + 1
            left = 0
            if root.left:
                left = countPseudoPali(root.left)

            right = 0
            if root.right:
                right = countPseudoPali(root.right)

            count[root.val] -= 1

            return left + right

        return countPseudoPali(root)

    # O(n) time,
    # O(h) space, h-> height of the tree
    # Approach: dfs, hashset
    def pseudoPalindromicPaths2(self, root: Optional[TreeNode]) -> int:
        nums = set()

        def isPseudoPali(val: int) -> bool:
            if val in nums:
                nums.remove(val)
                if len(nums) < 2:
                    nums.add(val)
                    return 1
                nums.add(val)
                return 0
            else:
                nums.add(val)
                if len(nums) < 2:
                    nums.remove(val)
                    return 1
                nums.remove(val)
                return 0

        def countPseudoPali(root: Optional[TreeNode]) -> int:
            val = root.val
            if not root.left and not root.right:
                if isPseudoPali(val):
                    return 1
                else:
                    return 0

            if val in nums:
                nums.remove(val)
            else:
                nums.add(val)
            left = 0
            if root.left:
                left = countPseudoPali(root.left)

            right = 0
            if root.right:
                right = countPseudoPali(root.right)

            if val in nums:
                nums.remove(val)
            else:
                nums.add(val)

            return left + right

        return countPseudoPali(root)

    def isPseudo(self, curr: List[int], nodes: int) -> bool:
        odds = nodes % 2

        for i in range(1, 10):
            if curr[i] % 2 == 1 and odds == 0:
                return False
            elif curr[i] % 2 == 1:
                odds -= 1

        return odds == 0

    def findTotalCount(
        self, node: Optional[TreeNode], nodes: int, curr: List[int]
    ) -> int:
        if not node:
            return 0

        tot = 0
        curr[node.val] += 1
        if not node.left and not node.right:
            if self.isPseudo(curr, nodes + 1):
                tot += 1

        tot += self.findTotalCount(node.left, nodes + 1, curr)
        tot += self.findTotalCount(node.right, nodes + 1, curr)
        curr[node.val] -= 1

        return tot

    # O(n) time, n -> nodes
    # O(h) space, h -> height of the tree
    # Approach: dfs, counting
    def pseudoPalindromicPaths3(self, root: Optional[TreeNode]) -> int:
        return self.findTotalCount(root, 0, [0 for _ in range(10)])
