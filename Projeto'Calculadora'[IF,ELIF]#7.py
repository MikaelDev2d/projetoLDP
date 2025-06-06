operador = input("Seu operador é (adição +), (subtração -) ou (divisão /)?  ")
parte1 = int(input("Qual é seu primeiro número?:   "))
parte2 = int(input("Qual é seu segundo número?:   "))

if operador == "+" or "adição":
    parte1 + parte2
    print((parte1)+(parte2))

elif operador == "-" or "subtração":
    parte1 - parte2
    print((parte1)-(parte2))

elif operador == "/" or "divisão":
    parte1 / parte2
    print((parte1)/(parte2))

else:
    print("Opa! Eu ainda não sei fazer essa conta com esse operador :( ")
    exit()

    