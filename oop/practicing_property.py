# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     @property
#     def msg(self):
#         return f"{self.name} got grade: {self.grade}."

#     @msg.setter
#     def msg(self, msg):
#         words = msg.split(" ")
#         self.name = words[0]
#         self.grade = words[-1]


# student1 = Student("Rose", "A")
# print(student1.name)
# student1.msg = "Lilly got grade C"
# print(student1.name, student1.msg)


class Student:
    def __init__(self, marks):
        self._marks = marks

    def percentage(self):
        return (self._marks / 600) * 100

    def getter(self):
        return self._marks

    def setter(self, value):
        if value < 0 or value > 600:
            print("Value should not be negative or > 600")
        else:
            self._marks = value

    marks = property(getter, setter)


s = Student(400)
s.marks = 500
print(s.marks)
print(s.percentage(), "%")
