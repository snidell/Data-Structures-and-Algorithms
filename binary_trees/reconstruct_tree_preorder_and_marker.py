# 9.12 REcoNSTRUCT A BINARY TREE FROM A PREORDER TRAVERSAL WITH MARKERS
# Leetcode 1008
# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any
#  descendant of node.left has a value < node.val, and any descendant of
#  node.right has a value > node.val.  Also recall that a preorder traversal
#  displays the value of the node first, then traverses node.left,
#  then traverses node.right.)
from typing import List
from binary_tree_node import BinaryTreeNode

class Solution:
    # Time complexity : O(N) since we visit each node exactly once.
    # Space complexity : O(N) to keep the entire tree.
    def bstFromPreorder(self, preorder: List[int]) -> BinaryTreeNode:
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            # if all elements from preorder are used
            # then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # if the current element
            # couldn't be placed here to meet BST requirements
            print ("val: ",val,"(val < lower) ",(val < lower) ,"(val > upper) ",(val > upper))
            if val < lower or val > upper:
                return None

            # place the current element
            # and recursively construct subtrees
            idx += 1
            root = BinaryTreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()


if __name__ =="__main__":
    mySolution = Solution()
    myNode = mySolution.bstFromPreorder([8,5,1,7,10,12])
    print(myNode)
    print(myNode.left)
    print(myNode.right)

        #     8
        #    /  \
        #   5    10
        #  / \     \
        # 1   7     12
