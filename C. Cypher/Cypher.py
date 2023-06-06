
# O(len(moves)) time,
# O(1) space,
# Approach: iteration
def decypher(moves: str) -> int:
    tot_shift = 0
    for ch in moves:
        if ch == 'D':
            tot_shift +=1
        else:
            tot_shift -=1
    
    return tot_shift


t = int(input())
for i in range(t):
    n = int(input())
    final_pos = list(map(int, input().split()))
    for j in range(n):
        moves = input().split()
        final_pos[j] += decypher(moves[1])
        if final_pos[j] < 0:
            final_pos[j] = 10 + (final_pos[j] % 10)
        final_pos[j] %= 10
        
        final_pos[j] = str(final_pos[j])
        
    print(" ".join(final_pos))