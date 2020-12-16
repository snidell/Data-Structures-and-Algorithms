# 6.10 WRITE A STRING SINUSOIDALLY

# Define the snakestring of s to be the left-right top-to-bottom sequence
# in which characters appear whensiswritteninsinusoidalfashion.
# For example, the snake string string for "Hello_World!" is "e_lHloWrdlo!".
class Solution:
    def snake_string(self,s: str) -> str:
        row1,row2,row3 = [], [],[]
        # Outputs the first row, i.e., s[l], s[S], s[9], ...
        for i in range(1, len(s),4):
           row1.append(s[i])

        print(row1)

        for i in range(0,len(s),2):
            row2.append(s[i])

        print(row2)

        for i in range(3,len(s),4):
            row3.append(s[i])

        print(row3)

        return ''.join(row1+row2+row3)


if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.snake_string("Hello_World!"))
