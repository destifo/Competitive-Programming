from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        tot = 0
        self.prefix_sum = [0]
        
        for num in nums:
            tot += num
            self.prefix_sum.append(tot)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)