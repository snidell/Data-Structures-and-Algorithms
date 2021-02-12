# 5.1 THE TOWERS OF HANOI PROBLEM

# A peg contains rings in sorted order, with the largest ring being the lowest.
# You are to transfer these rings to another peg, which is initially empty.

# Hint: If you know how to transfer the top n - 1 rings, how does that help move
# the nth ring?

class Solution:
    def towers_of_hanoi(self,n , source, destination, auxiliary):
        if n==1:
            print("Move disk 1 from source",source,"to destination",destination)
            return
        self.towers_of_hanoi(n-1, source, auxiliary, destination)
        print ("Move disk",n,"from source",source,"to destination",destination)
        self.towers_of_hanoi(n-1, auxiliary, destination, source)


if __name__ =="__main__":
    mySolution = Solution()
    print("move tower from A to B")
    mySolution.towers_of_hanoi(4,'A','B','C')
    # Move disk 1 from source A to destination C
    # Move disk 2 from source A to destination B
    # Move disk 1 from source C to destination B
    # Move disk 3 from source A to destination C
    # Move disk 1 from source B to destination A
    # Move disk 2 from source B to destination C
    # Move disk 1 from source A to destination C
    # Move disk 4 from source A to destination B
    # Move disk 1 from source C to destination B
    # Move disk 2 from source C to destination A
    # Move disk 1 from source B to destination A
    # Move disk 3 from source C to destination B
    # Move disk 1 from source A to destination C
    # Move disk 2 from source A to destination B
    # Move disk 1 from source C to destination B
