class Solution:
    def maxArea(self, height):
        #with some help able to solve it
        n = len(height)
        j = n - 1
        i = 0
        max_area = j * min(height[i], height[j])

        while j - i > 0:
            if height[i] < height[j]:   i +=1
            else:   j -=1

            current_area = (j - i) * min(height[i], height[j])
            max_area = max(current_area, max_area)
        
        return max_area


sol = Solution()
print(sol.maxArea(height = [1,8,6,2,5,4,8,3,7]))