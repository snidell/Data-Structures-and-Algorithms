class Solution:

    def test_method(self,a):
        cache = {'a':[0,'b'],'b':[1,'c'],'c':2,'z':26}
        print("cache output",cache[a])
        if a =='z':
            print('a')
        else:
            intvalue = ord('a') - ord(a) +1
            intvalue +=1
            print(intvalue)

            print(chr(ord(a)+1))




if __name__ =="__main__":
    mySoltuion = Solution()
    mySoltuion.test_method('z')
