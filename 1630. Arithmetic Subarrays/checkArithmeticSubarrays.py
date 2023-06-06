'''
https://leetcode.com/problems/arithmetic-subarrays/submissions/
'''

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

    

sol = Solution()

print(sol.checkArithmeticSubarrays(nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]))