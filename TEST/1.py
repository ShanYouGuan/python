# def counter(cls):
#     obj_list = []
#     def wrapper(*args, **kwargs):
#         new_obj = cls(*args, **kwargs)
#         obj_list.append(new_obj)
#         print ("class:%s'object number is %d" % (cls.__name__, len(obj_list)))
#         return new_obj
#     return wrapper
#
# @counter
# class my_cls(object):
#     STATIC_MEM = 'This is a static member of my_cls'
#     def __init__(self, *args, **kwargs):
#         print (self, args, kwargs)
#         print (my_cls.STATIC_MEM)
#
#
# my_cls(1,2, key = 'shijun')
import functools
import time
def timing(status='Train'):
    print('this is timing')
    def dec(func):
        print('this is dec in timing')
        @functools.wraps(func)
        def wrapper3(*args,**kwargs):
            start = time.time()
            func1 = func(*args,**kwargs)
            print('[%s] time: %.3f s '%(status,time.time()-start))
            return func1
        return wrapper3
    return dec


def dec1(func):
    print('this is dec1')
    @functools.wraps(func)
    def wrapper1(*args,**kwargs):
        print('this is a wrapper in dec1')
        return func(*args,**kwargs)
    return wrapper1


def dec2(func):
    print('this is dec2')
    @functools.wraps(func)
    def wrapper2(*args,**kwargs):
        print('this is a wrapper in dec2')
        return func(*args,**kwargs)
    return wrapper2

@dec1
@dec2
@timing(status='Test')
def fun():
    time.sleep(2)

fun ()