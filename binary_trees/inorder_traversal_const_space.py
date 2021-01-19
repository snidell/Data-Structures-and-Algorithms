# 9.10 IMPLEMENT AN INORDER TRAVERSAL WITH CONSTANT SPACE
#  Write a nonrecursive program for computing the inorder traversal sequence
#  for a binary tree. Assume nodes have parent fields.
# Hint: How can you tell whether a node is a left child or right child of its parent?
from binary_tree_node import BinaryTreeNode
from typing import List
class Solution:
    def inorder_traversal(self, tree: BinaryTreeNode) -> List[int]:
        prev, result = None, []
        while tree:
            if prev:
                print("current: ",tree.data,"prev: ",prev.data," result",result)
            else:
                print("current: ",tree.data,"prev: None"," result",result)
            if prev is tree.parent:
                # We came down to tree from prev.
                if tree.left: #Keep going left.
                    next = tree.left
                else:
                    result.append(tree.data)
                    #Done with left, so go right if right is not empty. Otherwise, # go up.
                    next = tree.right or tree.parent
            elif tree.left is prev:
                # We came up to tree from its left child.
                result.append(tree.data)
                #Done with left, so go right if right is not empty. Otherwise, go # up.
                next = tree.right or tree.parent
            else: #Done with both children, so move up.
                next = tree.parent


            prev, tree = tree, next
        return result

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

    node1.parent= node3
    node5.parent= node3
    node6.parent = node5
    node2.parent = node5
    node7.parent = node2
    node4.parent = node2
    node0.parent = node1
    node8.parent = node1


    # Tree tio traverse
    #       3
    #    /     \
    #  5        1
    #  /\      /  \
    # 6  2    0    8
    #   / \
    #  7   4

    print(mySolution.inorder_traversal(node3))
