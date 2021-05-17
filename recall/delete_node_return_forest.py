
from typing import List

class Solution:
    def delete_node(self,root,to_delete:List[int]):
        # create a set out of the list for faster access
        result = []
        to_delete_set = set(to_delete)

        def walk(node, parent_exists):
            if not node:
                return None
            if node in to_delete_set:
                walk(node.left,False)
                walk(node.right,False)
            if not parent_exists:
                result.append(node)

            walk(node.left,True)
            walk(node.right,True)

            return node

        walk(root,False)




if __name__ =="__main__":
    mySolution = Solution()
