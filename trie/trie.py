from node import Node
class Trie:

    def __init__(self):
        self.root = self.get_node()
    def get_node(self):
        return Node()
    def get_index(self,ch):
        return ord(ch) - ord('a')
    def insert(self,word):
        root = self.root
        len1 = len(word)

        for i in range (len1):
            index = word[i]

            if index not in root.children:
                root.children[index] = self.get_node()
            root =  root.children.get(index)

        return True if root and root.terminating else False
    def search(self,word):
        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = word[i]
            if not root:
                return False
            root = root.children.get(index)
        return True if root and root.terminating else False
