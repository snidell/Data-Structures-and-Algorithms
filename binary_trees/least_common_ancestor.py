# 9.3 least common ancestor
#  leetcode: 236. Lowest Common Ancestor of a Binary Tree
# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
# in the tree.
#
# According to the definition of LCA on Wikipedia: “The lowest common ancestor
# is defined between two nodes p and q as the lowest node in T that has
# both p and q as descendants
# (where we allow a node to be a descendant of itself).”

from binary_tree_node import BinaryTreeNode
from typing import Optional
import collections
class Solution:
    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root: BinaryTreeNode, p: BinaryTreeNode,
                              q: BinaryTreeNode) -> BinaryTreeNode:
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def recurse_tree(current_node)->bool:

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

    def lca(self,tree:BinaryTreeNode,node0: BinaryTreeNode,node1:BinaryTreeNode)-> Optional[BinaryTreeNode]:
            Status = collections.namedtuple('Status',('num_target_nodes','ancestor'))

            def lca_helper(tree,node0,node1):
                if tree is None:
                    return Status(num_target_nodes=0,ancestor=None)
                left_result = lca_helper(tree.left,node0,node1)
                if left_result.num_target_nodes == 2:
                    # found both nodes in left subtree
                    return left_result
                right_result = lca_helper(tree.right,node0,node1)
                if right_result.num_target_nodes == 2:
                    # found both in right subtree
                    return right_result
                num_target_nodes = (left_result.num_target_nodes +
                                    right_result.num_target_nodes +
                                    (node0,node1).count(tree))
                return Status(num_target_nodes,tree if num_target_nodes ==2 else None)

            return lca_helper(tree,node0,node1).ancestor



if __name__ == "__main__":
    mySolution = Solution()
    node7= BinaryTreeNode('7')
    node4= BinaryTreeNode('4')
    node2= BinaryTreeNode('2',node7,node4)
    node6= BinaryTreeNode('6')
    node5= BinaryTreeNode('5',node6,node2)
    node0= BinaryTreeNode('0')
    node8= BinaryTreeNode('8')
    node1= BinaryTreeNode('1',node0,node8)
    node3= BinaryTreeNode('3',node5,node1)

    print(mySolution.lowestCommonAncestor(node3,node5,node1).data)
    print(mySolution.lca(node3,node5,node1).data)
              # LCA of nodes 5 and 1 is 3
              #       3
              #    /     \
              #  5        1
              #  /\      /  \
              # 6  2    0    8
              #   / \
              #  7   4
    print(mySolution.lowestCommonAncestor(node3,node5,node4).data)
    print(mySolution.lca(node3,node5,node4).data)

              # LCA of nodes 5 and 4 is 5
              #       3
              #    /     \
              #  5        1
              #  /\      /  \
              # 6  2    0    8
              #   / \
              #  7   4
