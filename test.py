# grades = int(input("Insira o número de notas: "))
# gradesList = []
# i = 0

# while i < grades:
#     gradesList.append(float(input("Insira a nota: ")))
#     i += 1

# media = sum(gradesList)/len(gradesList)
# print(media)


# gradesList0 = [10.0, 8.8, 8.3, 7.0, 9.4]
# for grades in gradesList0:
#     print(grades)

# listNum = [-25, 39, 0, 43.0, -423, -4234, 75, 352.52, -34, 52, 523, 546, 75, 3, 7, -53, 52]
# listPos = []
# listNeg = []
# for item in listNum:
#     if item >= 0:
#         listPos.append(item)
#     else:
#         listNeg.append(item)
# print(f"Números positivos da lista: {listPos}\nNúmeros negativos da lista: {listNeg}")


# listNum = [-25, 39, 0, 43.0, -423, -4234, 75, 352.52, -34, 52, 523, 546, 75, 3, 7, -53, 52]
# listPos = []
# listNeg = []
# listNeu = []
# for item in listNum:
#     if (item >= 0):
#         listPos.append(item)
#     elif (item == 0):
#         listNeu.append(item)
#     else:
#         listNeg.append(item)

# print(f"Números positivos da lista: {listPos}\nNúmeros negativos da lista: {listNeg}\nNúmeros neutros: {listNeu}")

# listNum = [25, 39, 0, 43.0, -423, -4234, 75, 352.52, -34, 52, 523, 546, 75, 3, 7, -53, 52]
# listPos = []
# listNeu = []
# listNeg = []
# num = 0
# for item in listNum:
#     if (item < 0):
#         num = item
#         print(f"Número negativo encontrado: {num}\nÍndice do número: {listNum.index(item)}")
#         listNeg.append(item)
#         break
#     elif (item > 0):
#         listPos.append(item)
#     else:
#         listNeu.append(item)
# print(f"\nNúmeros positivos da lista: {listPos}\nNúmeros negativos da lista: {listNeg}\nNúmeros neutros: {listNeu}")

list010 = [23, 41, 53.5, -342, 42, -52, -2, 0, 42, -5]
listDouble = []

for item in list010:
    listDouble.append(item*2)
print(listDouble)