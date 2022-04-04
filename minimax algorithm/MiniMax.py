

finalScore = 0
def minimax(position, depth, player):
    if depth == 0:
        return finalScore

    maximizingPlayer = player
    if maximizingPlayer:
        maxEval = float('-inf')
        for child in position.moves:
            maxEval = max(maxEval, minimax(child, depth - 1, False))
    else:
        minEval = float('inf')
        for child in position.moves:
            minEval = min(minEval, minimax(child, depth - 1, True))