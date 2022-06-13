'''
https://practice.geeksforgeeks.org/problems/minimum-cost-of-ropes-1587115620/1
'''


import heapq


class Solution:
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self,arr,n) :
        
        # code here
        minHeap = []
        for elt in arr:
            heapq.heappush(minHeap, elt)
            
        min_cost = 0
        while len(minHeap) > 1:
            num1 = heapq.heappop(minHeap)
            num2 = heapq.heappop(minHeap)
            tot = num1 + num2
            min_cost +=tot
            heapq.heappush(minHeap, tot)
            
        return min_cost

    
    # slightly faster, we just hippified the arr rather creating a new one
    def minCost(self,arr,n) :
        
        # code here
        heapq.heapify(arr)
            
        min_cost = 0
        while len(arr) > 1:
            num1 = heapq.heappop(arr)
            num2 = heapq.heappop(arr)
            tot = num1 + num2
            min_cost +=tot
            heapq.heappush(arr, tot)
            
        return min_cost