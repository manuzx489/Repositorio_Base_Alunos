carro = input("qual foi o modelo do carro alugado?")
dias = float (input("por quantos dias o carro foi alugado:"))
km = float(input("quantos km o carro rodou:"))

if carro == "bmw":
    diaria = 600

elif carro == "toyota":
    diaria = 900

elif carro == "mustang":
    diaria = 1000

else:
    diaria = 60

total_dias = (dias * diaria)
total_km =(km * 0.15)
resultado = total_dias + total_km
print(f"vc andou {km} km por {dias} dias,então o preço a pagar é:{resultado}")