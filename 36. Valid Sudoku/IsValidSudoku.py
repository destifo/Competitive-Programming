'''
https://leetcode.com/problems/valid-sudoku/
'''

class Solution:
    def isValidSudoku(self, board):
        row_nums, col_nums = [set() for i in range(9)], [set() for i in range(9)]
        sub_box = {}
        for row in range(9):
            for col in range(9):
                curr_num = board[row][col]
                if curr_num == ".": continue
                if curr_num in row_nums[row] or curr_num in col_nums[col]:    return False
                row_nums[row].add(curr_num)
                col_nums[col].add(curr_num)

                key = (row//3, col//3)
                sub_box_nums = sub_box.get(key, {})
                if curr_num in sub_box_nums:    return False
                sub_box_nums.add(curr_num)
                sub_box[key] = sub_box_nums

        return True


sol = Solution()
print(sol.isValidSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))  