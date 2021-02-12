# 14.4 COMPUTE THE LCA IN A BST
# Design an algorithm that takes as input a BST and two nodes, and returns the
# LCA of the two nodes. For example, for the BST in Figure 14.1 on Page 203, and
# nodes C and G, your algorithm should return B. Assume all keys are distinct.
# Nodes do not have references to their parents.
#
# Hint: Take advantage of the BST property.


from binary_tree_node import BinaryTreeNode
class Solution:
    # Time complxity O(n) we could end up searching the whole tree in a poor case
    # Space compelxity is one due to the non recursive approach
    def find_lca(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Value of p
        p_val = p.data

        # Value of q
        q_val = q.data

        # Start from the root node of the tree
        node = root

        # Traverse the tree
        while node:
            # Value of current node or parent node.
            parent_val = node.data

            if p_val > parent_val and q_val > parent_val:
                # If both p and q are greater than parent
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                # If both p and q are lesser than parent
                node = node.left
            else:
                # We have found the split point, i.e. the LCA node.
                return node


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
    print(mySolution.find_lca(nA,nB,nF))
