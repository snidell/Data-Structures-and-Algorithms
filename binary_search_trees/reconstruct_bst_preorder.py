# 14.5 RECONSTRUCT A BST FROM TRAVERSAL DATA

# Suppose you are given the sequence in which keys are visited in an inorder
# traversal of a BST, and all keys are distinct. Can you reconstruct the BST
# from the sequence? If so, write a program to do so. Solve the same problem for
# preorder and postorder traversal sequences.
#
# Hint: Draw the five BSTs on the keys 1, 2, 3, and the corresponding traversal
# orders.

# same as leetcode 1008

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            # if all elements from preorder are used
            # then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # if the current element
            # couldn't be placed here to meet BST requirements
            if val < lower or val > upper:
                return None

            # place the current element
            # and recursively construct subtrees
            idx += 1
            root = TreeNode(val)
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
