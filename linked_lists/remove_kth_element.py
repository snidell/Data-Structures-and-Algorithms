# 7.7 REMOVE THE kTH LAST ELEMENT FROM A LIST
#
# Given a singly linked list and an integer k, write a program to remove the kth
 # last element from the list. Your algorithm cannot use more than a few words of
 # storage, regardless of the length of the list. 1n particular, you cannot assume
 #  that it is possible to record the length of the list.
from typing import Optional
from linked_list.linked_list import LinkedList
from linked_list.list_node import ListNode

class Solution:
    def remove_kth_last(self,L: ListNode, k: int)->Optional[ListNode]:
        dummy_head = ListNode(0,L)

        first = dummy_head.next
        for _ in range(k):
            print("go")
            first = first.next

        second = dummy_head
        print("first: ",first.data," second:",second.data)
        while first:
            first, second = first.next, second.next

        second.next = second.next.next
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
    L1.print_list(mySolution.remove_kth_last(myNode1,3))
