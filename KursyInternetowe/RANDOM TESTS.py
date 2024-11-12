def find_even_index(arr):
    lList = []
    pList = []
                                                # sum og arr == 66
                                                # print(sum(arr))
    # half to left | half to right
    for i in range(len(arr)):
        if i < (int(len(arr))/2):
            lList.append(arr[i])
        else:
            pList.append(arr[i])

    print("1. ",lList)
    print("left list sum = ", sum(lList))
    print("\n2. ",pList)
    print("right list sum = ", sum(pList))



find_even_index([1,2,3,4,5,6,7,8,9,10,11])