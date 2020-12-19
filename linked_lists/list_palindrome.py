#  7.11 TEST WHETHER A SINGLY LINKED LIST IS PALINDROMIC
from linked_list.linked_list import LinkedList
from linked_list.list_node import ListNode
class Solution:
    def is_linked_list_a_palindrome(self,L: ListNode) -> bool:
        #Finds the second half of L.
        slow = fast = L
        L1 = LinkedList()
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            #Compares the first half and the reversed second half lists.
            first_half_iter, second_half_iter = L, L1.reverse(slow)
            while second_half_iter and first_half_iter:
                if second_half_iter.data != first_half_iter.data:
                    return False
                second_half_iter, first_half_iter = (second_half_iter.next, first_half_iter.next)
        return True


if __name__ == "__main__":
    mySolution = Solution()
    myNode1 = ListNode(0)
    myNode2 = ListNode(1)
    myNode3 = ListNode(2)
    myNode4 = ListNode(1)
    myNode5 = ListNode(0)
    L1 = LinkedList()
    L1.insert_after(myNode1,myNode2)
    L1.insert_after(myNode2,myNode3)
    L1.insert_after(myNode3,myNode4)
    L1.insert_after(myNode4,myNode5)
    L1.print_list(myNode1)
    # L1.print_list(L1.reverse(myNode1))
    L1.print_list(myNode1)
    print(mySolution.is_linked_list_a_palindrome(myNode1))
