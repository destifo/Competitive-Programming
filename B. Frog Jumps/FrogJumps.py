

def findMinD(s: str) -> int:
    d = 1
    last_r = -1
    for i in range(len(s)):
        if s[i] == 'R':
            d = max(d, i-last_r)
            last_r = i
        
    d = max(d, len(s)-last_r)
    
    return d




t = int(input())
for i in range(t):
    s = input()
    print(findMinD(s))