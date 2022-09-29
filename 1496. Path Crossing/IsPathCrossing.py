class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: hashtable, 
    def isPathCrossing(self, path: str) -> bool:
        vstd = set()
        curr_pos = [0, 0]
        vstd.add((curr_pos[0], curr_pos[1] ))
        
        for direc in path:
            if direc == 'N':
                curr_pos = curr_pos[0], curr_pos[1]+1
            if direc == 'S':
                curr_pos = curr_pos[0], curr_pos[1]-1
            if direc == 'E':
                curr_pos = curr_pos[0]+1, curr_pos[1]
            if direc == 'W':
                curr_pos = curr_pos[0]-1, curr_pos[1]
                
            if (curr_pos[0], curr_pos[1]) in vstd:
                return True
            
            vstd.add((curr_pos[0], curr_pos[1]))
            
        return False