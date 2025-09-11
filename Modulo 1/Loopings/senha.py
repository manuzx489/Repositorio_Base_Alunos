senha_correta = "manu130509"
senha = input("Digite a senha correta: ")

while senha != senha_correta:
    print("senha incorreta,tente novamente!")
    senha = input("Digite sua senha: ")
print("senha correta acessa liberado!")