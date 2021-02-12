# 14.1 Test if a tree satisfies the BST property
# Write a program that takes as input a binary tree and checks if the tree 
# satisfies the BST property.
#
# Hint: Is it correct to check for each node that its
# key is greater than or equal to the key at its left child and less than or
# equal to the key at its right child?

from binary_tree_node import BinaryTreeNode


class Solution:
    # Time complexity is O(n) because we touch every treenode
    # Space is O(h) where h is the height of the tree
    def is_binary_tree(Self,tree:BinaryTreeNode)->bool:
        def are_keys_in_range(tree,low_range = float('-inf'),
                              high_range= float('inf')):

            # if we the end of a leaf return this path is ok
            if not tree:
                return True
            # Failure case. int needs to be balanced between its low and high range
            elif not low_range <= tree.data <=high_range:
                print("low: ",low_range,"tree data: ",tree.data,"high: ",high_range)
                return False
            else:
                # if everything is ok keep going down the tree
                return (are_keys_in_range(tree.left,low_range,tree.data) and
                        are_keys_in_range(tree.right,tree.data,high_range))
        return are_keys_in_range(tree)



if __name__ == "__main__":
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

    print(mySolution.is_binary_tree(nA)) # True

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
    nA = BinaryTreeNode(200,nB,nI)

    print(mySolution.is_binary_tree(nA)) # False
