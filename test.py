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

# list010 = [23, 41, 53.5, -342, 42, -52, -2, 0, 42, -5]
# listDouble = []

# for item in list010:
#     listDouble.append(item*2)
# print(listDouble)

# listGrades = []

# Problema gerador: Criar uma calculadora em Python
respostaSim = ["sim", "Sim", "SIM", "s", "S", "siM", "sIm", "sIM", "SIm", "SiM"]
respostaNao = ["nao", "Nao", "NAO", "n", "N", "naO", "nAo", "nAO", "NAo", "NaO", "não", "Não", "NãO", "NÃo"]
comecar = ""
comecar = input("\n    Instruções Calculadora Python*    \n\nPara calcular digite primeiro a operação que deseja realizar e depois dois números. Após a primeira operação o resultado fica salvo, você pode zerá-lo com a opção de numeral '0' ou continuar calculando selecionando uma operação. Entendeu?\n\nDigite: sim ou nao: ")
while (comecar):
    if (comecar == respostaSim[i]):
        print("Ok")
    elif (comecar == respostaNao[i]):
        print("Leia atentamente as instruções!")
        break




# while (comecar != "sim") or (comecar != "Sim") or (comecar != "SIM")or (comecar != "S") or (comecar != "s") or (comecar != "SIm") or (comecar != "SiM") or (comecar != "sIM") or (comecar != "sIM"):
#     if (comecar == "sim") or (comecar == "Sim") or (comecar == "SIM")or (comecar == "S") or (comecar == "s") or (comecar == "SIm") or (comecar == "SiM") or (comecar == "sIM") or (comecar == "sIM"):
#         i = 0
#         print("~"*25)
#         print("  Calculadora em Python")
#         print("~"*25)
#         print("Operações:\n  0- Zerar\n  1-  Soma\n  2-  Subtração\n  3-  Multiplicação\n  4-  Divisão\n  5-  Exponenciação\n  6-  Resto\n  7-  Parte inteira\n  8-  Paridade\n  9-  Módulo\n 10-  Sair")
#         print("~"*25)
#         while i > 5:
#             if (i == 1):
#                 print("oi")
#     elif (comecar == "nao") or (comecar == "Nao") or (comecar == "NAO")or (comecar == "N") or (comecar == "n") or (comecar == "Nao") or (comecar == "NaO") or (comecar == "nAO") or (comecar == "nAo") or (comecar == "não") or (comecar == "Não") or (comecar == "NÂO"):
#         print("Leia atentamente as instruções!")
#     else:
#         print("Insira uma resposta válida.")
