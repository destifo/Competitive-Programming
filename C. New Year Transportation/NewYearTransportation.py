


def isPossible(portals, n, t):
    curr = 1
    while curr != n:
        nxt = curr + int(portals[curr-1])
        if nxt == t:
            print('YES')
            return
        curr = nxt

    print("NO")


n, t = input().split()
n, t = int(n), int(t)

portals = input().split()
isPossible(portals, n, t)