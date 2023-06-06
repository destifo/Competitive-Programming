from collections import deque


class Solution:
    # O(n) time,
    # O(n) space,
    # Approach: BFS, deque, hashtable 
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        dominos = list(dominoes)
        qu = deque()
        
        
        for index, domino in enumerate(dominos):
            if domino == '.':   continue
            
            if domino == 'L':
                if index > 0 and dominos[index-1] == '.':
                    qu.append(index)
            
            if domino == 'R':
                if index < n-1 and dominos[index+1] == '.':
                    qu.append(index)
                    
        while qu:
            m = len(qu)
            changed = set()
            for i in range(m):
                index = qu.popleft()
                domino = dominos[index]
                
                if domino == 'R':
                    if index + 2 < n:
                        if dominos[index+2] == 'R' or dominos[index+2] == '.' or (index+2) in changed:
                            dominos[index + 1] = 'R'
                            changed.add(index+1)
                            if dominos[index+2] == '.':
                                qu.append(index+1)
                    else:
                        dominos[index + 1] = 'R'
                if domino == 'L':
                    if index - 2 > -1:
                        if dominos[index-2] == 'L' or dominos[index-2] == '.' or (index-2) in changed:
                            dominos[index - 1] = 'L'
                            changed.add(index-1)
                            if dominos[index-2] == '.':
                                qu.append(index-1)
                    else:
                        dominos[index - 1] = 'L'
                        
        return ''.join(dominos)

sol = Solution()
print(sol.pushDominoes(".L.R...LR..L.."))