nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

idade = int(input("Por favor, Nos diga sua idade:  "))
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")


altura = float(input("Digite sua altura em metros: "))
if altura <= 1.5:
    print("Você é considerado baixo.")
else:
    print("Você é considerado alto.")


peso = float(input("Digite seu peso em kg: "))
if peso <= 60:
    print("Você está abaixo do peso ideal.")
else:
    print("Você está acima do peso ideal.")

informações = input("você quer saber suas informações? (sim/não): ")
if informações == "sim":
    print(f"Seu nome é: {nome}, Idade: {idade}, Altura: {altura}m, Peso: {peso}kg")
else:
    print("Ok, não vou mostrar suas informações.")
print("Obrigado por usar o programa!")
# Fim do programa