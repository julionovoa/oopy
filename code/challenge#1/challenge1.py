import random


class Student:
    educational_platform = "udemy"

    def __init__(self, name, age=27):
        self.name = name
        self.age = age

    def greet(self):
        greetings = [
            "Hi, I'm {}",
            "Hey there, my name is {}",
            "Hi. Oh, my name is {}"
        ]
        greeting = random.choice(greetings)
        return greeting.format(self.name)


if __name__ == "__main__":
    # List of students
    students = ["Leonardo", "Donatello", "Michelangelo", "Raphael"]
    # Create a list of Student objects
    students_obj = [Student(s) for s in students]
    # Print the Student objects greetings
    for student in students_obj:
        print(student.greet())
