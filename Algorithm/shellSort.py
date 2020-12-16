def shell_sort(relist):
    n = len(relist)
    gap = n // 2 # 初始步长

    while gap > 0:
        for i in range(gap, n):
            temp = relist[i]  # 每个步长进行插入排序
            j = i
            # 插入排序
            while j >= gap and relist[j - gap] > temp:
                relist[j] = relist[j - gap]
                j -= gap
            relist[j] = temp

        gap = gap // 2  # 得到新的步长

    return relist


print(shell_sort([1, 9, 2, 6, 5, 3]))