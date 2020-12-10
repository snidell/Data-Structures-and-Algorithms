
class Solution:
    # time complexity is O(n)
    def dutch_flag(self,pivot_index: int,A: [int])->None:
        pivot = A[pivot_index]
        smaller = 0
        # first pass group smaller elements
        for i in range(len(A)):
            if A[i] < pivot:
                A[i],A[smaller] = A[smaller],A[i]
                smaller +=1
        #second pass group larger elements then pivot
        larger = len(A) - 1
        for i in reversed(range(len(A))):
            if A[i] >pivot:
                A[i], A[larger] = A[larger], A[i]
                larger -= 1
        print(A)


# Because for [0,1,0,1,1,2,2], all values less than the pivot come before all
# values equal to the pivot. The order of 1's and 0's doesn't matter, as long
# as none come after any 2's. Same idea for [0,0,1,2,2,1,1] - the pivot is 0,
# and all the 0's come before all the 1's and 2's - after that, it doesn't
# matter what order the 1's and 2's are in.

if __name__ =="__main__":
    mySolution = Solution()
    A = [0,1,2,0,2,1,1]
    mySolution.dutch_flag(0,A)
