# GPA calculator for 6 fixed courses

grade_points = {
"A": 5,
"B": 4,
"C": 3,
"D": 2,
"E": 1,
"F": 0
}

courses = [
{"code": "EIE322", "unit": 2, "grade": "A"},
{"code": "GEC320", "unit": 3, "grade": "A"},
{"code": "GEC321", "unit": 3, "grade": "A"},
{"code": "EIE323", "unit": 3, "grade": "A"},
{"code": "EIE326", "unit": 3, "grade": "A"},
{"code": "EIE327", "unit": 3, "grade": "A"}
]

total_units = 0
total_points = 0

for course in courses:
    unit = course["unit"]
    grade = course["grade"]
    point = grade_points[grade] * unit
    total_units += unit
    total_points +=point

gpa = total_points / total_units
print(f"GPA: {gpa:.2f}")
