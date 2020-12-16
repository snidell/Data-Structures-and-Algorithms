# 6.6 REVERSE ALL TiiE WORDS IN A SENTENCE
# Given a string containing a set of words separated by whitespace, we would
# like to transform it to a string in which the words appear in the reverse order.
# For example, "Alice likes Bob" transforms to "Bob likes Alice". We do not
# need to keep the original string.
class Solution:
    def reverse_words(self, s):
        def reverse_range(s,start, finish):
            while start < finish:
                s[start], s[finish] = s[finish],s[start]
                start , finish = start + 1, finish -1

        #reverse the whole string first ram is costly --> yltsoc si mar
        reverse_range(s,0,len(s)-1)
        print(s)
        # reverse each letter of each word
        start, finish = 0, 0
        while True:
            if s[finish] == ' ':
                reverse_range(s,start,finish-1)
                start, finish = finish +1,finish +1
            finish += 1
            if finish ==len(s)-1:
                break
        # reverse last word
        reverse_range(s,start,finish)
        print(s)



if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.reverse_words(list("ram is costly")))
