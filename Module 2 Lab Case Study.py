# Rachel Smiley
# Module 2 Lab Case Study.py
# Description: This app collects student names and GPAs,
# then determines whether they qualify for the Dean's List
# or Honor Roll. The program continues until "ZZZ" is entered
# as the last name.
# Variables:
# last_name (string): stores the student's last name
# first_name (string): stores the student's first name
# gpa (float): stores the student's GPA
while True:
    last_name = input("Enter student's last name: ")
    if last_name == "ZZZ":
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))
    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")