class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        dummy = ListNode(next=head)
        prev, cur = dummy, head
        
        while cur and cur.next:
            next = cur.next.next
            left_next = cur.next

            left_next.next = cur
            cur.next = next
            prev.next = left_next

            prev = cur
            cur = next
        return dummy.next
        
        