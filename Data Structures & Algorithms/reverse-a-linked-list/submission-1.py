# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverse_list(self, head, prev, curr):

        if curr is None: return prev

        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

        return self.reverse_list(head, prev, curr)
        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # curr = head
        # prev = None

        # while curr:
        #     next_node = curr.next

        #     curr.next = prev
        #     prev = curr
        #     curr = next_node

        # return prev
        prev, curr = None, head
        return self.reverse_list(head, prev, curr)