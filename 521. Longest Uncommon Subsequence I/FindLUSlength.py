class Solution:
    
    # O(n) time, takes linear time for comparing strings
    # O(1) space,
    # Approach: string, brain teaser
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1