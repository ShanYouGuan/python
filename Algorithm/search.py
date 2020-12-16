def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            print("The index is {0}".format(i))
        else:
            pass


list1 = ['A', 'B', 'C', 'D', 'E']
x = 'B'
search(list1, x)
