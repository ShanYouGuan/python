def insertSort(relist):
    len_ = len(relist)
    for i in range(1,len_):
        for j in range(i):
            if relist[i] < relist[j]:
                relist.insert(j, relist[i])
                relist.pop(i+1)
                break
    return relist


print(insertSort([1,6,3,5,4]))
A = [1,3,5]
A.pop(0)
print(A)