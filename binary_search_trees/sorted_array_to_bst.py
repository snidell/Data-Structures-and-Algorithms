# 14.8 BUILD A MINIMUM HEIGHT EST FROM A SORTED ARRAY
# Given a sorted array, the number of ESTs that can be built on the entries in
# the array grows enormously with its size. Some of these trees are skewed, and
# are closer to lists; others are more balanced. See Figure 14.3 on Page 210
# for an example.
#
# How would you build a EST of minimum possible height from a sorted array?
# Hint: Which element should be the root?
from typing import List
from binary_tree_node import BinaryTreeNode

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> BinaryTreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose left middle node as a root
            p = (left + right) // 2

            # preorder traversal: node -> left -> right
            root = BinaryTreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.sortedArrayToBST([1,2,3,4,5,6,7,8,9,10]))
