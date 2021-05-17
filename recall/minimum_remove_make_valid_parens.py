
class Solution:
    def min_remove_valid_parens(self,s:str)->str:
        indexes_to_remove = set()
        stack = []
        for idx,letter in enumerate(s):
            if letter in "()":
                if letter =="(":
                    stack.append(idx)
                if letter ==")":
                    if stack:
                        stack.pop()
                    else:
                        indexes_to_remove.add(idx)
        # join the indexes together
        indexes_to_remove = indexes_to_remove.union(set(stack))
        string_builder = []
        for idx,letter in enumerate(s):
            if idx not in indexes_to_remove:
                string_builder.append(letter)

        return "".join(string_builder)



if __name__ =="__main__":
    mySolution = Solution()
    s1 = "lee(t(c)o)de)"
    s2 = "a)b(c)d"
    s3 = "))(("

    print(mySolution.min_remove_valid_parens(s3))
