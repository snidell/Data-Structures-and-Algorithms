# 16.5 SEARCH FOR A SEQUENCE IN A 2D ARRAY
# Write a program that takes as arguments a 20 array and a 10 array, and checks
# whether the 10 array occurs in the 20 array.
# Hint: Start with length 1 prefixes of the 10 array, then move on to length
# 2,3,. .. prefixes.

class Solution:
    def search_grid(self,grid:List[List[int]],pattern: List[int])-> bool:
        
