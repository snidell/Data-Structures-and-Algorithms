
import functools
class Solution:
    def string_hash(self,s: str, modulus: int) -> int:
        mult = 997
        return functools.reduce(lambda v, c: (v * mult + ord(c)) % modulus, s, 0)

if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.string_hash("1myString",27))
