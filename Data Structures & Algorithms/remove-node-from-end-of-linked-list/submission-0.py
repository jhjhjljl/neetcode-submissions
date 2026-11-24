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
        
        cur = prev
        if n == 1:
            prev = prev.next
            cur.next = None
        else:
            prev2 = None
            count = 1
            while cur:
                if count == n:
                    prev2.next = prev2.next.next
                    break
                prev2 = cur
                cur = cur.next
                count += 1
        
        prev3 = None
        cur = prev
        while cur:
            next_node = cur.next
            cur.next = prev3
            prev3 = cur
            cur = next_node
        
        return prev3
        

            


        
        
        
        