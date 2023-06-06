'''
https://leetcode.com/problems/stamping-the-sequence/solution/
'''


from typing import List


class Solution:
    # O(n(n-m) * m) time,
    # O(n-m) space,
    # Approach: sliding window, 
    def movesToStamp(self, stamp: str, target: str) -> List[int]:
        n = len(target)
        m = len(stamp)
        target = list(target)
        ans = []
        vstd_indexes = set()
        
        
        def isStamped(subarray):
            for index,ch in enumerate(subarray):
                if not (ch == '?' or ch == stamp[index]):
                    return False
                
            return True
        
        
        def replaceToPlaceholder(start):
            non_questionmark = 0
            for i in range(m):
                if target[start+i] != '?':
                    non_questionmark += 1
                    target[start+i] = '?'
                
            return non_questionmark
        
        
        reversed = 0
        l, r = 0, m
        stampExists = False
        
        while reversed != n:
            while r <= n:
                if l not in vstd_indexes and isStamped(target[l:r]):
                    stampExists = True
                    ans.append(l)
                    vstd_indexes.add(l)
                    break
                l +=1
                r +=1
            if stampExists:
                reversed +=replaceToPlaceholder(ans[-1])
                stampExists = False
                l, r = 0, m
            else:
                return []
            
        ans.reverse()
        return ans