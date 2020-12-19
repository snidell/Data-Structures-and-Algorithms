from .list_node import ListNode
class LinkedList:
    def insert_after(self,node: ListNode, new_node: ListNode)-> None:
        new_node.next = node.next
        node.next = new_node
    def delete_after(self,node: ListNode)->None:
        node.next = node.next.next
    def search_list(self,L:ListNode, key:int)->ListNode:
        while L.next and L.data!=key:
            L = L.next
        # returns null if the value is not found
        return L
    def reverse(self,L:ListNode)->ListNode:
        prev = None
        current = L
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        L = prev
        return L
    def print_list(self,L: ListNode):
        while L:
            print(L.data,"->",end='')
            L = L.next
        print("->None")

if __name__ == "__main__":
    myList = LinkedList()
    myNode1 = ListNode(1)
    myNode2 = ListNode(6)
    myList.insert_after(myNode1,myNode2)
    myNode3 = ListNode(7)
    myList.insert_after(myNode2,myNode3)
    myNode4 = ListNode(4)
    myList.insert_after(myNode3,myNode4)
    myNode5 = ListNode(-5)
    myList.insert_after(myNode4,myNode5)
    myList.print_list(myNode1)
