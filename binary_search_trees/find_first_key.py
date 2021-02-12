# 14.2 FIND THE FIRST KEY GREATER THAN A GIVEN VALUE IN A BST
# Write a program that takes as input a BST and a value, and returns the first
# key that would appear in an inorder traversal which is greater than the input
# value.
# For example, when applied to the BST in Figure 14.1 on Page 203 you
# should return 29 for input 23.
#
# Hint: Perform binary search, keeping some additional state.
from binary_tree_node import BinaryTreeNode
from typing import Optional
class Solution:
    def find_first_greater_than_k(self,tree:BinaryTreeNode,k :int) ->Optional[BinaryTreeNode]:
        subtree, first_so_far = tree, None
        while subtree:
            print("data:" ,subtree.data," ",first_so_far)
            if subtree.data > k:
                first_so_far, subtree = subtree, subtree.left
            else:
                # Root and all subtrees to the left are <= k so skip them
                subtree = subtree.right
        # returns whole tree node not just the data
        return first_so_far

if __name__ =="__main__":
    mySolution = Solution()
    nP = BinaryTreeNode(53)
    nO = BinaryTreeNode(47,None,nP)
    nN = BinaryTreeNode(41)
    nM = BinaryTreeNode(31)
    nL = BinaryTreeNode(29,None,nM)
    nK = BinaryTreeNode(37,nL,nN)
    nJ = BinaryTreeNode(23,None,nK)
    nI = BinaryTreeNode(43,nJ,nO)
    nH = BinaryTreeNode(13)
    nG = BinaryTreeNode(17,nH)
    nF = BinaryTreeNode(11,None,nG)
    nE = BinaryTreeNode(5)
    nD = BinaryTreeNode(2)
    nC = BinaryTreeNode(3,nD,nE)
    nB = BinaryTreeNode(7,nC,nF)
    nA = BinaryTreeNode(19,nB,nI)
    print(mySolution.find_first_greater_than_k(nA,5)) #["29", null, "31"]
