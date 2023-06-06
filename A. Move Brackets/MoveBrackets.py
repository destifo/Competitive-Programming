

def findMinMoves(s: str) -> int:
    stack = []

    for brak in s:
        if brak == '(':
            stack.append(brak)
        else:
            if not stack:
                continue
            stack.pop()
    
    # if stack:
    #     return False
    
    return len(stack)


# def moveFirstToLast(s: str) -> str:
#     s_lst = list(s)
#     letter = s_lst.pop(0)
#     s_lst.append(letter)

#     return ''.join(s_lst)


# def findMinMoves(s: str) -> int:
#     moves = 0

#     while True:
#         if isValid(s):  return moves
#         s = moveFirstToLast(s)
#         moves +=1



t = int(input())
for i in range(t):
    n = int(input())
    braks = input()
    print(findMinMoves(braks))