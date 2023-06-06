
# O(n) time,
# O(n) space,
# Approach: hashtable,
def findTotBalloons(s: str) -> int:
    balloons = 0
    solved = set()
    
    for qustn in s:
        if qustn not in solved:
            solved.add(qustn)
            balloons += 2
        else:
            balloons +=1
            
    return balloons


t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    print(findTotBalloons(s))