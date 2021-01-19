from binary_tree_node import BinaryTreeNode

class Traverse:
    # preorder traversal root->left->right
    # in order traversal left->root->right
    # post ordfer traversal left->right->root
    def tree_traversal(self,root:BinaryTreeNode):
        if root:
            # preorder
            # print(root.data)
            self.tree_traversal(root.left)
            # in order
            print(root.data)
            self.tree_traversal(root.right)
            #post order
            # print(root.data)

if __name__ =="__main__":

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
    myTraverse = Traverse()
    myTraverse.tree_traversal(nodeA)
    myItem = 1
    myItem2 = 2
    stuff = []
    stuff.append(myItem)
    stuff.append(myItem2)
    print(stuff)
