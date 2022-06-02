class Solution:
    def transpose(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        result = [[0] * m for i in range(n)]
        
        for i in range(m):
            for j in range(n):
                num = matrix[i][j]
                result[j][i] = num
                
        return result


sol = Solution()
print(sol.transpose([[1,2,3], [4,5,6]]))