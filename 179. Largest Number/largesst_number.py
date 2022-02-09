"""
https://leetcode.com/problems/largest-number/
"""

class Solution:

    def compare(self, first, second):#where hyped about this comopare algorithm but in the end, didn't work out :(   didn't delete cause I thought it was/is beautiful
        first = str(first)
        second = str(second)
        if (first[0] > second[0]):
            return 1
        elif (first[0] < second[0]):
            return 0
        else:
            try:
                return self.compare(first[1:], second[1:])
            except:
                big_digit_num = None
                if (len(first) > len(second)):
                    big_digit_num = first
                elif(len(first) < len(second)):
                    big_digit_num = second
                else:
                    return 1
                if (big_digit_num == first):
                    if(first[1] < second[0]):
                        return 0
                    else:
                        return 1
                if (big_digit_num == second):
                    if(second[1] < first[0]):
                        return 1
                    else:
                        return 0


    def compare2(self, first, second):#I felt silly when I thought about this one, as it is really simple, but I felt compare was like good but then this worked out rather than compare... then everything was easy after this was revealed for me
        first = str(first)
        second = str(second)
        mesh1 = int(first + second)
        mesh2 = int(second + first)

        if (mesh1 > mesh2):
            return int(first)
        else:
            return int(second)


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
            if (self.compare2(left[i], right[j]) == left[i]):
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
                
    def largestNumber(self, nums):
        self.mergeSort(nums)
        largest_number = ""
        for i in range(len(nums)):
            largest_number += str(nums[i])
        if (int(largest_number) == 0):
            return "0"
        return largest_number




sol = Solution()
print(sol.largestNumber([0, 0]))
        
    