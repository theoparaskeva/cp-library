# Given the head of a linked list, rotate the list to the right by k places.
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import ListNode, Optional
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        ### count length of list and point to last node
        l,cur = 1,head
        while cur.next:
            l+=1
            cur = cur.next
        
        
        k = k%l
        if k == 0:
            return head
        
        
        new = head
        ### find the point where we pivot the list
        for i in range(l-k-1):
            new = new.next
        ### point to nodes after pivot
        piv = new.next
        ### cut list at pivot by setting next to none
        new.next = None
        ### add  the pre pivot nodes to the final node
        cur.next = head
        return piv
            