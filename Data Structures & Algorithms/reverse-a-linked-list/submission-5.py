# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
null < 0 < 1  2 > 3 > null
       h
               c
           p
               n


1. set next_node to cur.next
2. set cur.next to prev
3. move prev to cur
4. move cur to next_node


head | cur | next | prev
0    | 0   | 1    | null
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev

        