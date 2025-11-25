# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista
qt_filmes = int(input("Quantos filmes vc deseja coloca na lista?"))
# LOOP WHILE
cont = 1 
while cont <= 2:
    nome = input(f"Digite o nome do {cont} filme: ")
    filmes.append(nome)
    cont = cont + 1
print(filmes)





# LOOP FOR

for n in range(1, qt_filmes+1):
    print(n)