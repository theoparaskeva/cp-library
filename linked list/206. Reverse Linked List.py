# Given the head of a singly linked list, reverse the list, and return the reversed list.

#  Example 1:


# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import ListNode,Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr = None,head

        while curr:
            ## keep track of the next element in the original list
            nxt = curr.next
            ## set the next to prev - first iteration will be 0
            curr.next = prev
            ## set the prev to the current node
            prev = curr
            ## go to next node in the original order
            curr = nxt
        ## return the last first node in the list
        return prev
        