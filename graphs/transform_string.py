# 18.7 TRANSFORM ONE STRING TO ANOTHER

# Lets and t be strings and D a dictionary, i.e., a set of strings. Defines to
# produce t if there exists a sequence of strings from the dictionary
# P = (s0, s1, . . . , sn.1) such thatthe first string is s, the last string is
# t, and adjacent strings have the same length and differ in exactly one
# character. The sequence Pis called a production sequence. For example, if the
# dictionary is {bat, cot, dog, dag, dot, cat}, then (cat, cot, dot, dog) is
# production sequence.

# Given a dictionary D and two strings s and t, write a program to determine if s
# produces t. Assume that all characters are lowercase alphabets. If s does
# produce t, output the length of a shortest production sequence; otherwise,
# output -1.
#
# Hint: Treat strings as vertices in an undirected graph, with an edge between u
# and v if and only if the corresponding strings differ in one character.

from typing import Set
import collections
import string

class Solution:
    def transform_string(self,D: Set[str],s: str, t:str)->int:
        StringWithDistance = collections.namedtuple('StringWithDistance',('candidate_string','distance'))
        # use BFS to find the shortest path ie last amount of transforms
        q = collections.deque([StringWithDistance(s,0)])
        D.remove(s)

        while q:
            f = q.popleft()
            # return if we find a match
            if f.candidate_string == t:
                return f.distance #number of steps to reach t.

            # Tries all possible transformations of f.candidate_string
            for i in range(len(f.candidate_string)):
                # iterates through a-z
                for c in string.ascii_lowercase:
                    cand = f.candidate_string[:i] + c + f.candidate_string[i + 1:]
                    if cand in D:
                        D.remove(cand)
                        q.append(StringWithDistance(cand,f.distance +1))
        return -1 # Cannot find possible transform


if __name__ =="__main__":
    mySolution = Solution()
    myDictionary = set(["bat", "cot", "dog", "dag", "dot", "cat"])
    print("length of the shortest production sequence: ",mySolution.transform_string(myDictionary,"dog","cat"))
