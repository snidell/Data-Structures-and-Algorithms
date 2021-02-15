# 16.7 BUILDING A SEARCH INDEX FOR DOMAINS

from typing import List, Set

class Solution:
    def decompose_into_dictionary_words(self,domain: str ,dictionary: Set[str]) -> List[str]:
        #When the algorithm finishes, last_length[i] != -1 indicates domain[:i +
        # 1] has a valid decomposition, and the length of the last string in the
        #decomposition is last_length[i].

        last_length = [-1] * len(domain)
        for i in range(len(domain)):
            #If domain[:i + 1] is a dictionary word, set last_length[i] to the # length of that word.
            if domain[:i + 1] in dictionary:
                last_length[i] = i + 1
                continue
            # If domain[:i + l] is not a dictionary word, we look for j < i such
            # that domain[: j + l] has a valid decomposition and domain[j + l;i + l] # is a dictionary ward. If SO, record the length of that word in
            # last_length [i].
            for j in range(i):
                if last_length[j] != -1 and domain[j + 1:i + 1] in dictionary:
                    last_length[i] = i - j
                    break

        decompositions = []
        if last_length[-1] != -1:
            # domain can be assembled by dictionary words.
            idx = len(domain) - 1
            while idx >= 0:
                decompositions.append(domain[idx + 1 - last_length[idx]:idx + 1])
                idx -= last_length[idx]
            decompositions= decompositions[: :-1]
        return decompositions


if __name__ =="__main__":
    mySolution = Solution()
    myString = "bedbathandbeyond"
    myDictionary = ["bed","bath","bat","beyond","and","hand","six","twenty"]
    print(mySolution.decompose_into_dictionary_words(myString,myDictionary))
    # doesnt really work returns ['bed', 'bat', 'hand', 'beyond']
    # should return ['bed', 'bat', 'bath','and','hand', 'beyond']
