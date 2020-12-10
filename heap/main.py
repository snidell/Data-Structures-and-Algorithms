import heapq

if __name__ =="__main__":
    # random list of numbers
    myArray =[5,6,3,2,1,1,22]
    heapq.heappush(myArray,78)
    print(myArray)
    heapq.heappop(myArray)
    print(myArray)
    heapq.heapify(myArray)
    print(myArray)
    #get largest
    print(heapq.nlargest(1,myArray))
    print(heapq.nsmallest(1,myArray))
