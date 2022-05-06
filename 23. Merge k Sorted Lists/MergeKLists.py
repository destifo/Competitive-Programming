class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        l, r = 0, n - 1
        mid = n // 2
        while l < r:
            if l == r - 1:
                if not lists[l]:
                    self.merge(lists, l, r)
                return lists[r]
            elif lists[l]:
                self.merge(lists, l, l + 1)
            elif list[r]:
                self.merge(lists, r - 1, r)

            l, r = l + 1, r - 1

        return lists[r]


    def merge(self, lists, a, b):
        head1 = lists[a]
        head2 = lists[b]
        if head2 == None:
            head2 = head1
        elif head1 == None:
            head1 = head2
        else:
            curr1 = head2 if (head1.val >= head2.val) else head1
            curr2 = head1 if curr1 == head2 else head2
            smallHead = curr1

            while curr1.next.val < curr2.val or curr1.next != None:
                curr1 = curr1.next

            nxt = curr1.next
            curr1.next = curr2
            
            while curr2.next:
                curr2 = curr2.next

            curr2.next = nxt
            lists[b], lists[a] = smallHead, smallHead