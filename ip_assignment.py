import pandas as pd

def display_menu():
    print("Please select an action:")
    print("1. Add student")
    print("2. Display database")
    print("3. Search for student")
    print("4. Edit student data")
    print("5. Delete student record")
    print("6. Exit")

def add_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    marks = input("Enter Marks: ")
    data = {
        'Roll No': [roll_no],
        'Name': [name],
        'Marks': [marks]
    }
    df = pd.DataFrame(data)
    df.to_csv('students.csv', mode='a', index=False, header=not pd.io.common.file_exists('students.csv'))
    print("Student added successfully.")

def display_database():
    if pd.io.common.file_exists('students.csv'):
        df = pd.read_csv('students.csv')
        print(df)
    else:
        print("No students found in the database.")

def search_student():
    roll_no = input("Enter Roll No to search: ")
    if pd.io.common.file_exists('students.csv'):
        df = pd.read_csv('students.csv')
        student = df[df['Roll No'] == roll_no]
        if not student.empty:
            print(student)
        else:
            print("Student not found.")
    else:
        print("No students found in the database.")

def edit_student_data():
    roll_no = input("Enter Roll No to edit: ")
    if pd.io.common.file_exists('students.csv'):
        df = pd.read_csv('students.csv')
        student_index = df[df['Roll No'] == roll_no].index
        if not student_index.empty:
            new_name = input("Enter new name: ")
            new_marks = input("Enter new marks: ")
            df.loc[student_index, 'Name'] = new_name
            df.loc[student_index, 'Marks'] = new_marks
            df.to_csv('students.csv', index=False)
            print("Student data updated successfully.")
        else:
            print("Student not found.")
    else:
        print("No students found in the database.")

def delete_student_record():
    roll_no = input("Enter Roll No to delete: ")
    if pd.io.common.file_exists('students.csv'):
        df = pd.read_csv('students.csv')
        student_index = df[df['Roll No'] == roll_no].index
        if not student_index.empty:
            df.drop(student_index, inplace=True)
            df.to_csv('students.csv', index=False)
            print("Student record deleted successfully.")
        else:
            print("Student not found.")
    else:
        print("No students found in the database.")

# Main program
while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")
    if choice == '1':
        add_student()
    elif choice == '2':
        display_database()
    elif choice == '3':
        search_student()
    elif choice == '4':
        edit_student_data()
    elif choice == '5':
        delete_student_record()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
