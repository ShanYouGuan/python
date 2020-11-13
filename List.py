"""a = [66.25, 333, 333, 1, 1234.5]
a.insert(1,-1)
a.append(333)
print("尾插：",a)
a.reverse()#倒排
print("倒排：",a)
a.sort()
print("升序排列：",a)
b = [(x,y) for x in range(4) for y in range(6) if x!= y ]
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
for row in matrix:
    print(row)
c = list(zip(*matrix))
print(c)
d = dict([('name','jack'), ('age', 16)])
e = dict(name='jack', age=17 )
print(d.keys())
print(d)
print(e)
for k,v in d.items():
    print(k, v)
for k,v in enumerate(d):
    print(k,v)
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3
print(non_null)"""
for x in range(1,11):
    #print(repr(x).rjust(2),repr(x*x).rjust(3),repr(x**3).rjust(4))
    #print(repr(x).rjust(4,'*'), repr(x * x).rjust(4), repr(x ** 4).rjust(5))
    print('{0:3d},{1:3},{2:4}'.format(x, x**2, x**3))
print("my name is {}".format("jack"))
print()