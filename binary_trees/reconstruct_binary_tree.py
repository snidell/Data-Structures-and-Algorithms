# 9.11 RECONSTRUCT A BINARY TREE FROM TRAVERSAL DATA

# Given an inorder traversal sequence and a preorder traversal sequence of
# a binary tree write a program to reconstruct the tree. Assume each node
# has a tmique key.
# Hint: Focus on the root.

from binary_tree_node import BinaryTreeNode
# Time complexity : O(N)
# Space complexity : O(N), since we store the entire tree.
class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: BinaryTreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = BinaryTreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]
            print("in_left: ",in_left,"in_right: ",in_right,"root_val: ",root_val,"index: ",index)
            # recursion
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root

        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        # {9: 0, 3: 1, 15: 2, 20: 3, 7: 4}
        print(idx_map)
        return helper()

if __name__ =="__main__":
    mySolution = Solution()
    # preorder inorder
    print(mySolution.buildTree([3,9,20,15,7],[9,3,15,20,7]))

  #   3
  #  / \
  # 9  20
  #   /  \
  #  15   7
