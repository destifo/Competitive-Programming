class Solution:
    def merge(self, nums1:list, m: int, nums2, n: int):
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return

        def insertVal(val, index):
            nums1.insert(index, val)
            nums1.pop()
        
        i, j = 0, 0
        left_zeros = m
        while j < n:
            if nums1[i] >= nums2[j] or i >= left_zeros:
                insertVal(nums2[j], i)
                j +=1
                left_zeros +=1
            else:
                i +=1

        return


sol = Solution()
print(sol.merge([4,0,0,0,0,0],1,[1,2,3,5,6],5))       