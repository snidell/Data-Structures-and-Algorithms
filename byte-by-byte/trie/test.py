class TrieNode:
    def __init__(self):
        self.children = defaultdict()
        self.terminating = False

class Trie:

    def __init__(self):
        self.root = self.get_Node()
    def get_Node(self):
        return TrieNode()
    def insert(self,word):
        currentNode= self.root

        for i in range(len(word)):
            if word[i] not in currentNode.children
                currentNode.children[word[i]] = self.get_Node()
                #move to next node
            currentNode = currentNode.children.get(word[i])

        #Done with letters terminate nodes
        currentNode.terminate = True
    def search(self,word):
        currentNode = self.root

        for i in range(len(word)):
            if not currentNode
                return False
            currentNode = currentNode.children.get(word[i])

        return True currentNode and currentNode.terminating else False



    f __name__ == "__main__":

        strings = ["pqrs", "fu'Clan", "psst", "qqrs", "pqrs"]

        t = Trie()
        for word in strings:
            t.insert(word)

        print(t.search("pqrs"))
        print(t.search("pprt"))
        print(t.search("fu'Clan"))

        t.delete("pprt")

        print(t.search("pprt"))
