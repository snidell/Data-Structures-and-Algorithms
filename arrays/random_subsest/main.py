#5.15 COMPUTE A RANDOM SUBSET
import random
class Solution():
    def random_subest(self,n:int,k:int)->[int]:
        changed_elements: Dict[int,int] = {}
        for i in range(k):
            # generate random number between i and n-1 inclusive
            rand_idx = random.randrange(i, n)
            rand_idx_mappped = changed_elements.get(rand_idx,rand_idx)
            i_mapped = changed_elements.get(i,i)
            changed_elements[rand_idx] = i_mapped
            changed_elements[i] = rand_idx_mappped
        return [changed_elements[i] for i in range(k)]
# what if we had really bad luck with randrange and ended up getting the same rand_idx multiple times?
# n: 20 and k = 10  and our random was always 10?
#
# keys in the hashmap would continue to slide to the next (i) resulting if __name__ == '__main__':
# our only random number and the times it has appeared
# {10: 0, 0: 10}
# {10: 1, 0: 10, 1: 0}
# {10: 2, 0: 10, 1: 0, 2: 1}
# {10: 3, 0: 10, 1: 0, 2: 1, 3: 2}
# {10: 4, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3}
# {10: 5, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4}
# {10: 6, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
# {10: 7, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6}
# {10: 8, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7}
# {10: 9, 0: 10, 1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8}

if __name__=="__main__":
    mySolution = Solution()
    print(mySolution.random_subest(20,10))
