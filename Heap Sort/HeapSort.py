#User function Template for python3

class Solution:
    def get_parent_index(self, index:int):
        return (index-1)//2


    def get_left_child(self, index:list):
        return index*2 + 1


    def get_right_child(self, index:list):
        return index*2 + 2


    def swap(self, arr:list, index_one:int, index_two:int):
        temp = arr[index_one]
        arr[index_one] = arr[index_two]
        arr[index_two] = temp


    def pop(self, arr:list):
        if not arr: return
        temp = arr.pop()
        max_val = arr[0]
        arr[0] = temp
        self.heapify_down(arr)

        return max_val


    def heapify_down(self, arr):
        i = 0
        l = self.get_left_child(i)
        r = self.get_right_child(i)
        while (l < len(arr) and arr[i] < arr[l]) or (r < len(arr) and arr[i] < arr[r]):
            if arr[l] < arr[r]:
                self.swap(arr, i, l)
                i = l
                l = self.get_left_child(i)
                r = self.get_right_child(i)
            else:
                self.swap(arr, i, r)
                i = r
                l = self.get_left_child(i)
                r = self.get_right_child(i)


    
    def add(self, arr:list, val:int):
        arr.append(val)
        self.heapify_up(arr)

    
    def has_parent(index:int):
        return index > 0

    
    def heapify_up(self, arr:list):
        i = len(arr) - 1
        prnt = self.get_parent_index(i)
        while arr[i] > arr[prnt] and self.has_parent(i):
            self.swap(arr, i, prnt)
            i = prnt
            prnt = self.get_parent_index(i)

    
    def has_child(self, index:int, arr:list):
        return len(arr) > self.get_left_child(index)
    
    
    #Heapify function to maintain heap property.
    def heapify(self,arr:list, n:int, i:int):
        l = self.get_left_child(i)
        r = self.get_right_child(i)
        while (l < n and arr[i] < arr[l]) or (r < n and arr[i] < arr[r]):
            if r >=  n or arr[l] > arr[r]:
                self.swap(arr, i, l)
                i = l
                l = self.get_left_child(i)
                r = self.get_right_child(i)
            else:
                self.swap(arr, i, r)
                i = r
                l = self.get_left_child(i)
                r = self.get_right_child(i)
    
    #Function to build a Heap from array.
    def buildHeap(self,arr:list,n:int):
        for i in range(n-1, -1, -1):
            if self.has_child(i, arr):
                self.heapify(arr, n, i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr:list, n:int):
        self.buildHeap(arr, n)
        for i in range(len(arr)):
            self.swap(arr, 0, n-1)
            n-=1
            self.heapify(arr, n, 0)
        # print(arr)


sol = Solution()
sol.HeapSort([1, 4, 3, 2, 3, 7,5,6], 8)