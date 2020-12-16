class Singleton(object):
    _singletons = {}
    def __new__(cls):
        if not cls._singletons.keys():            #若还没有任何实例
            cls._singletons[cls] = object.__new__(cls)  #生成一个实例
        return cls._singletons[cls]                             #返回这个实例


a = Singleton()
b = Singleton()
print(id(a))
print(id(b))

