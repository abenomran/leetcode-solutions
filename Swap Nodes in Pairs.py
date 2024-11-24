# Medium
from typing import Optional, ListNode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head

        dummy = ListNode(next=head)
        prev, cur = dummy, head

        while cur and cur.next:
            first = cur
            second = cur.next

            # Swap the two nodes
            prev.next = second
            first.next = second.next
            second.next = first

            # Update pointers for the next pair
            prev = first
            cur = first.next

        return dummy.next


