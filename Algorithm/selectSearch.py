def selectSort(relist):
    for i in range(len(relist)):
        for j in range(len(relist)-i):
            if relist[i] > relist[i+j]:
                relist[i],relist[i+j] = relist[i+j],relist[i]
    return relist


print (selectSort([1,5,2,6,9,3]))