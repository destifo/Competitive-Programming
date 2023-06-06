from collections import Counter


class Solution:
    # O(n + m) time,
    # O(n + m + min_len) space
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        ans = []
        
        for key, value in count1.items():
            if key not in count2.keys():    continue
            min_occr = min(value, count2[key])
            for i in range(min_occr):
                ans.append(key)
                
        return ans

    
    # O(logn + logm) time,
    # O(min_len) space
    # approach: sorting, stack 
    def intersect2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n = len(nums1)
        m = len(nums2)
        ans = []
        
        nums1.sort()
        nums2.sort()
        
        while nums1 and nums2:
            if nums2[-1] == nums1[-1]:
                num = nums1[-1]
                ans.append(num)
                nums1.pop()
                nums2.pop()
            elif nums2[-1] > nums1[-1]:
                nums2.pop()
            else:
                nums1.pop()
                
        return ans