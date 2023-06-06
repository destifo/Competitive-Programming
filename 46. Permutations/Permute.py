class Solution:
    def permute(self, nums):        
        def findPermut(curr):
            ans = []
            if len(curr) == 1:
                return [curr.copy()]
            
            for i in range(len(curr)):
                num = nums.pop(0)
                permuts = findPermut(nums)
                nums.append(num)

                for permt in permuts:
                    permt.append(num)

                ans.extend(permuts)
            
        return findPermut(nums)