'''
https://leetcode.com/problems/max-number-of-k-sum-pairs/
'''

from collections import Counter


class Solution:
    def maxOperations(self, nums, k: int) -> int:
        nums_length = len(nums)
        nums.sort()

        #reversed_num = nums.reverse()
        #final_index = nums_length - nums.index(k) - 1

        nums_count = Counter(nums)
        max_ops = 0

        for i in range(1, k//2 + 1):
            if i == k - i:
                max_ops += nums_count[i] // 2
                continue
            max_ops += min(nums_count[i], nums_count[k - i])
        
        return max_ops
            
    def maxOperations2(self, nums, k: int) -> int:
        nums_count = [0]*k
        nums.sort()

        for num in nums:
            if num >= k:
                break
            nums_count[num] += 1

        max_ops = 0

        for i in range(1, k//2 + 1):
            if i == k - i:
                max_ops += nums_count[i] // 2
                continue
            max_ops += min(nums_count[i], nums_count[k - i])
        
        return max_ops

    def maxOperations3(self, nums, k: int) -> int:
        nums_count = Counter(nums)
        max_ops = 0

        for i in nums_count.keys():
            if i in nums_count.keys() and (k - i) in nums_count.keys():
                if i == k - i:
                    max_ops += nums_count[i] // 2
                    nums_count[i] = 0
                    continue
                max_ops += min(nums_count[i], nums_count[k - i])
                nums_count[i] = 0
                nums_count[k-i] = 0

        return max_ops

sol = Solution()
print(sol.maxOperations3([3,1,3,4,3], k = 6))



#maxOperations and maxOperations2 were my solutions, I think they were elegant but wasn't able to keep up with time :( but finally maxOperations3 worked out when only the hashmap is being iterated 