nome = input("qual é o seu nome?")
print("Uau!", nome, "é um nome super legal!")

idade = input("Digite sua idade aqui: ")
if int(idade) >= 18:
    print("Você é maior de idade!")
else:
    print("você é de menor!")

#primeiras informaçôes acima.

quer_desafio = input("você quer um desafio? (s/n): ")

#desafio aceito ou não abaixo.

if quer_desafio == "s":
    resposta = input("Qual é a montanha mais alta do planeta? ")
    if resposta == "MonteEverest":
      print("Você acertou!")
    else:
      print("Você errou!")
if quer_desafio == "n":
      print("talvez na próxima!")