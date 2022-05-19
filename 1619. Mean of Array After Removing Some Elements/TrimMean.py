'''
https://leetcode.com/problems/mean-of-array-after-removing-some-elements/
'''

class Solution:
    def trimMean(self, arr):
        n = len(arr)
        arr.sort()
        ten_percent = int(n / 10)
        five_percent = int(n / 20)
        
        tot = sum(arr)
        
        for i in range(five_percent):
            tot -= arr[i]
            
        for i in range(n - 1, n - five_percent - 1, -1):
            tot -= arr[i]
            
        final_mean = tot / (n - ten_percent)
        return final_mean