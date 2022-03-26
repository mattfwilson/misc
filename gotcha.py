def createStudent(name, age, grades=[]):
    return { "name": name, "age": age, "grades": grades }

matt = createStudent('Matt', 35)
janelle = createStudent('Janelle', 33)

print(matt)
print(janelle)