# Student Record Manager

## About the Project

Student Record Manager is a simple Python project made to store and manage student details. It uses a CSV file as a small database where student information can be saved and updated.

The program is menu-based, so the user can select what they want to do by entering a number.

## Information Stored

For each student, the program stores:

* Registration Number
* Name
* Date of Birth
* Branch

## What This Project Can Do

The program provides the following options:

1. **Student Record Information** – Shows a short description of the project.
2. **Add Student Record** – Adds a new student's details to the CSV file.
3. **Update Student Record** – Changes the details of an existing student.
4. **Delete Student Record** – Removes a student's record.
5. **Display Records** – Shows all the student records stored in the file.
6. **Search Record** – Finds a student using their registration number.
7. **Exit** – Closes the program.

## How It Works

The program is written in Python and uses the built-in `csv` module. The student records are stored in a file named `records.csv`.

Whenever a new record is added, it is written to the CSV file. For updating or deleting a record, the program reads the existing records, makes the required changes, and then saves the updated data back into the file.

## Requirements

* Python 3
* Python's built-in `csv` module
* A folder/location where the `records.csv` file can be stored

No extra Python packages are required.

## How to Run

1. Install Python 3 on your computer.
2. Save the program as a `.py` file.
3. Make sure the file location used in the program exists.
4. Run the Python file.
5. Select an option from the menu and follow the instructions.

## Example

When the program starts, it displays a menu like:

```text
No.1 Student record information
No.2 To add student information to record
No.3 To update student information
No.4 To delete student information
No.5 display record
No.6 Search student record
No.7 To EXIT
```

The user can enter a number such as `2` to add a new student or `6` to search for a student.

## Purpose

The main purpose of this project is to practice Python programming, functions, file handling, CSV files, loops, and basic record management.

## Conclusion

This project is a basic way of managing student information using Python. It is simple to understand and can be improved later by adding features such as better input validation, a graphical interface, or more student details.
