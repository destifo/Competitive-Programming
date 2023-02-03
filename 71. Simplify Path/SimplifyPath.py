class Solution:
    
    def split(self, s: str):
        
        elts = []
        curr_dir = ""
        
        for dirc in s:
            if not curr_dir and dirc == "/":
                continue
                
            if dirc == "/":
                elts.append(curr_dir)
                curr_dir = ""
            else:
                curr_dir += dirc
        
        if curr_dir:
            elts.append(curr_dir)
        
        return elts
    
    
    # O(n) time,
    # O(n) space,
    # Approach: slack, implementation, string
    def simplifyPath(self, path: str) -> str:
        splitted_path = self.split(path)

        stack = []
        for dirc in splitted_path:
            
            if dirc == "..":
                if stack:
                    stack.pop()
            elif dirc != ".":
                stack.append(dirc)
            
        canonical_path = "/" + "/".join(stack)
        
        return canonical_path