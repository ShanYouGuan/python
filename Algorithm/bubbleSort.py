def bubble_sort(List_1):
    for i in range(len(List_1)):
        flag = 0
        print("第%d趟排序" % (i+1))
        for j in range(len(List_1)-i-1):
            if List_1[j] > List_1[j+1]:
                List_1[j], List_1[j+1] = List_1[j+1], List_1[j]
                flag += 1

        if flag == 0:
            return List_1
    return List_1


print(bubble_sort([1, 6, 3, 2, 4]))
