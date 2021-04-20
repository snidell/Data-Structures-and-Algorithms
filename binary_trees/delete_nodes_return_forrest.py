# 1110. Delete Nodes And Return Forest
# Given the root of a binary tree, each node in the tree has a distinct value.
#
# After deleting all nodes with a value in to_delete, we are left with a forest
# (a disjoint union of trees).
#
# Return the roots of the trees in the remaining forest. You may return the
# result in any order.

from typing import List
from binary_tree_node import BinaryTreeNode

class Solution:
    def delNodes(self, root: BinaryTreeNode, to_delete: List[int]) -> List[BinaryTreeNode]:
        result = []
        # we do this because searching a set is a lot faster than a list or tuples
        to_delete = set(to_delete)

        def walk(node,parent_exist):
            # if this is a ending leaf pop back through the stack
            if node is None:
                return None
            # if this is a node we are looking for then mark the parent False
            # start signal of new sub tree and patch up the ending nodes of previous tree
            if node.data in to_delete:
                node.left = walk(node.left,parent_exist = False)
                node.right = walk(node.right,parent_exist = False)
                return None
            else:
                # if the parent doesn't exist we know its a start of a new subtree
                if not parent_exist:
                    result.append(node)
                node.left = walk(node.left,parent_exist = True)
                node.right = walk(node.right,parent_exist = True)
                return node

        walk(root,parent_exist= False)
        return result





if __name__ =="__main__":
    mySolution = Solution()
    node7 = BinaryTreeNode('7')
    node6 = BinaryTreeNode('6')
    node5 = BinaryTreeNode('5')
    node4 = BinaryTreeNode('4')
    node3 = BinaryTreeNode('3',node6,node7)
    node2 = BinaryTreeNode('2',node4,node5)
    node1 = BinaryTreeNode('1',node2,node3)
    to_delete = ['3','5']
    print(mySolution.delNodes(node1,to_delete))
