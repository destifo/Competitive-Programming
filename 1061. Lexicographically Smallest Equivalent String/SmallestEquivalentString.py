class Solution:
    
    def find(self, val1, parent):
        
        if val1 != parent[val1]:
            parent[val1] = self.find(parent[val1], parent)
            
        return parent[val1]
    
    def union(self, val1, val2, parent):
        
        if parent[val1] < parent[val2]:
            parent[parent[val2]] = parent[val1]
        else:
            parent[parent[val1]] = parent[val2]
    
    
    # O(len(s1) + len(baseStr)) time,
    # O(len(s1)) space, for call stack,
    # Approach: union find, 
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = [ i for i in range(26) ]
        
        for i in range(len(s1)):
            ch1 = s1[i]
            ch2 = s2[i]
            a_ascii = ord('a')
            val1 = ord(ch1)-a_ascii
            val2 = ord(ch2)-a_ascii
            if self.find(val1, parent) != self.find(val2, parent):
                self.union(val1, val2, parent)
                
        lexi_small = []
        for ch in baseStr:
            small_char = chr(self.find(ord(ch)-ord('a'), parent)+ord('a'))
            lexi_small.append(small_char)
            
        return "".join(lexi_small)