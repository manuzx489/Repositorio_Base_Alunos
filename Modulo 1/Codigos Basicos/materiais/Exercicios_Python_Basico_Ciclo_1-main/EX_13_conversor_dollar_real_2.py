# Atualize o código do exercício de conversor de dollar para real. Agora um "MENU" de opções aparecerá na tela pedindo ao usuário que escolha se quer converter
# de Reais para Dollar ou Dollar para reais. O usuário deve digitar a opção antes de informar os valores.

# OUTPUT ESPERADO:

#------- Exemplo 1 (Dólares para Reais):

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 1
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de dólares: 150 
# O valor em reais é R$847.50

#---------- Exemplo 2 (Reais para Dólares)

# Escolha uma opção: 
# 1 - Dollar para Real
# 2 - Real para dollar
# Digite a opção: 2
# Informe a cotação atual do Dollar: 5.65
# Informe a quantidade de reais: 150
# O valor em dólares é $26.55

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("Escolha uma opção: ")
print("1 - Dollar para real")
print("2 - Real para dollar")
opcao = int(input("Digite a opção: "))
dollar = float(input("Informe a cotação atual em dollar: "))
reais = float(input("Informe a quantidade de dólares: "))
if opcao == 1:
    print(f"o valor em dólares é R${dollar*reais}")
elif opcao == 2:
    print(f"o valor em reias é R${reais/dollar:.2f}")
else:
    print("Escolha um do menu")


