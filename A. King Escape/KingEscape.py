

n = int(input())
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))


x_up = max(bx, cx)
x_lo = min(bx, cx)
y_up = max(by, cy)
y_lo = min(by, cy)

if x_lo < ax and ax < x_up:
    print('no')
    quit()
    
if y_lo < ay and ay < y_up:
    print('no')
    quit()
    
print('yes')