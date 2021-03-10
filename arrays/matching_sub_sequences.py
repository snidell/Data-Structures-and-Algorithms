# This problem is similar to match the number of matching subsequences
# however instead of returning the number we want to return the actual subsequences

import collections

# seq is the sequence we are trying to match
# index is the current index
# size is the total size of the sequence. used to know when we are done
Sub = collections.namedtuple('Sub',('seq','index','size'))

class Sequence:
    def __init__(self,sequence):
        self.seq = sequence
        self.index = 0
        self.size = len(sequence)

class Solution:

    def numMatchingSubseq(self, S, words):
        waiting = collections.defaultdict(list)
        # load up the dictionary {'a':('acd',0,2)}
        def update_sequence(seq):
            seq.index+= 1
            return seq
        for word in words:
            sub = Sequence(word)
            waiting[word[0]].append(sub)

        

        for c in S:
            for seq in waiting.pop(c, ()):
                updated_seq = update_sequence(seq)
                if updated_seq.index == updated_seq.size:
                    waiting[None].append(updated_seq.seq)
                else:
                    waiting[updated_seq.seq[updated_seq.index]].append(updated_seq)
        return waiting[None]




if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.numMatchingSubseq("abcde",["a","bb","acd","ace"]))
