# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 # Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode,Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy
        right = head

        while n>0:
            right = right.next
            n-=1
        
        while right:
            left = left.next
            right = right.next

        left.next = left.next.next

        return dummy.next
        