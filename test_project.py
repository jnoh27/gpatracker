import pytest
from project import add_course, update_grade, calculate_gpa, predict_new_gpa, remove_course, courses

# Test for adding a normal course
def test_add_normal_course():
    # Clear the courses list to ensure a clean state
    courses.clear()

    # Add a normal course
    add_course()

    # Ensure that the course is added correctly
    assert len(courses) == 1
    assert courses[0]["course_name"] == "MATH"  # Assuming user input as "MATH"
    assert courses[0]["grade"] == "A"  # Assuming user input as "A"
    assert courses[0]["credit"] == 1.0  # Assuming user input as 1.0
    assert courses[0]["AP"] == False  # Assuming user input as 'N' for AP

# Test for adding an AP course
def test_add_ap_course():
    # Clear the courses list
    courses.clear()

    # Add an AP course
    add_course()

    # Ensure that the course is added correctly
    assert len(courses) == 1
    assert courses[0]["course_name"] == "AP HISTORY"  # Assuming user input as "AP HISTORY"
    assert courses[0]["grade"] == "A"  # Assuming user input as "A"
    assert courses[0]["credit"] == 1.0  # Assuming user input as 1.0
    assert courses[0]["AP"] == True  # Assuming user input as 'Y' for AP

# Test GPA calculation with normal and AP courses
def test_calculate_gpa():
    # Clear the courses list
    courses.clear()

    # Add two normal courses and one AP course
    courses.append({"course_name": "MATH", "grade": "A", "credit": 1.0, "AP": False})
    courses.append({"course_name": "ENGLISH", "grade": "A", "credit": 1.0, "AP": False})
    courses.append({"course_name": "AP HISTORY", "grade": "A", "credit": 1.0, "AP": True})

    # Calculate GPA
    gpa = calculate_gpa()

    # Ensure that the GPA is correct (2 normal courses + 1 AP course)
    # 4.0 (normal) + 4.0 (normal) + 5.0 (AP) / 3 = 4.33
    assert pytest.approx(gpa, 0.01) == 4.33

# Test GPA prediction functionality
def test_predict_new_gpa(monkeypatch):
    # Clear the courses list
    courses.clear()

    # Add two normal courses
    courses.append({"course_name": "MATH", "grade": "A", "credit": 1.0, "AP": False})
    courses.append({"course_name": "ENGLISH", "grade": "B+", "credit": 1.0, "AP": False})

    # Mock user input for predicting a grade change
    monkeypatch.setattr('builtins.input', lambda _: "1")  # Select the first course
    monkeypatch.setattr('builtins.input', lambda _: "A")  # Change grade to A

    original_gpa = calculate_gpa()

    # Predict the new GPA
    predict_new_gpa()

    new_gpa = calculate_gpa()

    # Ensure that the GPA has changed after hypothetical grade change
    assert new_gpa != original_gpa
    assert pytest.approx(new_gpa, 0.01) == 4.0  # After changing both to A

# Test for updating course grade
def test_update_grade(monkeypatch):
    # Clear the courses list
    courses.clear()

    # Add a course
    courses.append({"course_name": "MATH", "grade": "B", "credit": 1.0, "AP": False})

    # Mock user input to update grade
    monkeypatch.setattr('builtins.input', lambda _: "MATH")
    monkeypatch.setattr('builtins.input', lambda _: "A")

    # Update the course grade
    update_grade()

    # Ensure that the grade was updated
    assert courses[0]["grade"] == "A"

# Test for removing a course
def test_remove_course(monkeypatch):
    # Clear the courses list
    courses.clear()

    # Add two courses
    courses.append({"course_name": "MATH", "grade": "A", "credit": 1.0, "AP": False})
    courses.append({"course_name": "ENGLISH", "grade": "B+", "credit": 1.0, "AP": False})

    # Mock user input to remove the first course
    monkeypatch.setattr('builtins.input', lambda _: "1")

    # Remove the course
    remove_course()

    # Ensure that the course was removed
    assert len(courses) == 1
    assert courses[0]["course_name"] == "ENGLISH"
