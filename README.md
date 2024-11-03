# GPA Tracker

## Video Demo



## Description

GPA Calculator following KIS guidelines.

### Features:

1. Add Course and Grade: Input details such as course name, grade (e.g., A, B+), credits, and AP status.
2. Update Grade: Modify grades to keep GPA calculations current.
3. Calculate GPA: Automatically calculate GPA, adding 0.5 to AP classes.
4. Predict Future GPA: See how potential grade changes could affect GPA.
5. Remove Course: Delete courses to keep your list accurate.
6. Show Courses: View a list of all courses, grades, and GPA points.
7. Save/Load Courses: Courses are saved to a CSV file, automatically reloaded each session.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jnoh27/gpa-tracker.git
   cd gpa-tracker
2. **Download libraries**:
   ```bash
   pip install -r requirements.txt
3. Ensure there’s at least 15 MB of free space for saving the CSV file.

To use, download the `project.py` file on your computer and run it using an interpreter.


### Usage
- `project.py` is the code that mainly runs these features.
- `test_project.py` is the code to test. Run it with:
    ```bash
    python test_project.py
- After each session, a csv file with the course list will be saved in the same directory as the files.

### Grading Details

The tool uses a grade_conversion dictionary to convert letter grades to GPA points (e.g., “A” to 4.0). The cumulative GPA is calculated by dividing the total grade points by credit hours, with a 0.5-point boost for AP classes.

The standard follows KIS grading conventions.

### FAQ
**Q: Can this be used for non-KIS grading scales?** <br>
A: It’s optimized for KIS, but the `grade_conversion` dictionary can be customized.

**Q: Is there another way to adjust AP weighting?** <br>
A: The 0.5 AP boost is hardcoded; code modifications are needed for changes.

### Credits
Thanks to Python developers and the Harvard CS50 course!

