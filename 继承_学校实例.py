#encoding:utf-8

class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []
        self.staffs = []
    def enroll(self, stu_obj):
        print("为学员%s 办理注册手续"% stu_obj.name)
        self.students.append(stu_obj)
    def hire(self, staff_obj):
        print('guyoong %s' % staff_obj.name)
        self.staffs.append(staff_obj)
class SchooMember(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def tell(self):
        pass

class Teacher(SchooMember):
    def __init__(self,name,age,sex,salary,course):
        super(Teacher,self).__init__(name,age,sex)
        self.salary = salary
        self.course = course
    def tell(self):
        print('''
        - - - info of Teacher:%s - - -
        Name:%s
        Age:%s
        Sex:%s
        Salary:%s
        Course:%s
        '''%(self.name,self.name,self.age,self.sex,self.salary,self.course))
    def teach(self):
        print("%s is teaching course [%s]"%(self.name,self.course))

class Student(SchooMember):
    def __init__(self, name, age, sex, stu_id, grade):
        super(Student, self).__init__(name, age, sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        print('''
         - - - info of Student:%s - - -
         Name:%s
         Age:%s
         Sex:%s
         stu_id:%s
         grade:%s
         ''' % (self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
    def pay_tuition(self,amount):
        print("%s has paid tuition for %s $"%(self.name.amount))

shool = School('成都师范',"成都")

t1 = Teacher('li',56,'MF',10000,'linux')
t1 = Teacher('jie',12,'M',1000,'python')

s1 = Student('chen',23,'MF',1001,'python')
s2 = Student('xu',25,'M',1002,'linux')

t1.tell()
s1.tell()

#School.hire(t1)
#School.enroll(s1)

# print(school.students)
# print(school.staffs)