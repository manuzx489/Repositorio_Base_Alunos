# Crie um programa que receba um número inteiro e dia qual é o dia da semana correspondente a este número
# Os dias são:
# 1 - domingo
# 2 - Segunda
# 3 - Terça
# 4 - Quarta
# 5 - Quinta
# 6 - Sexta
# 7 - Sábado

# OUTPUT ESPERADO

# Digite um número: 1
# Domingo

# Digite um número: 2
# Segunda

# Digite um número: 8
# Número errado

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

n1 = int(input("Digite um número: "))
if n1 == 1:
    print("domigo")
elif n1 == 2:
    print("segunda")
elif n1 == 3:
    print("terça")
elif n1 == 4:
    print("quarta")
elif n1 == 5:
    print("quinta")
elif n1 == 6:
    print("sexta")
elif n1 == 7:
    print("sabádo")
else:
    print("digite um número de 1 a 7")