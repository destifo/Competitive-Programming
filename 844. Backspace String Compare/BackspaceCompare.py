class Solution:
    # O(n) time, assuming n is the len of longest word
    # O(n) space,
    # Appoach: stack,
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def process(clipboard, ch):
            if ch == '#':
                if clipboard:
                    clipboard.pop()
            else:
                clipboard.append(ch)
        
        
        n = len(s)
        m = len(t)
        min_len = min(n, m)
        stack1 = []
        stack2 = []
        
        for i in range(min_len):
            process(stack1, s[i])
            process(stack2, t[i])
        
        i +=1
        
        if i < n: 
            while i < n:
                process(stack1, s[i])
                i +=1
                
        while i < m:
            process(stack2, t[i])
            i +=1
            
        return "".join(stack1) == "".join(stack2)