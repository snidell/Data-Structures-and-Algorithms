# 7.2 REVERSE A SINGLE SUBLIST
# Write a program which takes a singly linked list L and two integers s and f
# as arguments, and reverses the order of the nodes from the sth node to nth node,
#  inclusive. The numbering begins at 1, i.e., the head node is the first node.
#   Do not allocate additional nodes.
# The time complexity is dominated by the search for the fth node, i.e., O(f).
from typing import Optional
from linked_list.linked_list import LinkedList
from linked_list.list_node import ListNode
class Solution:
    def reverse_sublist(self,L: ListNode, start: int,finish:int)->Optional[ListNode]:
        dummy_head = sublist_head = ListNode(0, L)
        # Finds the start of the sublist.
        for _ in range(1,start):
            sublist_head = sublist_head.next

        # Reverses sublist.
        sublist_iter = sublist_head.next
        for _ in range(finish-start):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = temp.next,sublist_head.next,temp
        return dummy_head.next

if __name__ == "__main__":
    mySolution = Solution()

    myNode1 = ListNode(11)
    myNode2 = ListNode(3)
    myNode3 = ListNode(5)
    myNode4 = ListNode(7)
    myNode5 = ListNode(2)
    L1 = LinkedList()
    L1.insert_after(myNode1,myNode2)
    L1.insert_after(myNode2,myNode3)
    L1.insert_after(myNode3,myNode4)
    L1.insert_after(myNode4,myNode5)
    L1.print_list(myNode1)
    L1.print_list(mySolution.reverse_sublist(myNode1,2,4))
