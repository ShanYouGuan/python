num = 1
def fun1():
    #num = 2
    def fun2():
        num = 3
        print("fun2的num：%d"%num)
    fun2()
fun1()


