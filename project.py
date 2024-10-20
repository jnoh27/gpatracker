import sys
import csv

courses = []
# Dictionary for letter grade to GPA conversion
grade_conversion = {
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "F": 0.0
}

def main():
    load_courses_from_csv()
    # display menu for user
    while True:
        print("1. Add Course and Grade")
        print("2. Update Grade")
        print("3. Calculate GPA")
        print("4. Predict Future GPA")
        print("5. Remove course")
        print("6. Show courses")
        print("7. Exit")

        # Get user choice
        while True:
            # keep prompting the user for a valid input
            try:
                choice = int(input("Enter your choice: "))
                break
            except ValueError:
                print("Please enter a number from 1-6.")

        if choice == 1:
            add_course()
        elif choice == 2:
            update_grade()
        elif choice == 3:
            print(f"Your final gpa is: {calculate_gpa(): .2f}")
        elif choice == 4:
            predict_new_gpa()
        elif choice == 5:
            remove_course()
        elif choice == 6:
            show_course()
        elif choice == 7:
            save_courses_to_csv()
            sys.exit("Exiting program.")
        else:
            print("Invalid choice, please try again.")

        print()

def add_course():
    # Prompt user for course details
    while True:
        try:
            course_name = input("Enter course name: ").strip().upper()
            grade = input("Enter grade (e.g., A, B+, etc.): ").upper().strip()
            credit = float(input("Enter credit hours for the course (1 or 0.5): ").strip())
            break
        except ValueError:
            print("Credit hours and weight should be a decimal (float) value. Please try again. ")

    while True:
        temp = input("Is this course AP? Y/N: ").strip().upper()
        AP = False
        if temp == "Y":
            AP = True
        elif temp != "Y" and temp != "N":
            print("Please answer with a Y or a N")
            continue

        break

    # Create a course dictionary to store the details
    course = {
        "course_name": course_name,
        "grade": grade,
        "credit": credit,
        "AP": AP
    }

    # Add course to the list
    courses.append(course)
    print(f"Course {course_name} added successfully!")

def update_grade():
    course_name = input("Enter course name you want to update grade for: ").strip().upper()
    grade = grade_conversion[input("Enter new grade (e.g., A, B+, etc.): ").strip().upper()]
    for course in courses:
        if course["course_name"] == course_name:
            course["grade"] = grade
            break

    print("Course grade updated successfully!")

def calculate_gpa():
    total_credit = 0
    total_grade = 0

    for course in courses:
        total_credit += course["credit"]
        total_grade += grade_conversion[course["grade"]]
        if grade_conversion[course["grade"]] == 0.0:
            continue
        if course["AP"]:
            total_grade += 1

    final_gpa = total_grade / total_credit
    return final_gpa

def predict_new_gpa():
    # Show the user current course
    show_course()

    while True:
        try:
            num = int(input("How many courses do you want to hyptehtically change?: ").strip())
            break
        except ValueError:
            print("Please enter a numerical value.")

    original_grades = []

    for i in range(num):
        try:
            course_index = int(input("Enter the index number of the course you want to change: ").strip()) - 1
            original_grades.append((course_index, courses[course_index]["grade"]))

            new_grade = input("Enter hypothetical grade (e.g., A, B+, etc.): ").upper().strip()
            courses[course_index]["grade"] = new_grade
            break
        except ValueError:
            print("Please enter a numerical value.")

    print(f"Your hypothetical GPA with those changes in your grade is: {calculate_gpa(): .2f}")

    # revert to original grades
    for course_index, original_grade in original_grades:
        courses[course_index]["grade"] = original_grade

def remove_course():
    if not courses:
        print("No courses available to remove. Add a course first.")
        return

    # Show the user current course
    show_course()

    # Prompt the user to select the course to remove
    while True:
        try:
            course_index = int(input("Enter the index number of the course you want to change: ").strip()) - 1
            removed_course = courses.pop(course_index)
            print(f"Course {removed_course['course_name']} removed successfully!")
            break
        except ValueError:
            print("Please enter a numerical value")
        except IndexError:
            print("Error: Index out of range. Please select a valid course number.")

def show_course():
    for i in range(len(courses)):
        course = courses[i]
        num_grade = grade_conversion[course['grade']]
        if course['AP']:
            num_grade += 1
        print(f"{i+1}: {course['course_name']} | {course['grade']} | {num_grade} | AP: {course['AP']}")

def save_courses_to_csv():
    with open('courses.csv', 'w', newline='') as csvfile:
        fieldnames = ['course_name', 'grade', 'credit', 'AP']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for course in courses:
            writer.writerow(course)

def load_courses_from_csv():
    try:
        with open('courses.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                course = {
                    "course_name": row['course_name'],
                    "grade": row['grade'],
                    "credit": float(row['credit']),
                    "AP": row['AP'] == 'True'
                }
                courses.append(course)
    except FileNotFoundError:
        pass

# only run if main is called
if __name__ == "__main__":
    main()
