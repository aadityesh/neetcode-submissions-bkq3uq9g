

class Solution:

    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")

    def find_middle(self, head):

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def reverse_list(self, head):

        prev, curr = None, head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev


    def reorderList(self, head: Optional[ListNode]) -> None:

        # middle_node = self.find_middle(head)
        # reverse_half = self.reverse_list(middle_node)
        # print(f"middle {middle_node.val}")
        # middle_node.next = None

        # curr = head

        # while curr:

        #     current_next = curr.next
            
        #     if reverse_half: 
        #         reverse_next = reverse_half.next
        #     else: 
        #         reverse_next = None

        #     curr.next = reverse_half
        #     reverse_half.next = current_next

        #     curr = current_next
        #     reverse_half = reverse_next
        
        # if reverse_half:
        #     curr.next = reverse_half


        # nodes = []
        # curr = head

        # while curr:
        #     nxt = curr.next
        #     curr.next = None
        #     nodes.append(curr)
        #     curr = nxt

        # n = len(nodes)
        # print(n)
        # L, R = 1, n - 1
        # curr = nodes[0]

        # while L < R:
            
        #     curr.next = nodes[R]
        #     curr = curr.next

        #     curr.next = nodes[L]
        #     curr = curr.next

        #     L += 1
        #     R -= 1

        # if L == R:
        #     curr.next = nodes[L]
    

        middle_node = self.find_middle(head)
        rev = self.reverse_list(middle_node.next)
        middle_node.next = None

        l1 = head

        while rev:

            nxt1, nxt2 = l1.next, rev.next

            l1.next = rev
            rev.next = nxt1

            l1, rev = nxt1, nxt2








                



            

        