'''
https://leetcode.com/problems/number-of-provinces/
'''


from typing import List


class Solution:
    # O(n^2) time,
    # O(n) space,
    # Approach: DFS, hashset
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        unexplored = set([i for i in range(1, n+1)])
        
        
        def findNeighbours(root):
            row = isConnected[root-1]
            neighbours = []
            for i in range(n):
                if i == root-1:    continue
                if row[i] == 1 and (i+1) in unexplored:
                    neighbours.append(i+1)
                    
            return neighbours
        
        
        def searchConnected(root):
            if root not in unexplored:
                return
            unexplored.remove(root)
            neighbours = findNeighbours(root)
            
            if len(neighbours) == 0:    return
            
            for neighbour in neighbours:
                searchConnected(neighbour)
        
        provinces = 0
        while unexplored:
            provinces +=1
            for city in unexplored:
                break  
            searchConnected(city)
            
        return provinces