Palavra = "wellington"
letter = []
Chances = 6
Ganhou = False

while True:
    Tentativa = input("Digite uma letra: ").lower()
    for letter in Palavra:
        if Tentativa in letter:
            print(letter, end= " ")
        else:
            print("_", end = " ")
    if Tentativa.lower() not in Palavra:
        Chances -= 1
        print(f"Você possui {Chances} chances restantes.")
    break
    if Chances == 0:
        break
if Ganhou:
    print(f"Você ganhou! A palavra é {Palavra}.")