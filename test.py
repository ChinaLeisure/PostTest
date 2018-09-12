
class Student():
    pass
#对象
mingyue = Student()
class PythonStudent():
    name = None
    age = 18
    course = "python"
    def doHomework(self):
        print("我在做作业")
        #在函数末尾使用return语句
        return None
    #实例化一个叫yueyue的学生
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
#注意成员函数的调用没有传递进入参数
yueyue.doHomework()