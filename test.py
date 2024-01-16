grades = int(input("Insira o número de notas: "))
gradesList = []
i = 0

while i < grades:
    gradesList.append(float(input("Insira a nota: ")))
    i += 1

media = sum(gradesList)/len(gradesList)
print(media)