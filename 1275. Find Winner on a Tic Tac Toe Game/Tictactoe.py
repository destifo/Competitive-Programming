'''
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
'''


class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        grid = [[ (i + 3*j) for i in range(3) ] for j in range(3)]
        
        def check_row_win():
            for row in range(3):
                if grid[row][0] == grid[row][1] and grid[row][1] == grid[row][2]:
                    return grid[row][0]
                
            return "0"
        
        def check_col_win():
            for col in range(3):
                if grid[0][col] == grid[1][col] and grid[1][col] == grid[2][col]:
                    return grid[0][col]
                
            return "0"
        
        def check_diagonal_win():
            if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
                return grid[0][0]
            
            if grid[0][2] == grid[1][1] and grid[1][1] == grid[2][0]:
                return grid[1][1]
            
            return "0"
        
        for index,move in enumerate(moves):
            ch = 'A' if index % 2 == 0 else 'B'
            x, y = move
            grid[x][y] = ch
            
        winner = check_col_win()
        if winner.isalpha():
            return winner
        
        winner = check_row_win()
        if winner.isalpha():
            return winner
        
        winner = check_diagonal_win()
        if winner.isalpha():
            return winner
        
        # for row in grid:
        #     print(row)
        return "Pending" if len(moves) < 9 else "Draw"