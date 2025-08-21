# Student Management System

students = []

def add_student():
    print("\n--- Add Student ---")
    try:
        student_id = input("Enter student ID: ").strip()
        if any(s['id'] == student_id for s in students):
            print("Student with this ID already exists.")
            return

        name = input("Enter name: ").strip()
        age = int(input("Enter age: "))
        course = input("Enter course: ").strip()

        students.append({'id': student_id, 'name': name, 'age': age, 'course': course})
        print("Student added successfully.")
    except ValueError:
        print("Invalid input. Age must be a number.")

def view_students():
    print("\n--- View All Students ---")
    if not students:
        print("No student records found.")
        return

    for idx, student in enumerate(students, start=1):
        print(f"{idx}. ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")

def search_student():
    print("\n--- Search Student ---")
    search_id = input("Enter student ID to search: ").strip()
    for student in students:
        if student['id'] == search_id:
            print(f"Found: ID: {student['id']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
            return
    print("Student not found.")

def update_student():
    print("\n--- Update Student ---")
    update_id = input("Enter student ID to update: ").strip()
    for student in students:
        if student['id'] == update_id:
            print("Leave blank to keep current value.")
            new_name = input(f"Enter new name ({student['name']}): ").strip()
            new_age = input(f"Enter new age ({student['age']}): ").strip()
            new_course = input(f"Enter new course ({student['course']}): ").strip()

            if new_name:
                student['name'] = new_name
            if new_age:
                try:
                    student['age'] = int(new_age)
                except ValueError:
                    print("Invalid age. Keeping old value.")
            if new_course:
                student['course'] = new_course

            print("Student record updated.")
            return
    print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    delete_id = input("Enter student ID to delete: ").strip()
    for i, student in enumerate(students):
        if student['id'] == delete_id:
            del students[i]
            print("Student deleted successfully.")
            return
    print("Student not found.")

def show_menu():
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
