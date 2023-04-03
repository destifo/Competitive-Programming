from typing import List


class Solution:
    # very space efficent
    def numRescueBoats(self, people, limit: int):
        if len(people) == 0:
            return 0
        people.sort()
        total_boats = 0
        j = len(people) - 1
        i = 0
        while i < j:
            while people and people[i] + people[j] > limit:
                if j <= i:
                    break
                j -=1

            if i >= j:
                break

            total_boats +=1
            people.pop(i)
            j -=1
            people.pop(j)
            j -=1

         
        total_boats += len(people)
        return total_boats
    
    # time efficent(kinda)
    def numRescueBoats2(self, people, limit) -> int:
        if len(people) == 0:
            return 0
        people.sort()
        total_boats = 0
        j = len(people) - 1
        i = 0
        while i <= j:
            if i == j:
                total_boats +=1
                return total_boats
            while people[i] + people[j] > limit:
                if j < i:
                    break
                j -=1
                total_boats +=1

            if i == j:
                total_boats +=1
                return total_boats
            if i >= j:
                break

            total_boats +=1
            i += 1
            j -= 1
         
        return total_boats
    

    # O(nlogn) time,
    # O(1) space,
    # Approach: two pointers, greedy, sorting
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people)-1
        boats = 0
        
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                right -= 1
                
            boats += 1
        
        return boats

sol = Solution()
print(sol.numRescueBoats([3,5,3,4], 5))