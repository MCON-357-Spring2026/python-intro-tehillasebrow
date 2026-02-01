"""
TODO:
Dictionary of students -> grades
Print averages
"""


students = {
    "Shana Kaufman": [90, 89, 65, 45, 97],
    "Chani Lichtman": [76, 90, 100, 37, 105],
    "Aviva Rosenberg": [88, 92, 77, 85, 91],
    "Leah Stein": [95, 100, 98, 87, 93],
    "Meira Adler": [70, 65, 80, 72, 68],
    "Tova Green": [82, 79, 88, 90, 84],
    "Yosefa Cohen": [100, 97, 93, 89, 96],
    "Malky Rubin": [58, 73, 69, 75, 60],
    "Daniella Farkas": [85, 90, 92, 78, 88],
    "Rivka Silver": [91, 94, 89, 96, 92]
}

for names, grades in students.items():
    var=0
    for g in grades:
        var += g
    print(names)
    print(var/(len(grades)))


