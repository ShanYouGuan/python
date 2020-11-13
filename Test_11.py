"""for num in range(2, 10):
    if num % 2 == 0:
       print("Found an even number", num)
       #continue#continue 的作用是执行到continue后返回循环而不执行下面的语句
       break
    print("Found a number", num)"""
"""a = list(map(lambda X: X**2,range(10)))
b = [(x, y) for x in range(1, 10) for y in range(1, 10) if x != y]
print(a)
print(b)
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
key=lambda pair: pair[1]
print(key)
pairs.sort(key=lambda pair: pair[1])
print(pairs)
def func(a):
    if a > 100:
        return True
    else:
        return False
aa = list(filter(func,[10,56,101,500]))
print (aa)
#res = filter(lambda x: x % 2 ==0, range(1, 10))
#print(list(res))
#res1 = map(lambda x: x**3, range(10))
#print(list(res))"""

"""def isLeapYear(y):
    return y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)


def ismonth(m):

    if 0 < m <= 12:
       pass
    else:
     m = int(input("输入不合法！！重新输入："))
    return m


res = 0
DoFm = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
year = int(input('Year:'))
month = int(input('Month:'))
month1 = ismonth(month)
day = int(input('day:'))
if isLeapYear(year):
    DoFm[2] += 1
for i in range(month1):
    res += DoFm[i]
print('This is {0}th in {1}'.format(res + day, year))"""
a = 10
b = 21
print(b//a)


