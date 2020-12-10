class Solution:
    def plus_one(self,A: [int]) -> [int]:
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:
                break
            A[i] = 0
            A[i-1]+=1
        else: #else clause on the for loop tells us a break was found
            print("break!")
            if A[0] == 10:
                #There is a carry-out, so we need one more digit to store t
                # he result. #A slick way to do this is to append a @ at
                # the end of the array, #and update the first entry to 1.
                A[0] =1
                A. append(0)
        return A


if __name__ =="__main__":
    mySolution = Solution()
    A = [1,2,3]
    print(mySolution.plus_one(A))
    B =[9,9]
    print(mySolution.plus_one(B))
    C =[9,9,9,9,9,9,9,9,9]
    print(mySolution.plus_one(C))
