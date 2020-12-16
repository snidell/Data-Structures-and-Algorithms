class Solution:
    def delete_duplicates(self,A:[int])-> int:
        if not A:
            return 0
        write_index = 1
        for i in range(1, len(A)):
            if A[write_index - 1] != A[i]:
                A[write_index] = A[i]
                write_index += 1
        print(A[:write_index])
        return write_index

if __name__ =="__main__":
    mySolution = Solution()
    A = [2,3,5,5,7,11,11,11,13]
    B = [1]
    C = [0,0,0,0,0,0,0]
    print(mySolution.delete_duplicates(A))
    print(mySolution.delete_duplicates(B))
    print(mySolution.delete_duplicates(C))
