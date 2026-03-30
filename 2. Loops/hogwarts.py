"""
students = ["Harry", "Hermione", "Ron"]

print(students[0])
print(students[1])
print(students[2])

print("-----------")
for student in students:
    print(student)

print("-----------")

for i in range(len(students)):
    print(i+1, students[i])
"""

"""
#using dictionary
students = {"Ram": "Koteshwor",
    "Harry": "New-delhi",
    "Sasmit": "Kathmandu"
}

print(students["Ram"]) #using key to printout the value i.e. ram key stores koteshwor as value

for student in students:
    print(f"{student} lives in {students[student]}")
"""

arr_students = [
    {"name": "Ram", "address": "Koteshwor", "age": 19},
    {"name": "Harry", "address": "New-delhi", "age": 20},
    {"name": "Sasmit", "address": None, "age": 21}
]
i = 0
for student in arr_students:
    print(f"{arr_students[i]['name']}, {arr_students[i]['address']}, {arr_students[i]['age']}")
    i+=1

print("-----------")
#also, we can do this way...
for student in arr_students:
    print(student['name'], student['address'], student['age'], sep=", ")
