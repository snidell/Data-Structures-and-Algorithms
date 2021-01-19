# 9.2 Write a program that checks whether a binary tree is symmetric.
# A binary tree is symmetric if you can draw a vertical line through the
# root and then the left subtree is the mirror image of the right subtree
# both in value and structure

from binary_tree_node import BinaryTreeNode

class Solution:
    def is_symmetric(self,tree: BinaryTreeNode) -> bool:
        def check_symmetric(subtree_0, subtree_1):
            if not subtree_0 and not subtree_1:
                return True
            elif subtree_0 and subtree_1:
                return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left)) #One subtree is empty, and the other is not.
            return False
        return not tree or check_symmetric(tree.left, tree.right)


if __name__ =="__main__":
    mySolution = Solution()
    nodeG = BinaryTreeNode(3)
    nodeF = BinaryTreeNode(2,nodeG,None)
    nodeE = BinaryTreeNode(6,nodeF,None)
    nodeD = BinaryTreeNode(3)
    nodeC = BinaryTreeNode(2,None,nodeD)
    nodeB = BinaryTreeNode(6,None,nodeC)
    nodeA = BinaryTreeNode(314,nodeB,nodeE)
    print(mySolution.is_symmetric(nodeA))
