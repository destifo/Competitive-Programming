'''
https://leetcode.com/problems/arithmetic-subarrays/submissions/
'''

from typing import List


class Solution:
    def checkArithmeticSubarrays(self, nums, l, r):#worked the first time, :)
        answer = []
        query_range = len(l)

        for i in range(query_range):
            current_array = nums[l[i]:r[i] + 1]
            current_array.sort()
            current_arr_length = len(current_array)
            isArithmetic = True
            difference = current_array[1] - current_array[0]

            for i in range(1, current_arr_length):
                if current_array[i] - current_array[i - 1] != difference:
                    isArithmetic = False
                    break
            
            answer.append(isArithmetic)
        
        return answer
    
    
    # O(m*nlogn) time,
    # O(m*n) space,
    # Approach: sorting, 
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        
        for i in range(len(r)):
            left, right = l[i], r[i]
            
            is_arthimetic = True
            s_nums = sorted(nums[left:right+1])
            diff = 0 if len(s_nums) <= 1 else s_nums[1]-s_nums[0]
            for j in range(1, len(s_nums)):
                if (s_nums[j]-s_nums[j-1]) != diff:
                    is_arthimetic = False
                    break
            
            ans.append(is_arthimetic)
            
        return ans

    

sol = Solution()

print(sol.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))