# Calcule a média das notas utilizando um loop while e também um loop for


# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

notas = ['9.5', '10', '6.75', '5.5']

# LOOP WHILE
# cont = 0
# soma = 0
# while cont <= 3 :
#     nota = float(notas[cont])
#     soma = soma + nota 
#     cont = cont + 1

#     media = soma / 4
#     print (media)




# LOOP FOR

soma = 0 
for nota in notas :
    soma = soma + float(nota)
    print(nota)

media = soma /4
print(media)