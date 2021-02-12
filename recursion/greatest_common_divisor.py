# Intro
# The Euclidean algorithm for calculating the greatest common divisor (GCD) of
# two numbers is a classic example of recursion. The central idea is that if
# y > x, the GCD of x and y is the GCD of x and y- x. For example, GCD(156,36) =
# GCD((l56 -36) = 120,36). By extension, this implies that the GCD of x and y is
# the GCD of x and y mod x, i.e., GCD(156, 36) = GCD((156 mod 36) = 12, 36) =
# GCD(l2,36 mod 12 =0) =12.

# Time complexity is O(n) where n is the number of bits needed to represent the inputs
# Space complxity is O(n) which is the max depth of the function call
class Solution:
    def gcd(self,x:int,y:int)-> int:
        print("x: ",x," y: ",y)
        if y == 0:
            return x
        else:
            return self.gcd(y,x%y)

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.gcd(156,36))
