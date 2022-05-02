'''
https://leetcode.com/problems/fruit-into-baskets/
'''

class Solution:
    # I guess this is space efficent.
    def totalFruit(self, fruits):
        n = len(fruits)
        l, r = 0, 0
        max_num_fruits = 0
        fruit_map = { fruits[0]: 1}

        for r in range(1, n):
            fruit = fruits[r]
            fruit_map[fruit] = fruit_map.get(fruit, 0) + 1
            while len(fruit_map) > 2:
                fruit = fruits[l]
                if fruit_map[fruit] == 1:
                    fruit_map.pop(fruit)
                else:
                    fruit_map[fruit] = fruit_map.get(fruit) - 1
                l +=1
            
            max_num_fruits = max(max_num_fruits, r - l + 1)

        max_num_fruits = max(max_num_fruits, r - l + 1)

        return max_num_fruits


sol = Solution()
print(sol.totalFruit([1,2,1]))