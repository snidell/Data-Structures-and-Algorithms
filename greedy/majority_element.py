# 17.5 FIND THE MAJORITY ELEMENT
# You are reading a sequence of strings. You know apriori that more than half the
# strings are repetitions of a single string (the "majority element") but the
# positions where the majority element occurs are unknown. Write a program that
# makes a single pass over the sequence and identifies the majority element. For
# example, if the input is (b,a, c, a, a, b,a, a, c,a), then a is the majority
# element (it appears in 6 out of the 10 places).

# Hint: Take advantage of the existence of a majority element to perform
# elimination.

from typing import Iterator

class Solution:
    # time complexity O(n)
    # Space complexity O(1)
    def majority_search(self, stream:Iterator[str])->str:
        candidate_count = 0

        for it in stream:
            if candidate_count == 0:
                candidate, candidate_count = it, candidate_count + 1
            elif candidate == it:
                candidate_count += 1
            else:
                candidate_count -= 1
        return candidate




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.majority_search(['b','a','c','a','j','b','a','a','c','a']))
