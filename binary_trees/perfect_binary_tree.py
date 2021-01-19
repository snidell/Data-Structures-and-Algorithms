# 9.15 COMPUTE THE RIGHT SIBLING TREE
# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children.
# The binary tree has the following definition:
#  BinaryTreeNode{val:int,left:Node,right:Node,next:node}
from binary_tree_node import BinaryTreeNode
import collections

class Solution:
    import collections

class Solution:
    # Time complexity O(N) process each node Once
    # Space complexity O(N) This is a perfect binary tree which means the last
    # level contains N/2N/2 nodes. The space complexity for breadth first
    # traversal is the space occupied by the queue which is dependent upon
    # the maximum number of nodes in particular level. So, in this case,
    # the space complexity would be O(N).
    def connect_w_queue(self, root: BinaryTreeNode) -> BinaryTreeNode:
        if not root:
            return root

        # Initialize a queue data structure which contains
        # just the root of the tree
        Q = collections.deque([root])

        # Outer while loop which iterates over
        # each level
        while Q:
            # Note the size of the queue
            size = len(Q)

            # Iterate over all the nodes on the current level
            for i in range(size):

                # Pop a node from the front of the queue
                node = Q.popleft()

                # This check is important. We don't want to
                # establish any wrong connections. The queue will
                # contain nodes from 2 levels at most at any
                # point in time. This check ensures we only
                # don't establish next pointers beyond the end
                # of a level
                if i < size - 1:
                    node.next = Q[0]

                # Add the children, if any, to the back of
                # the queue
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # Since the tree has now been modified, return the root node
        return root
    # Time Complexity: O(N) since we process each node exactly once.
    # Space Complexity: O(1) since we don't make use of any additional
    # data structure for traversing nodes on a particular level like the
    # previous approach does.
    def connect(self, root: BinaryTreeNode) -> BinaryTreeNode:
        if not root:
            return root

        # Start with the root node. There are no next pointers
        # that need to be set up on the first level
        leftmost = root

        # Once we reach the final level, we are done
        while leftmost.left:
            # Iterate the "linked list" starting from the head
            # node and using the next pointers, establish the
            # corresponding links for the next level
            head = leftmost
            while head:
                # CONNECTION 1
                head.left.next = head.right

                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left

                # Progress along the list (nodes on the current level)
                head = head.next

            # Move onto the next level
            leftmost = leftmost.left

        return root

if __name__ == "__main__":
    mySolution = Solution()

    node7 = BinaryTreeNode('7')
    node6 = BinaryTreeNode('6')
    node5 = BinaryTreeNode('5')
    node4 = BinaryTreeNode('4')
    node3 = BinaryTreeNode('3',node6,node7)
    node2 = BinaryTreeNode('2',node4,node5)
    node1 = BinaryTreeNode('1',node2,node3)

    mySolution.connect_w_queue(node1)
    mySolution.connect(node1)


    print("node1.next: ",node1.next) # None
    print("node2.next: ",node2.next) # 3
    print("node3.next: ",node3.next) # None


          #   1
          #/     \
        # 2       3
       # / \     / \
     # 4    5   6   7
