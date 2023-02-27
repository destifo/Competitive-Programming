from typing import List


class Solution:
    
    # O(nlogn) time,
    # O(n) space,
    # Approach: prefix sum, sorting, 
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        years = []
        
        for birth_year, death_year in logs:
            years.append(birth_year)
            years.append(death_year)
            
        years.sort()
        year_index = {}
        for index, year in enumerate(years):
            year_index[year] = index
        
        popn = [0 for _ in range(len(years))]
        for birth_year, death_year in logs:
            popn[year_index[birth_year]] += 1
            popn[year_index[death_year]] -= 1
        
        max_popn_year = years[0]
        max_popn = popn[0]
        for i in range(1, len(popn)):
            popn[i] += popn[i-1]
            if popn[i] > max_popn:
                max_popn_year = years[i]
                max_popn = popn[i]
                
        return max_popn_year