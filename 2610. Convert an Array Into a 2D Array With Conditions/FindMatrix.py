from typing import Counter, List


class Solution:
    
    # O(n) time, n --> len(nums)
    # O(n) space,
    # Approach: counting, hash map, 
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        uniques = len(count.keys())
        
        depleted = set()
        ans = []
        
        while len(depleted) < uniques:
            curr = []
            for k in count.keys():
                if k in depleted:
                    continue
                curr.append(k)
                count[k] -= 1
                if count[k] == 0:
                    depleted.add(k)
            ans.append(curr)
            
        return ans