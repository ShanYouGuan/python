#输入三个整数x,y,z，请把这三个数由小到大输出。

arr = []
for i in range(3):
    num = int(input("input the number:"))
    arr.append(num)
print(sorted(arr))



