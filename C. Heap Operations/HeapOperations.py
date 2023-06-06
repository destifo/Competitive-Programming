

import heapq


def findTotalOperations(operations):
    tot_operations = []
    min_heap = []

    for operation in operations:
        op = operation.split()
        method = op[0]

        if method == 'insert':
            num = int(op[1])
            tot_operations.append(operation)
            heapq.heappush(min_heap, num)
        elif method == 'getMin':
            num = int(op[1])
            while len(min_heap) > 0 and min_heap[0] < num:
                tot_operations.append('removeMin')
                heapq.heappop(min_heap)
            if len(min_heap) == 0 or min_heap[0] > num:
                heapq.heappush(min_heap, num)
                st = 'insert ' + str(num)
                tot_operations.append(st)
            tot_operations.append(operation)
        elif method == 'removeMin':
            if not min_heap:
                st = 'insert ' + str(1)
                tot_operations.append(st)
            else:
                heapq.heappop(min_heap)
            tot_operations.append(method)

    return tot_operations


n = int(input())
operations = [0] * n

for i in range(n):
    operations[i] = input()


tot_ops = findTotalOperations(operations)
print(len(tot_ops))
for op in tot_ops:
    print(op)