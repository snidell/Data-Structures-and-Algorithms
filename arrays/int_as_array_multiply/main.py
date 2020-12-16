# 5.3 MULTIPLY TW"O ARBITRARY-PRECISION INTEGERS
class Solution:
    def multiply(self,num1:[int],num2:[int])->[int]:
        sign = -1 if (num1[0] <0) ^ (num2[0] < 0) else 1
        num1[0], num2[0] = abs(num1[0]),abs(num2[0])

        result = [0]*(len(num1)+len(num2))
        print(len(num1),len(num2))
        print(list(reversed(range(len(num1)))))
        print(list(range(len(num1))))
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                print("i+j+1",i,j,1)
                result[i+j+1] += num1[i] * num2[j]
                result[i+j] += result[i+j+1] // 10
                result[i+j+1] %= 10
                print("result",result)
        # remove leading zeros zeros
        # [0,2,3,4,8,2]
        # result[1:6]
        # list comprehension leading i here is needed for iteration
        # i for i, x in enumerate(result) if x !=0 --> get indices of non-zero numbers
        #next() the len(result) is the default for edge cases of 0000-> all
        # are zero an empty array is returned and or'ed with [0] which results
        #  in [0]
        result = result[next((i for i, x in enumerate(result)
                              if x != 0),len(result)):] or [0]
        return [sign * result[0]] + result[1:]


if __name__=="__main__":
    mySolution = Solution()
    A = [1,2,3]
    B = [5,6]
    print(mySolution.multiply(A,B))
