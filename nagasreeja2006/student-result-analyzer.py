#student-result-analyzer
from functools import reduce
students = [
    {
        "name": "John Doe",
        "roll_no": "12345",
        "branch": "CSE",
        "marks": 85
    },
    {
        "name": "Jane Smith",
        "roll_no": "67890",
        "branch": "ECE",
        "marks": 92
    }
]

print("=" * 40)
print("     STUDENT RESULT ANALYZER")
print("=" * 40)
def add_student():
    name=input("Enter student name: ")
    roll_no=input("Enter student roll number: ")
    branch=input("Enter student branch: ").upper()
    marks=int(input("Enter student marks: "))
    student={
        "name": name,
        "roll_no": roll_no,
        "branch": branch,
        "marks": marks
    }
    students.append(student)
def view_all_students():
    for s in students:
        print(f"Name:{s['name']}")
        print(f"Roll Number:{s['roll_no']}")
        print(f"Branch:{s['branch']}")
        print(f"Marks:{s['marks']}")
        print("-" * 20)
def search_student():
    s_name=input("Enter student name to search:").lower()        
    for s in students:
        if s["name"].lower() == s_name:
            print("Students Found:")
            print(f"Name:{s['name']}")
            print(f"Roll Number:{s['roll_no']}")
            print(f"Branch:{s['branch']}")
            print(f"Marks:{s['marks']}")
            print("-" * 20)
            break
    else:
        print("Student not found!")
def update_marks():
    s_name=input("Enter student name to update marks:").lower()
    for s in students:
        if s['name'].lower() == s_name:
            print(f"Current marks of {s['name']}: {s['marks']}")
            new_marks=int(input("Enter new marks: "))
            s['marks'] = new_marks
            print("Marks updated successfully!")
            break
    else:
        print("Student not found!")
def delete_student():
    s_name=input("Enter student name to delete:").lower()
    for s in students:
        if s['name'].lower() == s_name:
            students.remove(s)
            print(f"Student {s['name']} deleted successfully!")
            break
    else:
        print("Student not found!")  

def show_passed_students():
    print("Passed Students:")
    for s in students:
        if s['marks'] >= 40:
            print(f"Name:{s['name']}, Marks:{s['marks']}")
    print("-" * 20)  

def show_failed_students():
    print("Failed Students:")
    for s in students:
        if s['marks'] < 40:
            print(f"Name:{s['name']}, Marks:{s['marks']}")
    print("-" * 20)

def show_topper():
    topper = reduce(lambda x, y: x if x['marks'] > y['marks'] else y, students)
    print(f"Topper: {topper['name']}, Marks: {topper['marks']}")

def show_class_statistics():

    total_students = len(students)
    marks = list(map(lambda s: s['marks'], students))
    total_marks = reduce(lambda x, y: x + y, marks)
    average_marks = total_marks / total_students
    highest_marks = reduce(lambda x, y: x if x > y else y,marks)
    lowest_marks = reduce(lambda x, y: x if x < y else y, marks)
    passed_students = list(filter(lambda s: s['marks'] >= 40, students))
    failed_students = list(filter(lambda s: s['marks'] < 40, students))
    print("\n" + "=" * 30)
    print("CLASS STATISTICS")
    print("=" * 30)
    print(f"Total Students: {total_students}")
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")
    print(f"Highest Marks: {highest_marks}")
    print(f"Lowest Marks: {lowest_marks}")
    print(f"Passed Students: {len(passed_students)}")
    print(f"Failed Students: {len(failed_students)}")
    print("=" * 30)
    

while True:

    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Show Passed Students")
    print("7. Show Failed Students")
    print("8. Show Topper")
    print("9. Show Class Statistics")
    print("10. Exit")

    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_student()
        print("Student added successfully!")
    elif choice == "2":
        if not students:
            print("No students found!")
        else:
            print("All Students:")
            view_all_students()    

    elif choice == "3":
        if not students:
            print("No students found!")
        else:
            search_student()     

    elif choice == "4":
        if not students:
            print("No students found!")
        else:
            update_marks()   

                    
    elif choice == "5":
        if not students:
            print("No students found!")
        else:
            delete_student()
    elif choice == "6":
        if not students:
            print("No students found!")
        else:
            show_passed_students()
    elif choice == "7":
        if not students:
            print("No students found!")
        else:
            show_failed_students()
            
    elif choice == "8":
        if not students:
            print("No students found!")
        else:
            show_topper()
    elif choice == "9":
        if not students:
            print("No students found!")
        else:
            show_class_statistics()
    elif choice == "10":
        print("Exiting Student Result Analyzer...")
        break

    else:
        print("invalid choice! Please try again.")
