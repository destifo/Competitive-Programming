

def locateRooms(rooms, letters):
    room_prefix = calcPrefixSum(rooms)
    for letter in letters:
        letter = int(letter)
        dorm = findDorm(0, len(rooms)-1, letter, room_prefix)
        if dorm != 0:
            letter -= room_prefix[dorm-1]
        print(dorm+1, letter)


def calcPrefixSum(nums):
    n = len(nums)
    room_prefix = [0] * n
    tot = 0
    for i in range(n):
        tot += int(nums[i])
        room_prefix[i] = tot
        
    return room_prefix



def findDorm(lo, hi, num, prefix_sum):
    ans = lo
    while lo <= hi:
        mid = (lo+hi)//2
        
        if prefix_sum[mid] >= num and (mid== 0 or prefix_sum[mid-1] < num):
            return mid
        
        elif prefix_sum[mid] < num:
            lo = mid+1

        else:
            hi = mid-1



n, m = input().split()
n = int(n)
rooms = input().split()
letters = input().split()
locateRooms(rooms, letters)