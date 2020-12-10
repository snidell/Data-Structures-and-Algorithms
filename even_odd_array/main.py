import bisect
import copy
class Solution:
    def even_odd_array(self,A:[int])->None:
        # set initial bounds
        next_even,next_odd = 0,len(A)-1
        while next_even < next_odd:
            if A[next_even] % 2 ==0:
                next_even+= 1
            else:
                A[next_even],A[next_odd] = A[next_odd],A[next_even]
                next_odd-=1

        print(A)

    def basic(self):
        # basic operators of an array/list
        A =[5,4,3,2,1] # instantiate 1d array
        B =[[5,4,3,2,1],[4,5],[6,7,8,9000]]
        print (len(A))
        A.append(42)
        print(A)
        A.remove(2) # remove the number 2
        # A.remove(62) throws error 62 is not in the list
        print(A)
        A.insert(3,28) #insert 28 at index 3
        print(A)
        # create a 2d array
        C =[[None]*10] * 10
        print(C)

        # copying an array
        D = [5,4,3,2]
        E = [0,0,0,0,0]
        F = list(D) # copy in new space
        E=D # shallow copy E points t D
        print(E)
        D.insert(3,28)
        print(E) # D changes and E gets updated also
        print(F)
        print("min(A)",min(A))
        print("max(A)",max(A))
        G = [1,2,3,5]
        print(bisect.bisect(G,4))
        print(bisect.bisect_left(G,4))
        print(bisect.bisect_right(G,4))
        G.insert(3,4)
        print(bisect.bisect(G,4))
        print(bisect.bisect_left(G,4))
        print(bisect.bisect_right(G,4))
        print(A.reverse()) #reverse list in place
        print(reversed(A)) # provides reversed iterator
        print(A.sort()) # sorts list in place
        print(sorted(A)) # returns a copy
        del A[0]  #delete item at index zero
        print("del A[0]",A)
        del A[1:2]
        print("del A[1:2]",A)
        H = [1,2,3,4,5,6,7]
        print(H[0:6:2])
        test_list = [1, 4, 6, 7, 2]

        # printing original list
        print ("Original list : " + str(test_list))
        # slice takes 3 optional arguements start, stop , step

        test_list = test_list[3:] + test_list[:3]
        # Printing list after left rotate
        print ("List after left rotate by 3 : " + str(test_list))
        test_list = test_list[-3:] + test_list[:-3]

        # Printing after right rotate
        print ("List after right rotate by 3(back to original) : "
                                         + str(test_list))

        # example of copy
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [a, b]
        d = c

        print("copy examples")
        print("id(c) == id(d) d is the same object as c",id(c) == id(d))
        # True - d is the same object as c
        print("d[0] is the same object as c[0] id(c[0]) == id(d[0]",id(c[0]) == id(d[0]))
        # True - d[0] is the same object as c[0]

        d = copy.copy(c)

        print("d is now a new object id(c) == id(d)",id(c) == id(d))
        # False - d is now a new object
        print("d[0] is the same object as c[0] id(c[0]) == id(d[0])",id(c[0]) == id(d[0]) )
        # True - d[0] is the same object as c[0]

        d = copy.deepcopy(c)

        print("d is now a new object id(c) == id(d)",id(c) == id(d))
        # False - d is now a new object
        print("d[0] is now a new object id(c[0]) == id(d[0])",id(c[0]) == id(d[0]))
        # False - d[0] is now a new object


if __name__ == "__main__":
    mySolution = Solution()
    mySolution.even_odd_array([1,2,3,4,5,6,7,8,9])
    mySolution.basic()
