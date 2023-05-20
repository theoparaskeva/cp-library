# You are given two linked lists: list1 and list2 of sizes n and m respectively.

# Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

# The blue edges and nodes in the following figure indicate the result:
# Build the result list and return its head.
# Example 1:
# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the 
# entire list2 in their place. The blue edges and nodes in the above figure indicate the result.

from typing import ListNode,Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        ## create dummy node 
        dummy1 = ListNode(0,list1)
        dummyl2 = list2
        l1 = dummy1
        l2 = dummy1
        ### find end of list2
        while dummyl2.next:
            dummyl2 = dummyl2.next
        
        ## point to node before a node
        for _ in range(a):
            l1 = l1.next
        
        # point to node before b node
        for _ in range(b):
            l2 = l2.next
        
        ## end of list2 next is set to node after b node
        dummyl2.next = l2.next.next
        
        ## add node up to a node to newly created list2 which contains all nodes after b
        l1.next = list2
        
        return list1