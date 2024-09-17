def numero_de_iteracoes():
    while True:
        try:
            Iteracoes = int(input("Digite o numero de iteracoes da sequencia: "))
            break
        except ValueError:
            print("Por favor, insira somente numeros")
            continue
    return Iteracoes


def numero_inicial():
    while True:
        try:
            numero = int(input("Insira o numero inicial da sequencia: "))
            break
        except ValueError:
            print("Por favor, insira somente numeros")
            continue
    return numero

def sequencia(Iteracoes, numeros):
    while Iteracoes>len(numeros):
        numeros.append(numeros[-1] + numeros[-2])
    return numeros


Iteracoes = numero_de_iteracoes()
numeros = []
numeros.append(0)
numeros.append(numero_inicial())
numeros = sequencia(Iteracoes, numeros)


print(numeros)


