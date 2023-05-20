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
        ## create dummy list so our left pointer is the node before our target node
        dummy = ListNode(0,head)
        left = dummy
        right = head

        ### first of all we set the gap between left and right to be equal to n meaning
        ## that when we are at the end of our list left is at len(list) - n - 1 because of dummy node in dummy
        while n>0:
            right = right.next
            n-=1
        
        # This works as well :)
        # for x in range(n):
        #     right = right.next
        
        ### loop untill right is at the end of the list, left should be at the node before our target node
        while right:
            left = left.next
            right = right.next

        ## to delete the node we set the node before target to the one after cutting it from the list
        left.next = left.next.next

        return dummy.next
        