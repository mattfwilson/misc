def createStudent(name, age, grades=[]):
    return { "name": name, "age": age, "grades": grades }

def addGrade(student, grade):
    student['grades'].append(grade)
    print(student['grades'])

matt = createStudent('Matt', 35)
janelle = createStudent('Janelle', 33)

print(matt)
print(janelle)

addGrade("Matt", 90)
addGrade("Janelle", 100)