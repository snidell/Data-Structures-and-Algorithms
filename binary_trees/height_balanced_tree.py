#  9.1
# A binary tree is said to be height-balanced if for each node in the tree,
# the difference in the height of its left and right subtrees is at most one.
# A perfect binary tree is height-balanced, as is a complete
# binary tree. A height-balanced binary tree does not have to be perfect or
# complete-see Figure 9.2 for an example.
from binary_tree_node import BinaryTreeNode
import collections

class Solution:
    def isBalancedHelper(self, root: BinaryTreeNode) -> (bool, int):
        # An empty tree is balanced and has height -1
        if not root:
            return True, -1

        # Check subtrees to see if they are balanced.
        leftIsBalanced, leftHeight = self.isBalancedHelper(root.left)
        if not leftIsBalanced:
            return False, 0
        rightIsBalanced, rightHeight = self.isBalancedHelper(root.right)
        if not rightIsBalanced:
            return False, 0

        # If the subtrees are balanced, check if the current tree is balanced
        # using their height
        if root.left:
            print("root.left: ",root.left.data)
        if root.right:
            print("root.right", root.right.data)
        print("leftheight: ",leftHeight, "rightheight: ",rightHeight,"sum: ",(leftHeight-rightHeight))
        return (abs(leftHeight - rightHeight) < 2), 1 + max(leftHeight, rightHeight)

    def isBalanced(self, root: BinaryTreeNode) -> bool:
        return self.isBalancedHelper(root)[0]


if __name__ == "__main__":
    mySolution = Solution()
    node15 = BinaryTreeNode('15')
    node7 = BinaryTreeNode('7')
    node20 = BinaryTreeNode('20',node15,node7)
    node9 = BinaryTreeNode('9')
    node3 = BinaryTreeNode('3',node9,node20)
#   height balanced tree node 9 and node 15/7 have a difference no larger than 1
#                  3
#               /    \
#              9      20
#                    /  \
#                   15   7
#
#
#
    nodeg = BinaryTreeNode('4')
    nodef = BinaryTreeNode('4')
    nodee = BinaryTreeNode('3')
    noded = BinaryTreeNode('3',nodef,nodeg)
    nodec = BinaryTreeNode('2')
    nodeb = BinaryTreeNode('2',noded,nodee)
    nodea = BinaryTreeNode('1',nodeb,nodec)
#  not a height balanced tree. node 2 and node 4 have a difference larger than 1 (2)
#                            1
#                          /   \
#                         2      2
#                       /  \
#                      3    3
#                    /  \
#                   4    4
#
#
