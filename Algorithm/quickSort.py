def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pro = array[0]
        less = [i for i in array[1:] if i < pro]
        gender = [j for j in array[1:] if j >= pro]
        return quicksort(less)+[pro]+quicksort(gender)


print(quicksort([1, 3, 5, 6, 4, 8]))