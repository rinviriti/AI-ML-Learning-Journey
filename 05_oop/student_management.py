# Student Management System

class Student:

    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

    def display(self):
        print("Name:", self.name)
        print("CGPA:", self.cgpa)

student1 = Student("Riti", 3.86)

student1.display()
