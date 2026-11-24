# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
 < 1 < 2 < 3 < 4 
   h
               p
               c

"""

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        reverse_head = prev
        
        cur = reverse_head
        if n == 1:
            reverse_head = reverse_head.next
            cur.next = None
        else:
            before = None
            count = 1
            while cur:
                if count == n:
                    before.next = before.next.next
                    break
                before = cur
                cur = cur.next
                count += 1
        
        prev = None
        cur = reverse_head
        while cur:
            next_node = cur.next
            cur.next = prev 
            prev = cur
            cur = next_node
        
        return prev 
        

            


        
        
        
        