class Solution:
    def rotate(self, nums, k: int):
        n = len(nums)
        if n < 2:
            return
        while k > 0:
            lastNum = nums.pop()
            nums.insert(0, lastNum)
            k -= 1
            
    def rotate2(self, nums, k):
        n = len(nums)
        if n < 2:
            return
        
        result = [0] * n
        for index, num in enumerate(nums):
            rotated_index = (index + k) % n
            result[rotated_index] = num
        
        for i in range(n - 1, -1, -1):
            nums[i] = result.pop()

    
    def rotate3(self, nums, k):
        n = len(nums)
        if n < 2:   return

        k = k % n
        self.reverse(0, n - 1, nums)
        self.reverse(0, k - 1, nums)
        self.reverse(k, n - 1, nums)


    def reverse(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            l +=1
            r -=1


    def rotate3(self, nums, k):
        n = len(nums)
        k = k % n
        if k == 0:  return nums
        rot_index = n - k
        
        def reverse(start, end):
            nums[start:end] = reversed(nums[start:end])
            
        reverse(0, rot_index)
        reverse(rot_index, n)
        nums.reverse()