"""
https://leetcode.com/problems/k-closest-points-to-origin/
"""
import math
import time
start_time = time.time()

class Solution:

    def insertionSort(self, array):#used insertion sort and time limit exceeded 72/87 tests passed
        for i in range(len(array)):
            current = array[i]
            j = i - 1
            while ( j >= 0 and self.distanceFromOrigin(array[j]) > self.distanceFromOrigin(current)):
                array[j + 1] = array[j]
                j -=1
            array[j + 1] = current

    def distanceFromOrigin(self, point):
        x_squared = point[0] ** 2 
        y_squared = point[1] ** 2
        return math.sqrt( x_squared + y_squared )

    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp


    #used quick sort and time limit exceeded and 85/87 tests passed, 2 fails
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
            if self.distanceFromOrigin(array[i]) < self.distanceFromOrigin(array[pivot]):
                boundary += 1
                self.swap(array, boundary, i)
        boundary += 1
        self.swap(array, boundary, pivot)
        return boundary


    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp

    #finally mergeSort worked, turns out it's faster than quick sort, comes with a space cost
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
            if (self.distanceFromOrigin(left[i]) <= self.distanceFromOrigin(right[j])):
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


    def kClosest(self, points, k: int):
        self.mergeSort(points)
        return points[:k]

sol = Solution()
print(sol.kClosest([[6,10],[-3,3],[-2,5],[0,2]], 3))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
            