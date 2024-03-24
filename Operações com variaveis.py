numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

maior_numero = numero1

if numero2 > numero1: maior_numero = numero2

if numero3 > numero2: maior_numero = numero3

print("O maior número é o: ", maior_numero)
