# 8.6 COMPUTE BINARY TREE NODES IN ORDER OF INCREASING DEPTH
#Given a binary tree, return an array consisting of the keys at the same level.
# Keys should appear in the order of the corresponding nodes' depths, breaking
# ties from left to right. For example, you should
# return ((314), (6,6), (271,561,2,271), (28,0,3, 1,28), (17,401,257), (641))
# for the binary tree
#  102. Binary Tree Level Order Traversal

from typing import List
from binary_tree_node import BinaryTreeNode
from collections import deque
class Solution:
    #recursive approach
    def recursive_binary_tree_depth_order(self,root: BinaryTreeNode)-> List[List[int]]:
        levels = []
        if not root:
            return levels

        def helper(node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.data)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

        helper(root, 0)
        return levels

    # iterative approach
    def binary_tree_depth_order(self,root: BinaryTreeNode)-> List[List[int]]:
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root])
        print(queue)
        while queue:
            # start the current level
            levels.append([])
            # number of elements in the current level
            level_length = len(queue)
            print("length:",level_length)

            for i in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                levels[level].append(node.data)

                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # go to next level
            level += 1

        return levels

if __name__ == "__main__":
    mySolution = Solution()
    node10 = BinaryTreeNode(10)
    node9 = BinaryTreeNode(9,None,node10)
    node8 = BinaryTreeNode(8,None,None)
    node7 = BinaryTreeNode(7,None,node9)
    node6 = BinaryTreeNode(6,node8,node7)
    node5 = BinaryTreeNode(5)
    node4 = BinaryTreeNode(4,None,node5)
    node3 = BinaryTreeNode(3,None,node4)
    node2 = BinaryTreeNode(2,None,node3)
    node1 = BinaryTreeNode(1,node6,node2)
    print("iterative")
    print(mySolution.binary_tree_depth_order(node1))
    print("recursive")
    print(mySolution.recursive_binary_tree_depth_order(node1))
