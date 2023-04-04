class Solution:
    
    # O(n) time,
    # O(n) space,
    # Approach: greedy, hashtable, 
    def partitionString(self, s: str) -> int:
        seen = set()
        partitions = 1
        
        for ch in s:
            if ch in seen:
                partitions += 1
                seen = set()
            seen.add(ch)
            
        return partitions