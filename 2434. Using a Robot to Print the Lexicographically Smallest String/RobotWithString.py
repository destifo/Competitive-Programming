class Solution:
    
    def findSmallest(self, i, count):
        
        while i < 26 and count[i] == 0:
            i += 1
            
        return i
    
    # O(n) time,
    # O(n) space,
    # Approach: stack, greedy, 
    def robotWithString(self, s: str) -> str:
        count = [ 0 for _ in range(26) ]
        for ch in s:
            count[ord(ch)-ord('a')] += 1
        
        i = self.findSmallest(0, count)
        
        t = []
        ans = []
        for ch in s:
            count[ord(ch)-ord('a')] -= 1
            t.append(ch)
            if count[i] == 0:
                i = self.findSmallest(i, count)
            while t and (ord(t[-1])-ord('a')) <= i:
                ans.append(t.pop())
        
        return "".join(ans)