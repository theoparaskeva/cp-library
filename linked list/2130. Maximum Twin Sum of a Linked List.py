# In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is
# known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

# For example, if n = 4, then node 0 is the twin of node 3, and node 1 is 
# the twin of node 2. These are the only nodes with twins for n = 4.
# The twin sum is defined as the sum of a node and its twin.

# Given the head of a linked list with even length, return the maximum twin sum of the linked list.

 
# Example 1:

# Input: head = [5,4,2,1]
# Output: 6
# Explanation:
# Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
# There are no other nodes with twins in the linked list.
# Thus, the maximum twin sum of the linked list is 6. 


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import ListNode,Optional

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        mx = -1
        cur = head
        left = cur
        right = head
        ### find middle of list
        while right:
            left = left.next
            right = right.next.next
        
        #### Reverse list
        prev,rev = None,left

        while rev:
            nxt = rev.next
            rev.next = prev
            prev = rev
            rev = nxt
        
        ### loop through both halves of the list adding up each corresponding value, keeping the max
        while prev:
            s = prev.val + cur.val
            prev = prev.next
            cur = cur.next
            mx = max(mx,s)
        ## return the max!
        return mx

        
        