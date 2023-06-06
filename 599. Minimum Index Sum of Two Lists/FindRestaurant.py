'''
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
'''

class Solution:
    def findRestaurant(self, list1, list2):
        map1 = {}
        for i, val in enumerate(list1):
            map1[val] = i
            
        map2 = {}
        for i, val in enumerate(list2):
            if val in map1.keys():
                map2[val] = i

        common_list = []
        for key,val in map2.items():
            rest_tot_index = (map1[key] + map2[key], key)
            common_list.append(rest_tot_index)

        common_list.sort(key=lambda x:x[0])
        result = []
        least_tot = common_list[0][0]
        for rest in common_list:
            if rest[0] != least_tot:
                return result
            result.append(rest[1])
        
        return result
                