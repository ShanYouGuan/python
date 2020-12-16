def merge(left, right):
    relist = []
    while left and right:
        relist.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
    while left:
        relist.append(left.pop(0))
    while right:
        relist.append(right.pop(0))
    return relist


def mergesort(list_):
    if len(list_) < 2:
        return list_
    len_ = len(list_)
    min_index = len_//2
    left = mergesort(list_[:min_index])
    right = mergesort(list_[min_index:])
    return merge(left, right)


print(mergesort([2, 5, 3, 6, 9, 0, 1]))
a = [1,2,3]
print(a.pop())