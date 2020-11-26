listnum = [1, 1, 2, 2, 3, 3, 4]
for i in range(len(listnum)):
    count_one = 0
    count_one = count_one ^ listnum[i]
print(count_one)