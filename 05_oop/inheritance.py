# Inheritance Example

class Person:

    def introduce(self):
        print("I am a person.")

class Student(Person):
    pass

student = Student()

student.introduce()
