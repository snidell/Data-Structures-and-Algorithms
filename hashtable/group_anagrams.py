from typing import List
import collections


class Solution:
    # Time Complexity: O(NK), where NN is the length of strs, and K is the
    # maximum length of a string in strs. Counting each string is linear in the
    # size of the string, and we count every string.

    # Space Complexity: O(NK)O(NK), the total information content stored in ans.
    def groupAnagrams(self,strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1

            print(count)
            ans[tuple(count)].append(string)
        return ans.values()



if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.groupAnagrams(["debitcard","elvis","silent","badcredit",
                                    "lives","freedom","listen","levis","money"]))
