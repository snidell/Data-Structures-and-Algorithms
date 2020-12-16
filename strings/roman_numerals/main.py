# 6.8 CONVERT FROM ROMAN TO DECIMAL
# The Roman numeral representation of positive integers uses the symbols
# I, V, X, L, C. D, M. Each symbol represents a value, with I being 1,
# V being 5, X being 10, L being 50, C being 100, D being 500, and M being 1000.

# Valid Roman number string if symbols appear in nonincreasing order,
# with the following exceptions allowed:
# • I can immediately precede V and X.
# • X can immediately precede L and C.
# • C can immediately precede D and M.
class Solution:
    def roman_to_integer(self,s)->int:
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            # if its not the first number and the preceeding digit is not greater than current addd
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                # why 2 * ? we already added this value to the result in the
                # previous step so we need to account for that value plus the
                # current value being removed
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                # if its not the first number or an preceeding case  just add
                int_val += rom_val[s[i]]
        return int_val




if __name__ == "__main__":
    mySolution = Solution()
    print(mySolution.roman_to_integer("MCLXLIV"))
