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

    def totalFruit2(self, fruits):
        # checked this one from Nick White @YT, efficent in space and time
        last_fruit = -1
        second_last_fruit = -1
        last_fruit_count = 0
        current_max = 0
        max_fruit = 0

        for fruit in fruits:
            if fruit == last_fruit or fruit == second_last_fruit:
                current_max +=1
            else:
                current_max = last_fruit_count + 1

            if fruit == last_fruit:
                last_fruit_count +=1
            else:
                last_fruit_count = 1

            if fruit != last_fruit:
                second_last_fruit = last_fruit
                last_fruit = fruit

            max_fruit = max(max_fruit, current_max)

        return max_fruit


sol = Solution()
print(sol.totalFruit2([1,2,3,2,2]))