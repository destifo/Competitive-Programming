'''
https://leetcode.com/problems/sort-array-by-increasing-frequency/
'''


from collections import Counter


class Solution:
    def frequencySort(self, nums: list):
        nums_count = Counter(nums)
        nums_freq = {}
        
        for key, value in nums_count.items():
            nums = nums_freq.get(value, [])
            nums.append(key)
            nums_freq[value] = nums
        
        nums_freq = sorted(nums_freq.items(), key=lambda x:x[0])
        result = []
        for freq, nums in nums_freq:
            nums.sort(reverse=True)
            for num in nums:
                for i in range(freq):
                    result.append(num)
                
        return result
        