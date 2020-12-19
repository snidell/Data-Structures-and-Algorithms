# 7.10 IMPLEMENT EVEN-ODD MERGE
# Consider a singly linked list whose nodes are numbered starting at O.
# Define the even-odd merge of the list to be the list consisting of the
# even-numbered nodes followed by the odd-numbered nodes.
from typing import Optional
from linked_list.linked_list import LinkedList
from linked_list.list_node import ListNode

class Solution:
    def even_odd_merge(self,L:ListNode)->Optional[ListNode]:
        if L is None:
            return L
        even_dummy_head, odd_dummy_head = ListNode(0), ListNode(0)
        tails, turn = [even_dummy_head,odd_dummy_head] , 0
        while L:
            tails[turn].next = L
            L = next
            tails[turn] = tails[turn].next
            turn ^= 1 # Alternate between even and odd.
        tails[0].next = None
        tails[1].next = odd_dummy_head.next
        return even_dummy_head.next




if __name__ == "__main__":
    mySolution = Solution()
    myNode1 = ListNode(0)
    myNode2 = ListNode(1)
    myNode3 = ListNode(2)
    myNode4 = ListNode(3)
    myNode5 = ListNode(4)
    L1 = LinkedList()
    L1.insert_after(myNode1,myNode2)
    L1.insert_after(myNode2,myNode3)
    L1.insert_after(myNode3,myNode4)
    L1.insert_after(myNode4,myNode5)
    L1.print_list(myNode1)
    L1.print_list(mySolution.even_odd_merge(myNode1,4))
