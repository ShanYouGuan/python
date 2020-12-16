def binarySearch(array, left, right, x):
    if right > 1:
        mid = int((left + right)/2)
        if x == mid:
            return array.index(mid)+1
        if x > mid:
            return binarySearch(array, mid+1, right, x)
        if x < mid:
            return binarySearch(array, left, mid-1, x)
    else:
        print("The list is not Exit")



list1 = [1, 3, 4, 5, 8, 10, 13, 14, 15]
left = 0
right = len(list1)-1
x = 5
result = binarySearch(list1, left, right, x)
print('the index is ', result)