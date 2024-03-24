secret_number = 777

print(
"""
+===================================+
| Bem vindo ao meu jogo, trouxa!    |
| Insira um número inteiro          |
| e adivinhar o número que tenho    |
| escolhidos para você.             |
| Então, qual é o número secreto?   |
+===================================+
""")

numero = int(input("Digite o número: "))

while numero != secret_number:
    print("Ha ha! Você está preso no meu loop!")
    
    if numero == secret_number:
        print("Muito bem, trouxa! Você está livre agora.")
        
    numero = int(input("Digite um novo número: "))


palavra_secreta = "chupacabra"

print(
"""
+===================================+
| Bem vindo ao meu jogo, humano!    |
| Insira uma palavra                |
| e adivinhe o apelido que tenho    |
| escolhido  para você.             |
| Então, qual é a palavra secreta?  |
+===================================+
""")

palavra = input("Qual é a palavra secreta? ")

while palavra != palavra_secreta:
    break
    
if palavra == palavra_secreta:
    print("Você saiu do loop com sucesso")

palavra = input("Qual é a palavra secreta? ")

