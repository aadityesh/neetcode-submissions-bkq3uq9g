

class Solution:
    def print_list(self, head):
        curr = head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")
    def reorderList(self, head: Optional[ListNode]) -> None:

        hash_list = {}

        curr = head
        pos = 0

        while curr:
            hash_list[pos] = curr
            curr = curr.next
            pos += 1
        
        
        n = len(hash_list)
        # print(f"n: {n}")
        even = 1
        odd = n - 1
        curr = head

        for i in range(1, n):

            if i % 2 == 0:
                # print(f"even: {even}")
                curr.next = hash_list[even]
                hash_list[even].next = None
                even += 1
                
            else:
                # print(f"odd: {odd}")
                curr.next = hash_list[odd]
                hash_list[odd].next = None
                odd -= 1

            # print(f"--{curr.val}", end= " ")
            self.print_list(head)
            curr = curr.next

                



            

        