import random
import re


def obter_tamanho_matriz():
    while True:
        try:
            linhas = int(input("Digite o número de linhas da matriz (mínimo 5): "))
            colunas = int(input("Digite o número de colunas da matriz (mínimo 5): "))

            if linhas >= 5 and colunas >= 5:
                print(f"Tamanho da matriz escolhido: {linhas}x{colunas}")
                return linhas, colunas
            else:
                print("O tamanho mínimo da matriz é 5x5. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números inteiros.")


def gerar_expressao_aleatoria():
    caracteres = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tipos = ["*", "+", "?", "{1,3}"]  # Repetições comuns em regex
    estruturas = [
        f"{random.choice(caracteres)}{random.choice(tipos)}",
        f"[{random.choice(caracteres)}{random.choice(caracteres)}]{random.choice(tipos)}",
        f"({random.choice(caracteres)}{random.choice(caracteres)}){random.choice(tipos)}",
    ]
    return random.choice(estruturas)


def gerar_expressoes(linhas, colunas):
    expressoes = {"linha": [], "coluna": []}

    for _ in range(linhas):
        expressoes["linha"].append(gerar_expressao_aleatoria())
    for _ in range(colunas):
        expressoes["coluna"].append(gerar_expressao_aleatoria())

    return expressoes


def inicializar_matriz(linhas, colunas):
    return [["_" for _ in range(colunas)] for _ in range(linhas)]


def imprimir_matriz(matriz, expressoes):
    colunas = len(matriz[0])
    linhas = len(matriz)

    # Imprime as expressões das colunas
    print("    " + "  ".join(f"{expr:^6}" for expr in expressoes["coluna"]))

    # Imprime linha de separação
    print("    " + "+".join(["-" * 6 for _ in range(colunas)]))

    # Imprime a matriz com expressões de linha
    for i, linha in enumerate(matriz):
        print(
            f'{expressoes["linha"][i]:<4}| '
            + " | ".join(f"{cell:^4}" for cell in linha)
            + " |"
        )

        if i < linhas - 1:
            print("    " + "+".join(["-" * 6 for _ in range(colunas)]))

    # Linha final de fechamento
    print("    " + "+".join(["-" * 6 for _ in range(colunas)]))


def atualizar_matriz(matriz, expressoes, linhas, colunas):
    while True:
        try:
            linha = (
                int(
                    input("Digite o número da linha para atualizar (ou -1 para sair): ")
                )
                - 1
            )
            if linha == -1:
                break
            coluna = int(input("Digite o número da coluna para atualizar: ")) - 1
            valor = input("Digite o valor a ser inserido na matriz: ").upper()

            if 0 <= linha < linhas and 0 <= coluna < colunas:
                matriz[linha][coluna] = valor
                imprimir_matriz(matriz, expressoes)
            else:
                print("Índices de linha ou coluna fora do intervalo.")
        except ValueError:
            print("Por favor, digite números inteiros válidos.")


def main():
    linhas, colunas = obter_tamanho_matriz()
    expressoes = gerar_expressoes(linhas, colunas)
    matriz = inicializar_matriz(linhas, colunas)

    imprimir_matriz(matriz, expressoes)
    atualizar_matriz(matriz, expressoes, linhas, colunas)


if __name__ == "__main__":
    main()
