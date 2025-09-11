from colorama import init, Fore
init(autoreset=True)
print("|---------------------------------|")
print("| Calculadora")
print("|---------------------------------|")
print("| 1 - Soma ")
print("| 2 - Subtração ")
print("| 3 - Multiplicação ")
print("| 4 - Divisão ")
print("|---------------------------------|")
opcao = int(input("| Escolha uma das opções: "))
n1 = float(input("| Digite o primeiro número: "))
n2 = float(input("| Digite o segundo número: "))


if opcao == 1:
    print("o resultado é:",n1+n2)

elif opcao == 2:
    print("o resultado é:",n1-n2)

elif opcao == 3:
    print("o resultado é:",n1 * n2)

elif opcao == 4:
    print("o resultado é:",n1 / n2)

else:
    print(Fore.RED+"|escolha uma opção do menu")

  
