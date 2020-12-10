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

if __name__=="__main__":
    mySolution = Solution()
    print(mySolution.random_subest(10,4))
