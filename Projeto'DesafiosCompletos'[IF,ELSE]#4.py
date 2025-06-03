nome = input("Qual é o seu nome? ")
idade = int(input(f"Qual é a sua idade? "))
if not nome or not idade:
    print("Por favor, preencha todos os campos.")
    exit()

print(f"Olá {nome}, você tem {idade} anos.")
desafio = input("Você quer fazer um desafio? (s/n) ")

if desafio == "s":
    resposta = input("Desafio aceito! Qual é o nome da linha invisivel que não existe e passa pelo mundo?: ")
    if resposta == "Linha do Equador":
      print("Resposta correta!")
      print("Parabéns, você ganhou um prêmio!")
      print("Obrigado por participar!")
      print("Fim do programa.")
      exit()
    else:
      print("Resposta incorreta.")
      print("Você não ganhou o prêmio, mas obrigado por participar!")
      print("Fim do programa.")
      exit()
elif desafio == "n":
    print("Tudo bem, você não precisa fazer o desafio.")
    print("Obrigado por participar!")
    print("Fim do programa.")
    exit()

