#Description: Design and implement a data structure for Least Recently Used (LRU) cache.
#It should support the following operations: get and put.
#get(key) - Get the value (will always be positive) of the key if the key exists
# in the cache, otherwise return -1.
#put(key, value) - Set or insert the value if the key is not already present.
#When the cache reached its capacity, it should invalidate the least recently
#used item before inserting a new item.

#Problem Link: https://leetcode.com/problems/lru-cache/
#solution:https://www.youtube.com/watch?v=NDpwj0VWz1U
from collections import defaultdict

class Node:
    def __init__(self,value=0):
        self.previous = None
        self.next = None
        self.value = value

class LRUcache:
    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.first.previous = self.last
        self.last.next = self.first
        self.last.prvious = self.first
        self.map = defaultdict()
        self.capacity = 0
        self.maxCap = 3
    def get(self,value):
        if value in self.map:
            node = self.map[value]
            #update position in cache
            self.removeNode(node)
            self.addNode(node)
        else:
            return None
    def put(self,value):
        #if we have the item already, just update the position in the linkedList
        if value in self.map:
            node = self.map.get(value)
            self.removeNode(node)
            self.addNode(node)
        #if we don't have the value
        else:
            #if the capcity is reach evict least Used
            if self.capacity >= self.maxCap:
                #get the previous node from the tail node.
                #This marks the 'least used' value
                removedNode = self.last.previous
                keyToRemove =  removedNode.value
                self.removeNode(removedNode)
                self.map.pop(keyToRemove)
                self.capacity-=1
            #create a new node and value and both to map
            newNode = Node(value)
            self.map[value]=newNode
            self.addNode(newNode)
            self.capacity+=1

    #add node value to Doubly linked list at the head
    def addNode(self,node):
        #add new node to head
        next_node = self.first.next
        self.first.next = node
        node.previous = self.first
        node.next = next_node
        next_node.previous = node
    def removeNode(self,node):
        next_node = node.next
        previous_node = node.previous

        next_node.previous = previous_node
        previous_node.next = next_node
    def print(self):
        next = self.first.next
        for i in range(self.capacity):
            print(next.value," ->",end=" ")
            next = next.next
        print("")
        for x in self.map:
            print(x,":",self.map[x])

def main():
    cache = LRUcache()
    cache.put(4)
    cache.put(4)
    cache.print()
    cache.put(4)
    cache.put(4)
    cache.put(4)
    cache.put(5)
    cache.print()
    cache.put(7)
    cache.print()
    cache.put(7)
    cache.put(8)
    cache.put(9)
    cache.print()


if __name__ =="__main__":
    main()
