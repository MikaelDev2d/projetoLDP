operador = input("Seu operador é (adição +), (subtração -), (multiplicação *) ou (divisão /)?  ")
if operador != "+" and operador != "-" and operador != "/" and operador != "*":
    print("Ainda não aprendi esse operador!...")
    exit()
else:
 parte1 = int(input("Qual é seu primeiro número?:   "))
 parte2 = int(input("Qual é seu segundo número?:   "))
    
if operador == "+":
    parte1 + parte2
    print((parte1)+(parte2))
elif operador == "-":
    parte1 - parte2
    print((parte1)-(parte2))
elif operador == "/":
    parte1 / parte2
    print((parte1)/(parte2))
elif operador == "*":
    parte1 * parte2
    print((parte1)*(parte2))
