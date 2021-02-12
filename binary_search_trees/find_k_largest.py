# 14.3 FIND THE k LARGEST ELEMENTS IN A BST
from binary_tree_node import BinaryTreeNode
from typing import List

# Write a program that takes as input a BST and an integer k, and returns the k 
# largest elements in the BST in decreasing order. For example, if the input is
# the BST in Figure 14.1 on Page 203 and k ~ 3, your program should return
# (53,47,43).
#
# Hint: What does an inorder traversal yield?
class Solution:

    # time complexity is O(h+k) h is the call stack and k is the size of the list
    # SPace is also the same
    def find_k_largest(Self,tree: BinaryTreeNode, k :int)-> List[BinaryTreeNode]:
        # Perform rever inorder traversal
        # inorder is Left, Node, right, so reverse is Right, Node, Left
        def helper(tree):
            if tree and len(k_elements) < k:
                helper(tree.right)
                if tree and len(k_elements) < k:
                    k_elements.append(tree.data)
                    helper(tree.left)
        k_elements: List[int] = []
        helper(tree)
        return k_elements



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
    print(mySolution.find_k_largest(nA,6))
