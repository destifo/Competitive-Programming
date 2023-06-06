"""
https://leetcode.com/problems/find-original-array-from-doubled-array/
"""

from collections import Counter
from typing import List


class Solution:
    def quickSort(self, array):
        self.__quickSort(array, 0, len(array) - 1)

    def __quickSort(self, array, start, end):
        if (start >= end):
            return
        boundary = self.partition(array, start, end)
        self.__quickSort(array, start, boundary - 1)
        self.__quickSort(array, boundary + 1, end)
        
    def partition(self, array, start, end):
        pivot = end
        boundary = start -1
        for i in range(start, end + 1):
            if array[i] < array[pivot]:
                boundary += 1
                self.swap(array, boundary, i)
        boundary += 1
        self.swap(array, boundary, pivot)
        return boundary


    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp 

    def mergeSort(self, array):
        if (len(array) < 2):
            return
        middleIndex = len(array)//2
        left = [0] * middleIndex
        right = [0] * (len(array) - middleIndex)
        for i in range(middleIndex):
            left[i] = array[i]
        for i in range(len(array) - middleIndex):
            right[i] = array[i + middleIndex]
        
        self.mergeSort(left)
        self.mergeSort(right)

        self.merge(left, right, array)
    
    def merge(self, left, right, result):
        i = 0
        j = 0
        k = 0
        while(i < len(left) and j < len(right)):
            if left[i] <= right[j]:
                result[k] = left[i]
                i +=1
                k +=1
            else:
                result[k] = right[j]
                k +=1
                j +=1
        while (i < len(left)):
            result[k] = left[i]
            i+=1
            k+=1
        while (j < len(right)):
            result[k] = right[j] 
            j +=1
            k +=1 
    def findOriginalArray(self, changed):
        changed_length = len(changed)
        unchanged = list()
        if len(changed)%2 != 0:
            return []
        odd_dict = dict()
        even_dict = dict()
        for num in changed:
            if num%2 != 0:
                if num not in odd_dict.keys():
                    odd_dict[num] = 1
                else:
                    odd_dict[num] +=1
            else:
                if num not in even_dict.keys():
                        even_dict[num] = 1
                else:
                    even_dict[num] +=1   
        try:
            if even_dict[0] %2 != 0:
                return []
        except:
            pass
        for key,value in odd_dict.items():
            if (2*key) not in even_dict.keys():
                return []
            else:
                unchanged.append(key)
                changed.remove(key)
                changed.remove(key*2)
        if (len(odd_dict) == changed_length/2):
            return list(odd_dict.keys())
        unmultiplied = dict()
        multiplied = dict()
        changed.sort()
        i = 0
        is_changed = True
        while (i < len(changed)):
            num = changed[i]
            if (num * 2) in changed:
                unchanged.append(num)
                changed.remove(num)
                changed.remove(num*2)
                i = 0
                continue
            is_changed = False
            break
        if is_changed == False:
            return []
        if len(changed) !=0:
            return []
        return unchanged
    

    def findOriginalArray2(self, changed):
        changed_length = len(changed)
        changed.sort()
        zero_count = 0
        for num in changed:
            if num != 0:
                break
            zero_count +=1
        if zero_count % 2 != 0:
            return []
        if zero_count == len(changed):
            return [0] * int(len(changed)/2)
        unchanged = list()
        i = 0
        is_changed = True
        while (i < len(changed)):
            num = changed[i]
            if (num * 2) in changed:
                unchanged.append(num)
                changed.pop(i)
                changed.remove(num*2)
                i = 0
                continue
            is_changed = False
            break
        if is_changed == False:
            return []
        if len(changed) !=0:
            return []
        
        return unchanged

    
    def findOriginalArray3(self, changed):
        changed_length = len(changed)
        unchanged = list()
        if len(changed)%2 != 0:
            return []
        odd_dict = dict()
        even_dict = dict()
        for num in changed:
            if num%2 != 0:
                if num not in odd_dict.keys():
                    odd_dict[num] = 1
                else:
                    odd_dict[num] +=1
            else:
                if num not in even_dict.keys():
                        even_dict[num] = 1
                else:
                    even_dict[num] +=1   
        try_case = 0
        try:
            if even_dict[0] %2 != 0:
                try_case = 1
            if even_dict[0] == len(changed):
                try_case = 2
        except:
            pass
        if try_case == 1:
            return []
        if try_case == 2:
            return [0] * int(len(changed)/2)
        for key in odd_dict.items():
            if (2*key) not in even_dict.keys():
                return []
            else:
                unchanged.append(key)
                changed.remove(key)
                changed.remove(key*2)
        if (len(odd_dict) == changed_length/2):
            return list(odd_dict.keys())
        unmultiplied = dict()
        multiplied = dict()
        self.quickSort(changed)
        i = 0
        is_changed = True
        while (i < len(changed)):
            num = changed[i]
            if (num * 2) in changed:
                unchanged.append(num)
                changed.remove(num)
                changed.remove(num*2)
                continue
            is_changed = False
            break
        if is_changed == False:
            return []
        if len(changed) !=0:
            return []
        return unchanged

    def findOriginalArray4(self, changed):#The working one
        changed_length = len(changed)
        if (changed_length % 2) != 0:
            return []

        unchanged = []
        count = Counter(changed)
        changed.sort() 
        
        for num in changed:
            if num == 0 and (count[num] % 2) != 0:
                return []

            if count[num] and count[num * 2]:
                count[num] -= 1
                count[num * 2] -= 1
                unchanged.append(num)
        
        if len(unchanged) == changed_length //2:
            return unchanged
        return []


    # O(nlogn) time,
    # O(n) space,
    # Approach: hashtable, sorting
    def findOriginalArray4(self, changed: List[int]) -> List[int]:
        count = Counter(changed)
        original = []
        
        changed.sort()
        
        for num in changed:
            if num == 0:
                if len(original) > 0:
                    continue
                elif count[num] % 2 != 0:
                    return []
                else:
                    original.extend([0 for i in range(count[0]//2)])
                    continue
                
            
            if count[num] > 0 and count.get(num*2, 0) > 0:
                count[num] -=1
                count[num*2] -=1
                original.append(num)
            elif count[num] <= 0:
                continue
            else:
                return []
            
        return original


sol = Solution()
print(sol.findOriginalArray4([2,1,2,4,2,4]))