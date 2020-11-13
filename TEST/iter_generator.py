# -*- coding: utf-8 -*-
__author__ = 'Guanshanyou'
'''list_a = [1, 3, 5, 7, 10]
list_b = iter(list_a)
print(list_b)
print(next(list_b))'''


'''def generator(Arry):
     for i in Arry:
          yield (i)

if __name__ == '__main__':
     gen = generator([3, 4, 5, 6, 7, 9])
     print(type(gen))'''

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res:",res)
g = foo()
print(next(g))
print("*"*20)
print(next(g))
