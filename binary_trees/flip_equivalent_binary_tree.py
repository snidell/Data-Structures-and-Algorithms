# 951. Flip Equivalent Binary Trees
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
#
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
#
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivelent or false otherwise.
import collections
from typing import List
from binary_tree_node import BinaryTreeNode
class Solution:
    def flipEquiv(self, root1, root2) -> bool:
        # if they are both equal conitnue
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False


        return (self.flipEquiv(root1.left, root2.left) and
                self.flipEquiv(root1.right, root2.right) or
                self.flipEquiv(root1.left, root2.right) and
                self.flipEquiv(root1.right, root2.left))



if __name__ =="__main__":
    mySolution = Solution()
    node8 = BinaryTreeNode('8')
    node7 = BinaryTreeNode('7')
    node6 = BinaryTreeNode('6')
    node5 = BinaryTreeNode('5',node7,node8)
    node4 = BinaryTreeNode('4')
    node3 = BinaryTreeNode('3',node6)
    node2 = BinaryTreeNode('2',node4,node5)
    node1 = BinaryTreeNode('1',node2,node3)

    node17 = BinaryTreeNode('8')
    node16 = BinaryTreeNode('7')
    node15 = BinaryTreeNode('6')
    node14 = BinaryTreeNode('5',node8,node7)
    node13 = BinaryTreeNode('4')
    node12 = BinaryTreeNode('3',None,node6)
    node11 = BinaryTreeNode('2',node4,node5)
    node10 = BinaryTreeNode('1',node3,node2)
    print(mySolution.flipEquiv(node1,node10))
