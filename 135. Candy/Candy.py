'''
https://leetcode.com/problems/candy/
'''


from typing import List


class Solution:
    # O(nlogn) time,
    # O(n) space,
    # Approach: greedy, sorting, hashtable
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1 for i in range(n)]
        indices = {}
        
        def assignCandy(index: int) -> None:
            left = float('inf') if index == 0 else ratings[index-1]
            right = float('inf') if index == len(ratings)-1 else ratings[index+1]
            
            if ratings[index] <= left and ratings[index] <= right:
                return
            left_candy = 0 if left == float('inf') else candies[index-1]
            right_candy = 0 if right == float('inf') else candies[index+1]
            
            rating = ratings[index]
            if right == float('inf'):
                candies[index] = left_candy + 1
                return
            
            if left == float('inf'):
                candies[index] = right_candy + 1
                return
            
            if rating > left and rating > right:
                candies[index] = max(left_candy, right_candy) + 1
                return
            
            if left < right:
                candies[index] = left_candy + 1
                return
            if right < left:
                candies[index] = right_candy + 1
                return
            
        
        
        for i in range(n):
            rating = ratings[i]
            if rating not in indices.keys():
                indices[rating] = []
                
            indices[rating].append(i)
            
        srtd_ratings = sorted(ratings)
        
        i = 0
        while i < n and srtd_ratings[i] == srtd_ratings[0]:
            i +=1
            
        while i < n:
            rating = srtd_ratings[i]
            for index in indices[rating]:
                assignCandy(index)
            
            while i < n and srtd_ratings[i] == rating:
                i +=1
                
        # print(candies)
        return sum(candies)