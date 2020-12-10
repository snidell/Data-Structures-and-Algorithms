import functools
import itertools
import operator
import math

class Solution:
    # any() takes O(n) time
    def testAny(self):
        listOne = [True,True,False]
        listTwo = ["left","right","center"]
        listThree = [1,2,3,4,0]
        print(any(listOne))
        print(any(listTwo))
        print(any(listThree))
    # all() takes O(N) time
    def testAll(self):
        listOne = [True,True,False]
        listTwo = ["left","right","center"]
        listThree = [1,2,3,4,5,0]
        print(all(listOne))
        print(all(listTwo))
        print(all(listThree))
    def testFalsey(self):
        print("Falsey values")
        print(bool(0),"bool(0)") #zero value
        print(bool([]),"bool([])") # empty list
        print(bool(()),"bool(())") #empty tuple
        print(bool({}),"bool({})") # empty dict
        print(bool(set()),"bool(set())") # empty set
        print(bool(""),"bool("")") # empty string
        print(bool(range(0)),"bool(range(0))") # range of zero
        print(bool(0.0),"bool(0.0)") # zero float
        print(bool(None),"bool(None)") #keyword None
        print(bool(False),"bool(False)")# False is...False =)
    # map can uses a function and a iterable and applies the
    # function to each member of the iterable
    def testMap(self):
        myList = [1,2,3,4,5,6]
        myList2 = [0,6,5,4,3,2,1]

        result = map(lambda x: x+x,myList)
        # maps are lazily evaluated so the values are computed on demand,
        # thus we have to add list(myMap) to make it printable
        print(list(result),"result = map(lambda x: x+x,myList)")
        result2 = map(lambda x,y:x+y,myList,myList2)
        print(list(result2),"result2 = map(lambda x,y:x+y,myList,myList2)")

    def testReduce(self):
        myList = [1,2,3,4,5,6,7,0]
        myList2 = [0,9,8,7,6,5,4,3,2]

        total = functools.reduce(lambda a,b:a+b,myList)
        max = functools.reduce(lambda a,b: a if a>b else b,myList2)
        max = functools.reduce(lambda a,b: a if a>b else b,myList2)
        print(total, "functools.reduce(lambda a,b: a+b, myList)")
        print(max,"functools.reduce(lambda a,b:a if a>b else b,myList2)")
    # zip maps similar index of multiple containers
    def testZip(self):
        myList = [1,2,3,4,5]
        myList2=[10,20,30,40,50]
        myList3 = [1,2,3,4,5,6,7,8,9,10]
        myList4 = ["scott","heather","Holly","Eric"]

        # map multiple lists to a map
        myMap = zip(myList4,myList,myList2)
        # a list of lists
        print(list(myMap))
        # a set of lists
        print(set(myMap))

        # loop through multiple containers
        for pl, sc in zip(myList4,myList2):
            print(pl," scored an amount of ",sc)

        # zip will by default only go to the shortest list length
        for pl, sc in zip(myList4,myList3):
            print(pl," scored an amount of ",sc)
        # works on multiple iterators
        for pl, sc, sc2 in zip(myList3, myList4, myList):
            print(pl," scored an amount of ",sc," more scores ",sc2)

    def testEnumerate(self):
        myList = ["scott","heather","holly","eric"]
        obj1 = enumerate(myList)
        # printing enumerate object as list
        print(list(obj1))

        for item in enumerate(myList):
            print(item)

        for idx,name in enumerate(myList):
            print("index: ",idx," name:",name)
    # groups by must be sorted
    def testGroupBy(self):
        things = [("animal", "bear"), ("animal", "duck"),("vehicle", "speed boat"), ("plant", "cactus"),  ("vehicle", "school bus")]
        for key, group in itertools.groupby(things, lambda x: x[0]):
            for thing in group:
                print("A %s is a %s." % (thing[1], key))
                print("")

        # for unsorted it groups consecutive occurences
        for key,group in itertools.groupby("BCAACACAADBBB",None):
            print("key: ",key,"group: ",list(group))
        print("----------")
        # for sorted it groups all occurences of a item
        for key,group in itertools.groupby(sorted("BCAACACAADBBB"),None):
            myGroup = list(group)
            print("key: ",key,"group: ",myGroup,"number: ",len(myGroup))

    def testAccumulate(self):
        #accumulates the reults of the pervious operands in a list
        myList = [1,2,3,4,5,6,7]
        mulAccumulate = itertools.accumulate(myList,operator.mul)
        print(list(mulAccumulate))

    def testProduct(self):
        arr = [1,2,3,4,5]
        arr2 = [6,7,8,9]

        print(list(itertools.product(arr,arr2)))

        myProduct = itertools.product(arr,arr2)
        for item in myProduct:
            print(item[0],"then item 1 ",item[1])

    def testCombinations(self):
        # combinations() helps  in permutaiton, combination, and cartesian product problems
        # get the number of combinations of GeEKS of size 3
        myString = "GeEKS"
        print(list(itertools.combinations(myString,3)))

        print ("All the combination of list in sorted order(without replacement) is:")
        print(list(itertools.combinations(['A', 2], 2)))
        print()

        print ("All the combination of string in sorted order(without replacement) is:")
        print(list(itertools.combinations('AB', 2)))
        print()

        print ("All the combination of list in sorted order(without replacement) is:")
        print(list(itertools.combinations(range(2), 1)))
def count_bits(x:int)->int:
    # bits = 0
    # while x:
    #     print(x)
    #     bits += 1
    #     x >> bits
    # return bits
    num_bits = 0
    while x:
        num_bits += 1
        x >>= 1
    return num_bits
def play_bits():
    print(10>>2)
    print(10<<4)
    print(-10<<4)
    print(-10>>2)

def play_math(x: float, y:int):
    print(max(10,x),"max of 10 and x")
    print(min(10,x),"min of 10 and x")
    print(pow(x,y),"exponent")
    print(x**y, "exponent")
    print(math.floor(y),"floor of y")
    print(math.ceil(y),"ceil of y")
    print(math.sqrt(255),"sqrt of 255")
def play_conversion(x:int,y:str):
    print("string to int",int(y))
    print("int to string",str(x))
    print("int to float: ",float(x))

def play_infinite():
    # unlike ints floats are not infinte percision use 'inf' and -'inf' for boundaries
    print(float("inf"))
    print(float("-inf"))
    print(float("-inf")>10,"float(\"-inf\")>10")
    print(float("inf")>10,"float(\"inf\")>10")

if __name__ =="__main__":
    mySolution = Solution()
    mySolution.testAny()
    print("----------")
    mySolution.testAll()
    print("----------")
    mySolution.testFalsey()
    print("----------")
    mySolution.testMap()
    print("----------")
    mySolution.testReduce()
    print("----------")
    mySolution.testZip()
    print("----------")
    mySolution.testEnumerate()
    print("----------")
    mySolution.testGroupBy()
    print("----------")
    mySolution.testAccumulate()
    print("----------")
    mySolution.testProduct()
    print("----------")
    mySolution.testCombinations()
    print("----------")
    print(count_bits(12))
    play_bits()
    play_math(14,29.333)
    play_conversion(22,"36")
    play_infinite()
