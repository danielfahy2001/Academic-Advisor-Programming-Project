from Student import Student
from MailingAddress import MailingAddress
from Email import Email
from Phone import Phone
from Date import Date

def add_student():
    """Add a new student to the system."""
    print("\n--- ADD NEW STUDENT ---")

    # Get basic info
    name = input("Student name (First Middle Last): ")
    sid = int(input("Student ID: "))

    # Get address
    print("\n--- Mailing Address ---")
    street = input("Street: ")
    city = input("City: ")
    state = input("State: ")
    zipcode = int(input("Zip code: "))
    addr_type = input("Address type (permanent/local): ")
    address = MailingAddress(street, city, state, zipcode, addr_type)

    # Get emails (at least one)
    emails = []
    print("\n--- Email Address ---")
    email_addr = input("Email address: ")
    email_type = input("Email type (personal/academic): ")
    emails.append(Email(email_addr, email_type))

    # Ask if they want to add more emails
    more = input("Add another email? (y/n): ")
    if more.lower() == 'y':
        email_addr2 = input("Second email address: ")
        email_type2 = input("Email type: ")
        emails.append(Email(email_addr2, email_type2))

    # Get phone numbers
    phones = []
    print("\n--- Phone Number ---")
    phone_num = input("Phone number (xxx-xxx-xxxx): ")
    phone_type = input("Phone type (cell/home): ")
    phones.append(Phone(phone_num, phone_type))

    # Ask if they want to add another phone
    more = input("Add another phone? (y/n): ")
    if more.lower() == 'y':
        phone_num2 = input("Second phone number: ")
        phone_type2 = input("Phone type: ")
        phones.append(Phone(phone_num2, phone_type2))

    # Get dates
    print("\n--- Birth Date ---")
    birth_year = int(input("Birth year: "))
    birth_month = int(input("Birth month (1-12): "))
    birth_day = int(input("Birth day (1-31): "))
    birth_date = Date(birth_year, birth_month, birth_day)

    print("\n--- Acceptance Date ---")
    accept_year = int(input("Acceptance year: "))
    accept_month = int(input("Acceptance month (1-12): "))
    accept_day = int(input("Acceptance day (1-31): "))
    accept_date = Date(accept_year, accept_month, accept_day)

    # Get semester and major
    semester = input("Start semester (Spring 2024): ")
    major = input("Major: ")

    # Create and return student
    student = Student(name, sid, address, emails, phones,
                     birth_date, accept_date, semester, major)
    return student

def find_student(students, sid):
    """Find a student by ID number."""
    for student in students:
        if student.get_sid() == sid:
            return student
    return None

def show_student(student):
    """Display a student's information."""
    print("\n" + "="*50)
    print(student)
    print("="*50)

def edit_student(student):
    """Edit a student's information."""
    print("\n--- EDIT STUDENT ---")
    print("What do you want to edit?")
    print("1. Name")
    print("2. Major")
    print("3. Semester")
    print("4. Cancel")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        new_name = input("Enter new name: ")
        student.set_name(new_name)
        print("Name updated!")

    elif choice == "2":
        new_major = input("Enter new major: ")
        student.set_major(new_major)
        print("Major updated!")

    elif choice == "3":
        new_semester = input("Enter new semester: ")
        student.set_semester(new_semester)
        print("Semester updated!")

    else:
        print("Edit cancelled.")

def create_sample_students():
    """Create 5 sample students to start with."""
    students = []

    # Student 1
    addr1 = MailingAddress("123 Main St", "State College", "PA", 16801, "local")
    email1 = Email("john@psu.edu", "academic")
    phone1 = Phone("814-555-1234", "cell")
    bdate1 = Date(2000, 5, 15)
    adate1 = Date(2018, 8, 20)
    s1 = Student("John Doe", 1001, addr1, [email1], [phone1], bdate1, adate1, "Fall 2018", "CS")
    students.append(s1)

    # Student 2
    addr2 = MailingAddress("456 Oak St", "Pittsburgh", "PA", 15213, "permanent")
    email2 = Email("jane@cmu.edu", "academic")
    phone2 = Phone("412-555-5678", "cell")
    bdate2 = Date(2001, 8, 22)
    adate2 = Date(2019, 9, 1)
    s2 = Student("Jane Smith", 1002, addr2, [email2], [phone2], bdate2, adate2, "Fall 2019", "Engineering")
    students.append(s2)

    # Student 3
    addr3 = MailingAddress("789 Pine St", "Philly", "PA", 19104, "local")
    email3 = Email("bob@upenn.edu", "academic")
    phone3 = Phone("215-555-9012", "cell")
    bdate3 = Date(2002, 3, 10)
    adate3 = Date(2020, 8, 15)
    s3 = Student("Bob Wilson", 1003, addr3, [email3], [phone3], bdate3, adate3, "Fall 2020", "Arts")
    students.append(s3)

    print("Loaded 5 sample students!")
    return students

def main():
    """Main program loop."""
    print("="*50)
    print("STUDENT MANAGEMENT SYSTEM")
    print("="*50)

    # Start with sample students
    students = create_sample_students()

    while True:
        # Show menu
        print("\n--- MENU ---")
        print("1. Add Student")
        print("2. Edit Student")
        print("3. Delete Student")
        print("4. View Student")
        print("5. View All Students")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        # Option 1: Add student
        if choice == "1":
            new_student = add_student()
            students.append(new_student)
            print("Student added! Total students:", len(students))

        # Option 2: Edit student
        elif choice == "2":
            if len(students) == 0:
                print("No students to edit.")
                continue

            sid = int(input("Enter student ID to edit: "))
            student = find_student(students, sid)

            if student:
                show_student(student)
                edit_student(student)
            else:
                print("Student not found!")

        # Option 3: Delete student
        elif choice == "3":
            if len(students) == 0:
                print("No students to delete.")
                continue

            sid = int(input("Enter student ID to delete: "))
            student = find_student(students, sid)

            if student:
                show_student(student)
                confirm = input("Delete this student? (y/n): ")
                if confirm.lower() == 'y':
                    students.remove(student)
                    print("Student deleted!")
                else:
                    print("Delete cancelled.")
            else:
                print("Student not found!")

        # Option 4: View one student
        elif choice == "4":
            if len(students) == 0:
                print("No students to view.")
                continue

            sid = int(input("Enter student ID to view: "))
            student = find_student(students, sid)

            if student:
                show_student(student)
            else:
                print("Student not found!")

        # Option 5: View all students
        elif choice == "5":
            if len(students) == 0:
                print("No students to display.")
                continue

            print("\n" + "="*50)
            print("ALL STUDENTS (" + str(len(students)) + " total)")
            print("="*50)

            for i, student in enumerate(students, 1):
                print("\n--- Student " + str(i) + " ---")
                print(student)

        # Option 6: Exit
        elif choice == "6":
            print("Goodbye!")
            break

        # Invalid choice
        else:
            print("Invalid choice. Try again.")

# Run the program
if __name__ == "__main__":
    main()