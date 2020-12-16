#Question: Given an array of integers where each value 1 <= x <= len(array), write a
#function that finds all the duplicates in the array.
#https://www.byte-by-byte.com/findduplicates/?utm_source=optin_carrot&utm_medium=pdf&utm_campaign=50questions

def findDuplicates(items):
    resultSet = set()
    #Translate values into there relative indexs
    #example: if we have [1,2,3] --> [0,1,2]
    for i in range(len(items)):
        index = abs(items[i])-1
        #if we have seen this item it will be set to a negative number
        #if this is the first time we see it set the item to be a negative values#representation
        if(items[index] < 0):
            resultSet.add(abs(items[i]))
        else:
            items[index] = -items[index]

    return list(resultSet)



def main():
    arr1 = [1,2,3]
    arr2 = [1,2,3,3]
    arr3 = [2,1,2,1]
    print(findDuplicates(arr1))
    print(findDuplicates(arr2))
    print(findDuplicates(arr3))


if __name__ == "__main__":
    main()
