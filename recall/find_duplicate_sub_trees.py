class Solution:
    def find_duplicate_subtrees(self,root):
        # declare map to store unique tree key
        if not root:
            return
        self.node_map = {}
        # recurse by using preorder traversal
        # create key value pair by concatenating node-left-right as key
        self.result = []
        self.recurse(root)
        def traverse(node):
            if node:
                ls = str(node.val)+ "-"+self.preorder(node.left)+'-'+self.preorder(node.right)
                count = self.node_map.get(ls,0)
                if count ==1:
                    result.append(node)
                self.node_map[ls] += 1
                return ls
            return '#'
