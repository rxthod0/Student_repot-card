class Student:
    def __init__(self, name, roll_no, marks, total_marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks
        self.total_marks = total_marks
        self.percentage = self.calculate_percentage()
        self.grade = self.get_grade()

    # Percentage calculator
    def calculate_percentage(self):
        return (self.marks / self.total_marks) * 100

    # Grade calculator
    def get_grade(self):
        if self.percentage >= 91:
            return "Grade A"
        elif self.percentage >= 81:
            return "Grade B"
        elif self.percentage >= 71:
            return "Grade C"
        else:
            return "Fail"

    # Output details
    def show_details(self):
        print(f"Details of the Student:")
        print(f"Name        : {self.name}")
        print(f"Roll Number : {self.roll_no}")
        print(f"Marks       : {self.marks}/{self.total_marks}")
        print(f"Percentage  : {self.percentage:.2f}%")
        print(f"Grade       : {self.grade}")


# Example usage
s1 = Student("Alex", 10, 901, 1000)
s1.show_details()
