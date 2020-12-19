from typing import Optional
from linked_list.linked_list import LinkedList
from linked_list.list_node import ListNode
# 7.1 MERGE TWO SORTED LISTS
class Solution:
    def merge_two_sorted_lists(self,L1: Optional[ListNode], L2: Optional[ListNode])-> Optional[ListNode]:
        dummy_head  = tail = ListNode()

        while L1 and L2:
            if L1.data <=L2.data:
                tail.next, L1 = L1, L1.next
            else:
                tail.next, L2 = L2, L2.next
            tail = tail.next

        tail.next = L1 or L2
        return dummy_head.next

if __name__ == "__main__":
    mySolution = Solution()
    L1 = LinkedList()
    L2 = LinkedList()
    myList = LinkedList()

    myNode1 = ListNode(2)
    myNode2 = ListNode(5)
    myNode3 = ListNode(7)
    L1.insert_after(myNode1,myNode2)
    L1.insert_after(myNode2,myNode3)
    myList.print_list(myNode1)
    myNode4 = ListNode(3)
    myNode5 = ListNode(11)
    L2.insert_after(myNode4,myNode5)
    myList.print_list(myNode4)
    myList.print_list(mySolution.merge_two_sorted_lists(myNode1,myNode4))
