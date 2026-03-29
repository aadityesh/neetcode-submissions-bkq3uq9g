# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_length(self, head):
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        return length

    def removeNthFromEnd(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # length = self.get_length(head)
        # times = length - k

        # if times == 0:
        #     head = head.next
        #     return head

        # prev = None
        # curr = head

        # while times:
            
        #     prev = curr
        #     curr = curr.next
            
        #     times -= 1

        
        # prev.next = curr.next

        # return head

        slow, fast = head, head
        times = k

        while times:
            fast = fast.next
            times -= 1

        if not fast: return head.next # When node is Kth Length

        prev = slow
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next
        
        prev.next = slow.next
        del slow
        return head
        
        




        