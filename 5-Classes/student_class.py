"""
This is to demonstrate basic function of classes.
A class is blueprint for an object.
It contains variables which are called as aatributes.
It contains functions which are called as methods
"""


class Student:
    def __init__(self, roll_no: int, name: str, age: int, standard: int) -> None:
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.standard = standard

    def print_details(self):
        print("----------------------------")
        print(f"Roll no of student: {self.roll_no}")
        print(f"Name of student: {self.name}")
        print(f"Age of student: {self.age}")
        print(f"Standard of student: {self.standard}")
        print("----------------------------")

    def update_details(self, name=None, age=None, standard=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if standard is not None:
            self.standard = standard


if __name__ == "__main__":
    roll_no = int(input("Please enter the roll no: "))
    name = input("Please enter the name: ")
    age = int(input("Please enter the age: "))
    standard = int(input("Please enter the standard: "))

    s1 = Student(roll_no, name, age, standard)
    choice = int(
        input(
            "Here are the choices\n1. Print Details\n2. Update details \nEnter your choice(1 or 2): "
        )
    )
    if choice == 1:
        s1.print_details()
    elif choice == 2:
        update_choice = int(
            input(
                "Here are the choices to update value\n\
                 1. Name\n\
                 2. Age\n\
                 3. Standard:\n\
                 Enter your choice: "
            )
        )
        if update_choice == 1:
            updated_name = input("Please enter the name: ")
            s1.update_details(name=updated_name)
            s1.print_details()
        elif update_choice == 2:
            updated_age = int(input("Please enter the age: "))
            s1.update_details(age=updated_age)
            s1.print_details()
        elif update_choice == 3:
            updated_standard = int(input("Please enter the name: "))
            s1.update_details(standard=updated_standard)
            s1.print_details()
        else:
            print("Invalid Choice!!")
    else:
        print("Invalid Choice!!")
