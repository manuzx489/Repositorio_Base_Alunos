# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("| ____________________________ |")
print("| SISTEMA DE PROVAS")
print("|_____________________________ |")
nome = input("| Nome do aluno: ")
no1 = float(input("| Nota da primeira prova: "))
no2 = float(input("| Nota da segunda prova: "))
no3 = float(input("| Nota da terceira prova: "))
print("| ____________________________ |")
soma = no1 + no2 + no3
media = soma/3
input(f"| Aluno: {nome}")
input(f"| Média: {media:.2f}")
if media >=5:
    print("| Aluno aprovado")
else:
    print("| Aluno reprovado")
print("| ____________________________ |")