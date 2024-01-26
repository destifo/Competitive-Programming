class Node:
    
    def __init__(self, key=-1, val=-1, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = nxt


# Approach: double ended linked list
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = Node()
        self.tail = Node()
        self.head.next, self.tail.prev = self.tail, self.head
        self.size = 0
        
        
    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        
        curr = self.data[key]
        self.removeNode(curr)
        self.addNode(curr)
        
        return curr.val
    
    
    def addNode(self, curr: Node) -> None:
        curr.prev, curr.next = self.head, self.head.next
        curr.prev.next = curr
        if curr.next:
            curr.next.prev = curr
        
        
    def removeNode(self, curr: Node) -> None:
        curr.prev.next = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        curr.prev, curr.next = None, None
    

    def put(self, key: int, value: int) -> None:
        if key not in self.data:
            if self.capacity == self.size:
                self.data.pop(self.tail.prev.key)
                self.removeNode(self.tail.prev)
            else:
                self.size += 1
        else:
            self.removeNode(self.data[key])
        
        node = self.data[key] = Node(key, value)
        self.addNode(node)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)