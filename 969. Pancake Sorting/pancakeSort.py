'''
https://leetcode.com/problems/pancake-sorting/
'''

class Solution:
    #at first I thought it was difficult but then the core idea basically a bubble sort variation, just bubble out the largest values to the last index, takes 1 or 2 flips per value, and need not be concerned with the the 1st value
    def pancakeSort(self, arr):
        arr_len = len(arr)

        isSorted = True
        for i in range(1, arr_len):
            if arr[i] < arr[i -1]:
                isSorted = False
        
        if isSorted:
            return []

        result = []
        sorted_arr = arr.copy()
        sorted_arr.sort()

        for i in range(arr_len - 1, 0, -1):
            current_index = arr.index(sorted_arr[i]) 
            if current_index == i:
                continue
            if current_index != 0:
                self.flip(arr, current_index + 1)
                result.append(current_index + 1)
            self.flip(arr, i + 1)
            result.append(i + 1)
        
        return result

    
    def flip(self, arr, k):
        flipped = arr[:k]
        flipped.reverse()
        arr[:k] = flipped
    



sol = Solution()
arr = [1,2,3]
print(sol.pancakeSort(arr))
