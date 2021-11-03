class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    @property
    def msg(self):
        return f"{self.name} got grade: {self.grade}."

    @msg.setter
    def msg(self, msg):
        words = msg.split(" ")
        self.name = words[0]
        self.grade = words[-1]


student1 = Student("Rose", "A")
print(student1.name)
student1.msg = "Lilly got grade C"
print(student1.name, student1.msg)