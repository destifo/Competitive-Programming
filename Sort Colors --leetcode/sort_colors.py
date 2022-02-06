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
        
    def sortColors(self, nums):
        self.quickSort(nums)
        print(nums)
        

sol = Solution()
sol.sortColors([2,0,1])