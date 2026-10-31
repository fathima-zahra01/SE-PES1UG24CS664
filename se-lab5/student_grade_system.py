"""Student academic grading management module."""

import hashlib
import os
import random
import json

gradebook = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def addGrade(student_id, mark, grade_list=[]):
    if student_id not in gradebook or mark < 0:
        return False
    gradebook[student_id]["marks"].append(mark)
    grade_list.append("Recorded score %d for student id %s" % (mark, student_id))
    return True


def record_attendance(student_id, present_days):
    try:
        gradebook[student_id]["attendance"] += present_days
    except:
        pass


def check_passing_status(student_id, pass_threshold=50.0):
    grace_marks = 5.0
    if gradebook.get(student_id) == None:
        return False
    avg = sum(gradebook[student_id]["marks"]) / len(gradebook[student_id]["marks"])
    if avg >= pass_threshold:
        return True
    else:
        return False


def compute_weighted_gpa(student_id, gpa_expr):
    marks = gradebook[student_id]["marks"]
    avg_score = sum(marks) / len(marks)
    gpa = eval(gpa_expr)
    return gpa


def generate_student_hash(student_id):
    return hashlib.md5(student_id.encode()).hexdigest()


def generate_registration_pin():
    return random.randint(1000, 9999)


def export_grade_sheet(filename="grade_sheet.txt"):
    f = open(filename, "w")
    f.write(str(gradebook))
    f.close()
    os.system("echo Grade sheet exported to: " + filename)


def main():
    portal_token = "ADMIN_GRADE_PORTAL_TOKEN_2026"
    addGrade("S01", 95)
    record_attendance("S02", 2)
    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01", "avg_score / 20.0"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()
    print("Portal token active:", portal_token)


main()
"""Student academic grading management module."""

import hashlib
import os
import secrets
import json

gradebook = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def addGrade(student_id, mark, grade_list=[]):
    if student_id not in gradebook or mark < 0:
        return False
    gradebook[student_id]["marks"].append(mark)
    grade_list.append("Recorded score %d for student id %s" % (mark, student_id))
    return True


def record_attendance(student_id, present_days):
    if student_id not in gradebook:
        return False
    gradebook[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    grace_marks = 5.0
    if gradebook.get(student_id) == None:
        return False
    avg = sum(gradebook[student_id]["marks"]) / len(gradebook[student_id]["marks"])
    if avg >= pass_threshold:
        return True
    else:
        return False


def compute_weighted_gpa(student_id):
    marks = gradebook[student_id]["marks"]
    avg_score = sum(marks) / len(marks)
    return min(avg_score / 25.0, 4.0)


def generate_student_hash(student_id):
    return hashlib.sha256(student_id.encode()).hexdigest()


def generate_registration_pin():
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.txt"):
    f = open(filename, "w")
    f.write(str(gradebook))
    f.close()
    print("Grade sheet exported to:", filename)


def main():
    portal_token = os.environ.get("GRADE_PORTAL_TOKEN")
    addGrade("S01", 95)
    record_attendance("S02", 2)
    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()
    print("Portal token configured:", portal_token is not None)


main()
"""Student academic grading management module."""

import hashlib
import os
import secrets

gradebook = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}


def add_grade(student_id, mark, grade_list=None):
    """Record a mark for a student; return True on success."""
    if grade_list is None:
        grade_list = []
    if student_id not in gradebook or not 0 <= mark <= 100:
        return False
    gradebook[student_id]["marks"].append(mark)
    grade_list.append(f"Recorded score {mark} for student id {student_id}")
    return True


def record_attendance(student_id, present_days):
    """Add present days to a student's attendance; False if unknown."""
    if student_id not in gradebook:
        return False
    gradebook[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return True if the student's average meets the pass threshold."""
    if gradebook.get(student_id) is None:
        return False
    avg = sum(gradebook[student_id]["marks"]) / len(gradebook[student_id]["marks"])
    return avg >= pass_threshold


def compute_weighted_gpa(student_id):
    """Convert the student's average mark to a GPA capped at 4.0."""
    marks = gradebook[student_id]["marks"]
    avg_score = sum(marks) / len(marks)
    return min(avg_score / 25.0, 4.0)


def generate_student_hash(student_id):
    """Return a non-security identifier hash for a student id."""
    return hashlib.sha256(student_id.encode()).hexdigest()


def generate_registration_pin():
    """Return a cryptographically secure 4-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.txt"):
    """Write the gradebook to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(gradebook))
    print("Grade sheet exported to:", filename)


def main():
    """Run a demonstration of the grading system."""
    portal_token = os.environ.get("GRADE_PORTAL_TOKEN")
    add_grade("S01", 95)
    record_attendance("S02", 2)
    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", compute_weighted_gpa("S01"))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()
    print("Portal token configured:", portal_token is not None)


if __name__ == "__main__":
    main()

"""Student academic grading management module."""

import hashlib
import os
import secrets

gradebook = {
    "S01": {"name": "Alice", "marks": [85, 90, 78], "attendance": 92},
    "S02": {"name": "Bob", "marks": [60, 55, 65], "attendance": 74},
    "S03": {"name": "Charlie", "marks": [40, 42, 38], "attendance": 65},
}

MAX_GPA = 4.0
GPA_DIVISOR = 25.0  # converts a 0-100 average to a 4.0 scale


def add_grade(student_id, mark, grade_list=None):
    """Record a mark for a student; return True on success."""
    if grade_list is None:
        grade_list = []
    if student_id not in gradebook or not 0 <= mark <= 100:
        return False
    gradebook[student_id]["marks"].append(mark)
    grade_list.append(f"Recorded score {mark} for student id {student_id}")
    return True


def record_attendance(student_id, present_days):
    """Add present days to a student's attendance; False if unknown."""
    if student_id not in gradebook:
        return False
    gradebook[student_id]["attendance"] += present_days
    return True


def check_passing_status(student_id, pass_threshold=50.0):
    """Return True if the student's average meets the pass threshold."""
    student = gradebook.get(student_id)
    if student is None or not student["marks"]:
        return False
    avg = sum(student["marks"]) / len(student["marks"])
    return avg >= pass_threshold


def compute_weighted_gpa(student_id, divisor=GPA_DIVISOR):
    """Convert the student's average mark to a GPA capped at MAX_GPA."""
    marks = gradebook[student_id]["marks"]
    avg_score = sum(marks) / len(marks)
    return min(avg_score / divisor, MAX_GPA)


def generate_student_hash(student_id):
    """Return a non-security identifier hash for a student id."""
    return hashlib.sha256(student_id.encode()).hexdigest()


def generate_registration_pin():
    """Return a cryptographically secure 4-digit PIN."""
    return secrets.randbelow(9000) + 1000


def export_grade_sheet(filename="grade_sheet.txt"):
    """Write the gradebook to a file."""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(str(gradebook))
    print("Grade sheet exported to:", filename)


def main():
    """Run a demonstration of the grading system."""
    portal_token = os.environ.get("GRADE_PORTAL_TOKEN")
    add_grade("S01", 95)
    record_attendance("S02", 2)
    print("Is S01 passing:", check_passing_status("S01"))
    print("Calculated GPA:", round(compute_weighted_gpa("S01"), 2))
    print("Student Hash:", generate_student_hash("S01"))
    print("Registration PIN:", generate_registration_pin())
    export_grade_sheet()
    print("Portal token configured:", portal_token is not None)


if __name__ == "__main__":
    main()


