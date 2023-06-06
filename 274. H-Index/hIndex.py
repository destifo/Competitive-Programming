'''
https://leetcode.com/problems/h-index/
'''

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse = True)
        for index, citation in enumerate(citations):
            if index >= citation:
                return index

        return len(citations)

    def hIndex2(self, citations):
        n = len(citations)
        citations.sort()
        h_index = 0
        count = [0] * (citations[-1] + 1)

        for i in range(n):
            for j in range(i, citations[i] + 1):
                count[j + 1] = n - i
        
        for k in range(1, citations[-1] + 1):
            if k <= count[k]:
                h_index = k

        return h_index

    def hIndex2(self, citations):
        n = len(citations)
        if (n == 1 and citations[0] == 0):    return 0
        if (n == 1):    return 1
        citations.sort()
        h_index = 0
        
        try:
            while (citations[0] == 0):
                citations.pop(0)
        except:
            return 0
            
        n = len(citations)
        
        if (citations[0] > n):
            return n

        for i in range(n):
            if citations[i] <= n - i:
                h_index = citations[i]

        return h_index


sol = Solution()
print(sol.hIndex([1, 2, 3, 4, 5, 6]))