# 9.4 COMPUTE THE L C A WHEN NODES HA VE P ARENT POINTERS
# Given two nodes in a binary tree, design an algorithm that computes their LCA.
# Assume that each node has a parent pointer.
# Hint: The problem is easy if both nodes are the same distance from the root.

from binary_tree_node import BinaryTreeNode
from typing import Optional
class Solution:
    def lca(self,node0: BinaryTreeNode, node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:
        #  crawl up to the root
        def get_depth(node):
            depth = 0
            while node.parent:
                depth += 1
                node = node.parent
            return depth

        depth0, depth1 = map(get_depth, (node0, node1))
        print(depth0)
        print(depth1)
        # Makes node0 as the deeper node in order to simplify the code.
        if depth1 > depth0:
            node0, node1 = node1, node0
        # Ascends from the deeper node.
        depth_diff = abs(depth0 - depth1)
        while depth_diff:
            node0 = node0.parent
            depth_diff -= 1
        # Now ascends both nodes until we reach the LCA.
        while node0 is not node1:
            node0, node1 = node0.parent, node1.parent
        return node0


if __name__ == "__main__":
    nodeP = BinaryTreeNode('P')
    nodeO = BinaryTreeNode('O',None,nodeP)
    nodeN = BinaryTreeNode('N')
    nodeM = BinaryTreeNode('M')
    nodeL = BinaryTreeNode('L',None,nodeM)
    nodeK = BinaryTreeNode('K',nodeL,nodeN)
    nodeJ = BinaryTreeNode('J',None,nodeK)
    nodeI = BinaryTreeNode('I',nodeJ,nodeO)
    nodeH = BinaryTreeNode('H')
    nodeG = BinaryTreeNode('G',nodeH,None)
    nodeF = BinaryTreeNode('F',None,nodeG)
    nodeE = BinaryTreeNode('E')
    nodeD = BinaryTreeNode('D')
    nodeC = BinaryTreeNode('C',nodeD,nodeE)
    nodeB = BinaryTreeNode('B',nodeC,nodeF)
    nodeA = BinaryTreeNode('A',nodeB,nodeI)
    nodeB.parent = nodeA
    nodeC.parent = nodeB
    nodeD.parent = nodeC
    nodeE.parent = nodeC
    nodeF.parent = nodeB
    nodeG.parent = nodeF
    nodeH.parent = nodeG
    nodeI.parent = nodeA
    nodeJ.parent = nodeI
    nodeK.parent = nodeJ
    nodeL.parent = nodeK
    nodeM.parent = nodeL
    nodeN.parent = nodeK
    nodeO.parent = nodeI
    nodeP.parent = nodeO
    mySolution = Solution()
    print(mySolution.lca(nodeM,nodeP).data)
