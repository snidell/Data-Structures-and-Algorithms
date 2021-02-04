# 12.8 Find the longest Subarray with distinct values

# Write a program that takes an array and returns the length of a longest
# subarray with the property that all its elements are distinct. For example, if
# the array is (f, s,f,e, t, w,e, n, w, e) then a longest subarray all of whose
# elements are distinct is (s,f,e, t, w).

from typing import List, Dict

class Solution:
    def longest_subarray_with_distinct_entries(self,A: List[int]) -> int:
            most_recent_occurence: Dict[int,int] = {}
            p = result = 0
            for i, a in enumerate(A):
                # A[i] appeared before?
                if a in most_recent_occurence:
                    dup_idx = most_recent_occurence[a]
                    # Did it appear in the longest current subarray ?
                    print("i: ",i," p: ",p," a:",a," dup_idx: ",dup_idx," result: ",result)
                    if dup_idx >= p:
                        # if the current span is bigger than our result update the result
                        result = max(result,i - p)
                        p = dup_idx + 1
                most_recent_occurence[a] = i

            # len(A) - p checks for a unique
            # array or a subarray thats longest that occurs at the end

            return max(result,len(A) - p)

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.longest_subarray_with_distinct_entries(
        ["1","2","1","3","1","2","1"]))
    # print(mySolution.longest_subarray_with_distinct_entries(
    #     ["0","1", "2", "1", "3", "1", "2", "1","4","5","6","0"]))
