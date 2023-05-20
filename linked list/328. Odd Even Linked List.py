# Given the head of a singly linked list, group all the nodes with odd indices 
#     together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

# Note that the relative order inside both the even and odd groups should remain as it was in the input.

# You must solve the problem in O(1) extra space complexity and O(n) time complexity.

# Example 1:


# Input: head = [1,2,3,4,5]
# Output: [1,3,5,2,4]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import ListNode,Optional

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        # pointer at start of list
        odd = head
        # pointer at first even index
        even = head.next
        ehead = even

        while even and even.next:
            # change odd next to the even next ensuring that it skips onto the 2nd odd index
            odd.next = even.next
            # keep going down the list
            odd = odd.next
            # change even next to the next even integer 
            even.next = odd.next
            ## keep looping
            even = even.next
        ## concat the list of odd numbers within head to ehead which is pointed at first index in the even list
        odd.next = ehead
        return head
            