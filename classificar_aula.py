# IA Classificadora de Comentários

palavras_positivas = [
    "excelente",
    "ótima",
    "ótimo",
    "interessante",
]

palavras_negativas = [
    "ruim",
    "péssima",
    "péssimo",
    "difícil",
]

def classificar(frase):
    frase = frase.lower()

    pontos_positivos = 0
    pontos_negativos = 0

    # Verifica palavras positivas
    for palavra in palavras_positivas:
        if palavra in frase:
            pontos_positivos += 1

    # Verifica palavras negativas
    for palavra in palavras_negativas:
        if palavra in frase:
            pontos_negativos += 1

    # Classificação
    if pontos_positivos > pontos_negativos:
        return "Positivo"

    elif pontos_negativos > pontos_positivos:
        return "Negativo"

    else:
        return "Neutro"


# Programa principal

print("=== IA Classificadora de Comentários ===")
print("Digite um comentário sobre a aula.")
print("Digite 'sair' para encerrar.\n")

while True:

    frase = input("Comentário: ")

    if frase.lower() == "sair":
        print("Programa encerrado.")
        break

    resultado = classificar(frase)

    print("Segundo seu comentário, a classificação é:", resultado)
    print()