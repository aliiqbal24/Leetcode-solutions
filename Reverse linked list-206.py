## NOTES
# We can brute force this by converting to an array then reversing, then converting back
# This would take O(n) space, we can do better by doing inplace
# By flipping the pointers, we can flip the list in place
# Implement a two pointer approach, current, on the head and a prev, at null
# iterate through the list, pointing current to previous for each link
# at the last node, current will be null, and prev will be our head

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

