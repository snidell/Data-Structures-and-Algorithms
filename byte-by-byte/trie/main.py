#https://medium.com/@info.gildacademy/a-simpler-way-to-implement-trie-data-structure-in-python-efa6a958a4f2
import heapq
from collections import defaultdict


class TrieNode():

    def __init__(self):
        self.children = defaultdict()
        self.terminating = False


class Trie():

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return TrieNode()

    def insert(self, word):
        currentNode = self.root
        #loop through word letter by letter
        for i in range(len(word)):
            #if the key doesn't exist in the children add the new node
            if word[i] not in currentNode.children:
                currentNode.children[word[i]] = self.get_node()
            #move to the next node
            currentNode = currentNode.children.get(word[i])
        #Once we are out of letters terminate this identifies the last letter in a word
        currentNode.terminating = True

    def search(self, word):
        currentNode = self.root
        #loop through word letter by letter
        for i in range(len(word)):
            #if we have run out of nodes return False
            if not currentNode:
                return False
            #move to the next node
            currentNode = currentNode.children.get(word[i])
        #If we are on the last node and that node is a temrinating node, we have found our word
        return True if currentNode and currentNode.terminating else False

    def delete(self, word):

        root = self.root
        len1 = len(word)

        for i in range(len1):
            index = word[i]

            if not root:
                print ("Word not found")
                return -1
            root = root.children.get(index)

        if not root:
            print ("Word not found")
            return -1
        else:
            root.terminating = False
            return 0

    def update(self, old_word, new_word):
        val = self.delete(old_word)
        if val == 0:
            self.insert(new_word)
    def print(self,currentNode=None):
        if currentNode is None:
            currentNode = self.root

        if len(currentNode.children) ==0:
            return

        for i in currentNode.children.keys():
            print(i,end="")
            self.print(currentNode.children.get(i))

    def list_words(self,currentNode = None):
        if currentNode is None:
            currentNode = self.root
        my_list = []
        for k,v in currentNode.children.items():
            print(k)
            for el in self.list_words(v):
                print("el=: "+k+el)
                my_list.append(k+el)
        return my_list



if __name__ == "__main__":
    listForTree = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    heapq.heapify(listForTree)             # for a min heap
    heapq._heapify_max(listForTree)        # for a maxheap!!
    print(listForTree)
    strings = ["Dad", "fu'Clan", "Mom", "Auntie", "Pops"]

    t = Trie()
    for word in strings:
        t.insert(word)
    #t.print()
    print(t.list_words())

    t.delete("pprt")

    print(t.search("pprt"))

    t.update("mnop", "pprt")
