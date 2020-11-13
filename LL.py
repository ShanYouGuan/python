import copy
'''a = [1, 2, 3, 4, ['a', 'b']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)
a.append(5)
a[4].append('c')
print(a)
print(b)
"删除"
'''

c = [4, 5, 6,['a','b']]
d = c
a1 = copy.copy(c)#相当于a的一个引用 a变a1变
a2 = copy.deepcopy(c) #相当于将a中的数据重新存入内存中a2指向它
c[3].append('c')
a1.append(7)
print(id(c))
print(id(d))
print(id(a1))
print(id(a2))
print(a2)
