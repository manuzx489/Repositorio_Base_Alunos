from colorama import init, Fore
init(autoreset=True)

print("| ------------------------- |")
print("| SISTEMA DE PROVAS")
print("| ------------------------- |")
nome = input("| Nome do aluno: ")
nota = float(input("| Nota da primeira prova: "))
nota2 =float(input("| Nota da segunta prova: "))
nota3 =float(input("| Nota da terceira prova: "))
print("| ------------------------- |")
provas = nota + nota2 + (nota3/2)
if provas >= 5:
    print(Fore.GREEN+f"| aluno {nome} aprovado")
elif provas <5:
    print(Fore.RED+f"| aluno {nome} reprovado")
print("| ------------------------- |")
