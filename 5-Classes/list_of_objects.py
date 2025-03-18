"""
It is a basic student project

"""

from typing import List


class Student:
    def __init__(self):
        self.roll_no = int(input("Enter the roll no: "))
        self.name = input("Enter the name: ")
        self.gender = input("Enter the gender: ")
        self.marks = []
        for i in range(3):
            mark = int(input(f"Enter marks {i+1}: "))
            self.marks.append(mark)

    def display(self):
        print(f"\nStudent Roll No: {self.roll_no}")
        print(f"Student Name: {self.name}")
        print(f"Student Gender: {self.gender}")
        print("Student Marks are- ")
        for i in range(3):
            print(f"Marks {i+1}: {self.marks[i]}")

    def display_marks(self):
        print(f"Marks of {self.name} are: ")
        for i in range(3):
            print(f"Marks of subject {i+1}: {self.marks[i]}")

    def update_name(self, name):
        self.name = name
        print("Student name successfully Updated.\n")

    def update_marks(self):
        self.marks.clear()
        for i in range(3):
            mark = int(input(f"Enter marks {i+1}: "))
            self.marks.append(mark)
        print("Marks are update successfully.\n")

    def check_roll_no(self, roll):
        if self.roll_no == roll:
            return True
        return False


all_students: List[Student] = []

while True:
    print("\n1. Add a student")
    print("2. View all students")
    print("3. Update Student Name")
    print("4. Display student Marks")
    print("5. Update Student Marks")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        obj = Student()
        all_students.append(obj)
    elif choice == 2:
        if len(all_students) == 0:
            print("No student data vavailable to display")
        else:
            for st in all_students:
                st.display()
    elif choice == 3:
        is_present = False
        roll = int(input("Enter the roll no of student whose name will be update: "))
        for st in all_students:
            if st.check_roll_no(roll):
                name = input("Enter the update name: ")
                st.update_name(name)
                is_present = True
                break
        if not is_present:
            print("\nStudent not present. Please enter valid roll no")
    elif choice == 4:
        is_present = False
        roll = int(
            input("Enter the roll no of student whose marks will be displayed: ")
        )
        for st in all_students:
            if st.check_roll_no(roll):
                st.display_marks()
                is_present = True
                break
        if not is_present:
            print("\nStudent not present. Please enter valid roll no")
    elif choice == 5:
        is_present = False
        roll = int(input("Enter the roll no of student whose name will be update: "))
        for st in all_students:
            if st.check_roll_no(roll):
                st.update_marks()
                is_present = True
                break
        if not is_present:
            print("\nStudent not present. Please enter valid roll no")
    elif choice == 6:
        print("Exiting. Thank you!!")
        break
    else:
        print("Invalid Choice")
