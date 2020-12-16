def bubble_sort(list):
    for i in range(0, len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


lista = [1, 3, 6, 5, 4, 2]
bubble_sort(lista)
for i in range(0, len(lista)):
    print(lista[i])