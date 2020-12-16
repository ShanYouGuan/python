class people:
    name = ""
    age = 0
    __weigt = 0
    def __init__(self,a, n, w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak1(self):
        print("{}说：我今年{}岁，我{}斤".format(self.name, self.age,self.__weight))
class student(people):
    grade = ''
    def __init__(self,n, a, w, g):
        people.__init__(self,a, n, w)
        self.grade = g
    def speak2(self):
        print("{}说：我{}岁了，我在读{}年级。".format(self.name, self.age, self.grade))
class speaker:
    topic = ''
    name = ''
    def __init__(self,n, t):
        self.name = n
        self.topic = t
    def speak3(self):
        print("我叫{},我是演说家,我演讲的题目是{}".format(self.name, self.topic))
class sampe(student, speaker,people):
    def __init__(self,n, a, w, g, t):
        student.__init__(self,n, a, w, g)
        speaker.__init__(self,n, t)
    pass
tmp = sampe('tim',10,100,8, "Lovely")
tmp.speak1()
tmp.speak2()
tmp.speak3()