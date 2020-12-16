from collections import defaultdict

def consecutive(arr1):
    #create Dictionary of numbers
    set = defaultdict()
    for i in range(len(arr1)):
        set[arr1[i]] = True

    maxLength = 0
    for i in range(len(arr1)):
        length = 1
        print(set.get(arr1[i]))
        j=1
        while set.get(arr1[i]+j):
            length+=1
            j+=1
        maxLength = max(maxLength,length)
    return maxLength





def main():
    arr1 = [-1,0,1,2,3,7,7,7,7,7,10]
    print(consecutive(arr1))
if __name__ == "__main__":
    main()
