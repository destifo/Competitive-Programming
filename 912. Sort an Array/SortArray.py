class Solution:
    # wasn't accepted, 
    # O(nlogn) time,
    # O(1) space,
    # Approach: quick sort, divide and conquer
    def sortArray(self, nums: list[int]) -> list[int]:
        nums.append(float('inf'))
        def quickSort(l, r):
            if l < r:
                prev_pivot = partition(l, r)
                quickSort(l, prev_pivot)
                quickSort(prev_pivot, r)
                
        
        def partition(l, r):
            pivot = nums[l]
            i = l
            j = r
            while i < j:
                i +=1
                j -=1
                while nums[i] <= pivot:
                    i +=1
                while nums[j] > pivot:
                    j -=1
                    
                if i < j:
                    swap(i, j)
                    
            swap(l, j)
            
            return j
                    
        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
          
        quickSort(0, len(nums)-1)
        ans = nums
        
        return ans


    # O(nlogn) time,
    # O(n) space,
    # Approach: Merge sort, divide and conquer
    def sortArray2(self, nums: list[int]) -> list[int]:
        n = len(nums)
        return self.__mergeSort(0, n-1, nums)

    
    def __mergeSort(self, l:int, r:int, nums:list[int]) -> list[int]:
        if l < r:
            mid = l + (r-l) // 2
            left = self.__mergeSort(l, mid, nums)
            right = self.__mergeSort(mid+1, r, nums)
            return self.merge(left, right)
        else:
            return [nums[l]]


    def merge(self, nums1:list[int], nums2:list[int]) -> list[int]:
        merged = list()
        m, n = len(nums1), len(nums2)
        i, j = 0, 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i +=1
            else:
                merged.append(nums2[j])
                j +=1

        while i < m:
            merged.append(nums1[i])
            i +=1

        while j < n:
            merged.append(nums2[j])
            j +=1

        return merged


sol = Solution()
print(sol.sortArray([5,2,3,1]))