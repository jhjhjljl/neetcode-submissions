# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
[0] >    0 > 1 > 2 > 3 >   < 4 < 5 < 6 
         h
 t
                                     p
"""


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        prev = None
        cur = mid
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur 
            cur = next_node
        
        list1 = head
        list2 = prev
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            tail.next = list1
            tail = tail.next
            list1 = list1.next
            tail.next = list2
            tail = tail.next
            list2 = list2.next
        tail.next = list1

        