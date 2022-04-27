class Solution:
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

sol = Solution()
print(sol.numRescueBoats([3,5,3,4], 5))