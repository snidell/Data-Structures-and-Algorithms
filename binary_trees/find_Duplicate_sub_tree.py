# 652. Find Duplicate Subtrees
# Given the root of a binary tree, return all duplicate subtrees.
#
# For each kind of duplicate subtrees, you only need to return the root node of
# any one of them.
#
# Two trees are duplicate if they have the same structure with the same node
# values.

from typing import List
from binary_tree_node import BinaryTreeNode

class Solution:
    def findDuplicateSubtrees(self, root: BinaryTreeNode) -> List[BinaryTreeNode]:
        if root is None:
            return []
        self.map = {}
        self.result = []
        self.preorder(root)
        print(self.map)
        return self.result

    def preorder(self, root):
        if root:
            # construct preorder string
            ls = str(root.data) + "-" + self.preorder(root.left) + "-" + self.preorder(root.right)
            count = self.map.get(ls, 0)
            if count == 1:
                self.result.append(root)
            self.map[ls] = count + 1
            return ls
        else:
            return "#"

if __name__ =="__main__":
    mySolution = Solution()
    node8 = BinaryTreeNode('4')
    node7 = BinaryTreeNode('4')
    node6 = BinaryTreeNode('2',node8)
    node5 = BinaryTreeNode('2')
    node4 = BinaryTreeNode('4')
    node3 = BinaryTreeNode('3',node6,node7)
    node2 = BinaryTreeNode('2',node4)
    node1 = BinaryTreeNode('1',node2,node3)
    print(mySolution.findDuplicateSubtrees(node1))
