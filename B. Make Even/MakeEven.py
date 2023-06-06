

def findMinOperations(num:int) -> int:
    if int(num) % 2 == 0:
        return 0

    if int(num[0]) % 2 == 0:
        return 1

    for digit in num:
        digit = int(digit)
        if digit % 2 == 0:
            return 2
    
    return -1



inputs = input()
inputs = inputs.split()
t = int(inputs[0])
nums = [0] * t
for i in range(t):
    nums[i] = input()


for num in nums:
    print(findMinOperations(num))