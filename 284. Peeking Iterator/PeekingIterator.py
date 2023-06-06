# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

# O(len(iterator)) time,
# O(1) space,
# Approach: design, array
class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.iterator = iterator
        self.nxt = -1
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
        

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nxt
        
        

    def next(self):
        """
        :rtype: int
        """
        temp_next = self.nxt
        if self.iterator.hasNext():
            self.nxt = self.iterator.next()
        else:
            self.nxt = -1
            
        return temp_next
        

    def hasNext(self):
        """
        :rtype: bool
        """
        
        return self.nxt != -1
        

# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].