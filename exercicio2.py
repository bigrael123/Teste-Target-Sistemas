palavra = input("Digite uma palara e veja quantos As ela tem: ")
numero_de_as = 0
for letters in palavra:
    if (letters == "A" or letters == "a"):
        numero_de_as+=1
print(numero_de_as)