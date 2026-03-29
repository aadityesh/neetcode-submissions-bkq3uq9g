# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        left = list1
        right = list2
        
        merged = ListNode()
        curr = merged

        while left and right:

            if left.val < right.val:
                curr.next = ListNode(left.val)
                left = left.next
                curr = curr.next
            
            elif left.val > right.val:
                curr.next = ListNode(right.val)
                right = right.next
                curr = curr.next
            
            else:

                if left.val == right.val:
                    curr.next = ListNode(left.val)
                    left = left.next
                    curr = curr.next
                    curr.next = ListNode(right.val)
                    right = right.next
                    curr = curr.next

        while left:
            curr.next = ListNode(left.val)
            left = left.next
            curr = curr.next

        while right:
            curr.next = ListNode(right.val)
            right = right.next
            curr = curr.next



        return merged.next
        