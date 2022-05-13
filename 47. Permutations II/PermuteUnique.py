from collections import Counter


class Solution:
    def permuteUnique(self, nums):
        num_count = {}
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1
        ans = []
        permuts = []
        def findPermut():
            if len(permuts) == len(nums):
                ans.append(permuts[:])
                return
            
            for key in num_count:
                if num_count[key] > 0:
                    num_count[key] -=1
    
                    permuts.append(key)
                    findPermut()
                    num_count[key] +=1
                    permuts.pop()
            
        findPermut()
        
        return ans


sol = Solution()
print(sol.permuteUnique([1,1,2]))