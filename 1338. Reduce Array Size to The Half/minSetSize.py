'''
https://leetcode.com/problems/reduce-array-size-to-the-half/
'''

from collections import Counter


class Solution:
    #today is truly problem solving day
    def minSetSize(self, arr) -> int:
        arr_count = Counter(arr)

        arr_count = sorted(arr_count.items(), key=lambda x: x[1], reverse=True)

        tot = 0
        num_of_set = 0

        for num in arr_count:
            if tot >= len(arr)/2:
                break
            tot += num[1]
            num_of_set += 1

        return num_of_set


sol = Solution()

print(sol.minSetSize( [9,77,63,22,92,9,14,54,8,38,18,19,38,68,58,19]))
    