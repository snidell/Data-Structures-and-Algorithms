def solve(arr1,arr2):
    #base case we can take the max of index zero and max of index1
    print(arr1,arr2)
    if len(arr1) == 2:
        result = (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
        return result
    #if its even
    if len(arr1)%2 ==0:
        #length 4 gives index 1 and 2
        median1 = (arr1[(len(arr1)//2)-1]+arr1[(len(arr1)//2)])/2
        median2 = (arr2[(len(arr2)//2)-1]+arr2[(len(arr2)//2)])/2
        if median1>median2:
            #take left side of arr1
            #take right side of arr2
            return solve(arr1[:len(arr1)//2],arr2[len(arr2)//2:])
        else:
            #take right side of arr1
            #take left side of arr2
            return solve(arr1[len(arr1)//2:],arr2[:len(arr2)//2:])
    else:
        median1 = arr1[(len(arr1)//2)]
        median2 = arr2[(len(arr2)//2)]
        if median1>median2:
            #take left side of arr1
            #take right side of arr2
            return solve(arr1[:len(arr1)//2+1],arr2[len(arr2)//2:])
        else:
            #take right side of arr1
            #take left side of arr2
            return solve(arr1[len(arr1)//2:],arr2[:len(arr2)//2+1:])


def main():
    arr1 = [1,2,3,4,5,6,7]
    arr2 = [0,0,0,0,10,10,10]
    answer = solve(arr2,arr1)
    print(answer)

if __name__ == "__main__":
    main()
