# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

from typing import List


class NestedIterator:
    def __init__(self, nestedList: List["NestedInteger"]):
        self.nested_list = nestedList
        self.indices = []
        self.curr_index = 0
        self.stack = []

    def movePointer(self):
        while self.indices and (self.curr_index == len(self.nested_list)):
            self.curr_index = self.indices.pop()
            self.nested_list = self.stack.pop()

    def next(self) -> int:
        next_val = None

        if self.nested_list[self.curr_index].isInteger():
            next_val = self.nested_list[self.curr_index]
            self.curr_index += 1
            self.movePointer()
        else:
            self.stack.append(self.nested_list)
            self.indices.append(self.curr_index + 1)
            self.nested_list = self.nested_list[self.curr_index].getList()
            self.curr_index = 0
            next_val = self.next()

        return next_val

    def hasNext(self) -> bool:
        return self.curr_index < len(self.nested_list)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())