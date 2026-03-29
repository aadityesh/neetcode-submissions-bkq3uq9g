# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def get_all_elements(self, list1, list2):

        res = []
        tail1 = list1
        tail2 = list2

        while tail1:
            res.append(tail1.val)
            tail1 = tail1.next
        
        while tail2:
            res.append(tail2.val)
            tail2 = tail2.next
        
        return res

    def recursive(self, left, right, curr, merged):

        if left is None: 
            curr.next = right
            return

        if right is None: 
            curr.next = left
            return

        if left.val <= right.val:
            curr.next = left
            left = left.next
            self.recursive(left, right, curr.next, merged)
        
        else:
            curr.next = right
            right = right.next
            self.recursive(left, right, curr.next, merged)
        

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # all_elements = self.get_all_elements(list1, list2)

        # all_elements.sort()
        
        # n = len(all_elements)
        # merged = ListNode()
        # tail = merged

        # for index in range(0, n):
        #     new_node = ListNode(all_elements[index])
        #     tail.next = new_node
        #     tail = new_node

        
        # return merged.next
            
        # left = list1
        # right = list2
        
        # merged = ListNode()
        # curr = merged

        # while left and right:

        #     if left.val <= right.val:
        #         curr.next = left
        #         left = left.next
        #     else:
        #         curr.next = right
        #         right = right.next
            
        #     curr = curr.next

        # if left:
        #     curr.next = left
        
        # if right:
        #     curr.next = right

        # return merged.next

        left = list1
        right = list2
        
        merged = ListNode()
        curr = merged

        self.recursive(left, right, curr, merged)

        return merged.next

        