'''
https://leetcode.com/problems/spiral-matrix/
'''

class Solution:
    #did this one all by myself, I had to be brave and workout the algorithm on paper, but I have read the hints.
    #I just told myself that I need to do this and it worked out
    #felt so good when it got accepted
    def spiralOrder(self, matrix):
        m = len(matrix)
        n = len(matrix[0])
        tot_elts = m*n
        spiral = []
        count = 0

        r, c = 0, 0
        while count <= (tot_elts):
            for c in range(c, c+n):
                spiral.append(matrix[r][c])
                count +=1
            if count == tot_elts: return spiral
            r +=1
            m -=1
            for r in range(r, r+m):
                spiral.append(matrix[r][c])
                count +=1
            if count == tot_elts: return spiral
            n -=1
            c -=1
            for c in range(c, (c-n), -1):
                spiral.append(matrix[r][c])
                count +=1
            if count == tot_elts: return spiral
            r -=1
            m -=1
            for r in range(r, r-m, -1):
                spiral.append(matrix[r][c])
                count +=1
            if count == tot_elts: return spiral
            n -=1
            c +=1

        return spiral


sol = Solution()
print(sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))