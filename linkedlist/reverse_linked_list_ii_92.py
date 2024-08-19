class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        dummy = ListNode(next=head)
        prev, left_prev, cur = None, dummy, head

        for _ in range(left - 1):
            left_prev = cur
            cur = cur.next

        for _ in range(right - left + 1):
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        
        if left_prev.next:
            left_prev.next.next = cur
            left_prev.next = prev

        return dummy.next

        