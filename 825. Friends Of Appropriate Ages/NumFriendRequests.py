'''
https://leetcode.com/problems/friends-of-appropriate-ages/
'''


from collections import Counter


class Solution:
    # had to sweat for it, ngl
    def numFriendRequests(self, ages: list[int]) -> int:
        n = len(ages)
        ages.sort()
        tot_req = 0
        age_count = Counter(ages)
        for age, count in age_count.items():
            if count == 1 or age <= (0.5*age) + 7:  continue
            count -=1
            temp = (count*count) + count
            tot_req +=temp
        
        ages = list(age_count.keys())
        n = len(ages)
        for x in range(n-1, 0, -1):
            age = ages[x]
            lower_interval = (0.5*age) + 7

            for y in range(x-1, -1, -1):
                age_y = ages[y]
                if age_y <= lower_interval:
                    break
                if age == age_y:    continue
                tot_req +=age_count[age_y]*(age_count[age])
        
        return tot_req


sol = Solution()
print(sol.numFriendRequests([8,85,24,85,69]))