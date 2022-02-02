"""
https://codeforces.com/problemset/status?my=on
"""

def max_no_dominos_finder(board_size):
    board_size = board_size.split()
    area = int(board_size[0]) * int(board_size[1])
    return int(area/2)

board_size = input()
print(max_no_dominos_finder(board_size))
