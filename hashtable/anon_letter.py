# 12.2 Is AN ANONYMOUS LEITER CONSTRUCTIBLE?
# Write a program which takes text for an anonymous letter and text for a
# magazine and determines if it is possible to write the anonymous letter using
# the magazine. The anonymous letter can be written using the magazine if for
# each character in the anonymous letter, the number of times it appears in the
# anonymous letter is no more than the number of times it appears in the magazine.
#
# Hint: Count the number of distinct characters appearing in the letter.

import collections

class Solution:
    # letter -> string we need to construct
    # mag -> word bank we can use to construct the letter
    # Therefore, the time complexity is O(m + n) where m and n are the number
    # of characters in the letter and magazine, respectively. The space
    # complexity is the size of the hash table constructed in the pass over the
    # letter, i.e.,
    # O(L), where Lis the number of distinct characters appearing in the letter.
    def is_letter_constructable(self,letter:str,mag:str) -> bool:
        # compute letter frequency
        char_frequency = collections.Counter(letter)

        # check if characters in magazine can cover the letter
        for c in mag:
            if c in char_frequency:
                char_frequency[c] -= 1
                if char_frequency[c] ==0:
                    del char_frequency[c]
                if not char_frequency:
                    return True
        print(char_frequency)
        return not char_frequency


if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.is_letter_constructable("abbcd","abacd"))
