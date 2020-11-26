'''def scope_test():
    def do_local():
        spam = "local spam"
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
    def do_global():
        global spam
        spam = "global spam"
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)'''


'''    class Complex:
def __init__(self,realpart,imagpart):
        self.realpart= realpart
        self.imagpart= imagpart
x = Complex(5,6)
print(x.d, x.e)'''
'''class MyClass:
    """A simple example class"""
    i = 12345
def f(self):
        return 'hello world'
x = MyClass()
xf = x.f()'''
'''class Dog:

                # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
d.tricks                # unexpectedly shared by all dogs'''
"""class Employee:
    "所有员工的基类"
    Empcount = 0
    def __init__(self,name, salary):
        self.name = name
        self.salary = salary
        Employee.Empcount +=1
    def DisplayCount(self):
        print("Total Employee is {} ".format(Employee.Empcount))
    def DisplayEmployee(self):
        print("Name:",self.name,"Salary:",self.salary)
"""
class gradParent():
    gardParent = 200
    def __init__(self):
        self.__gradParent = 4
    def __gradParentCount(self,count):
       self.__gradParent = count
       print(self.__gradParent )
    def get(self):
        print("ss",self.__gradParent)
    #def gradParentMethod(self):
        ##print("调用祖父类方法")
    #def gradParentsetAttr(self,attr):
       # gradParent.attr = gradParent
   # def gradParentgetAttr(self):
        #print("祖父类属性：%d" % gradParent.gardParent)
    def getprivategradParent(self,count):
        self.__gradParentCount(count)
class Child(gradParent):  # 定义子类
    def __init__(self):
     print("English_txt")
    def childMethod(self):
        print('调用子类方法')
if __name__ == "__main__":
    c2 = Child()
    c2.getprivategradParent(13)
    c2.get()
