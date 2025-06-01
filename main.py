from db import setup_database, add_student, add_fee_record, view_student

setup_database()

def menu():
    while True:
        print("\n--- Student Fee Management ---")
        print("1. Add New Student")
        print("2. Add Fee Record")
        print("3. View Student Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student name: ")
            class_name = input("Enter student class: ")
            fee = float(input("Enter total fee: "))
            add_student(name, class_name, fee)
            print("Student added successfully.")

        elif choice == '2':
            student_id = int(input("Enter student ID: "))
            amount = float(input("Enter amount paid: "))
            slip = input("Enter slip number: ")
            add_fee_record(student_id, amount, slip)

        elif choice == '3':
            student_id = int(input("Enter student ID: "))
            view_student(student_id)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

menu()
