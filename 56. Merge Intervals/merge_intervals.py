"""
https://leetcode.com/problems/merge-intervals/
"""


class Solution:
    def merge(self, intervals):
        self.quickSort(intervals)

        merged_list = list()
        i = 0
        j = 1
        isDone = True
        while (i < len(intervals)):
            if (j >= len(intervals)):
                merged_list.append(intervals[i])
                i +=1
                continue
            if (intervals[i][1] >= intervals[j][0]):
                if (intervals[i][1] >= intervals[j][1]):
                    merged_list.append([intervals[i][0], intervals[i][1]])
                if (intervals[j][1] > intervals[i][1]):
                    merged_list.append([intervals[i][0], intervals[j][1]])
                i +=2
                j +=2
                isDone = False
            else:
                merged_list.append(intervals[i])
                i +=1
                j +=1
        if isDone:
            return merged_list
        else:
            return self.merge(merged_list)

    
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
            if array[i][0] < array[pivot][0]:
                boundary += 1
                self.swap(array, boundary, i)
        boundary += 1
        self.swap(array, boundary, pivot)
        return boundary


    def swap(self, array, first, second):
        temp = array[first]
        array[first] = array[second]
        array[second] = temp
        

sol = Solution()
print(sol.merge([[1,4],[1,5]]))
        
        