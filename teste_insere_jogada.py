def insere_jogada(mat_tabuleiro,lin:int, col:int,jogador:str):
    if mat_tabuleiro[lin][col] is not None:
        print("Posição oculpada! Tente outra casa.")
        return False

    mat_tabuleiro[lin][col] = jogador
    return True

def desenha_tabuleiro(mat_tabuleiro):
    print("    [0] [1] [2]")
    for lin in range(3):
        print(f"[{lin}]", end=" ")
        for col in range(3):
            print(f"[{'-' if mat_tabuleiro[lin][col] is None else mat_tabuleiro[lin][col]}]", end=" ")
        print()


tabuleiro: list[list[str]] = [[None for col in range(3)]for lin in range(3)]

desenha_tabuleiro(tabuleiro)

lin = int(input("Informe a linha que quer jogar: "))
col = int(input("Informe a coluna que quer jogar: "))


if insere_jogada(tabuleiro, lin, col, 'X'):
    # Jogada Realizada
    print("Jogada Realiza")
else:
    # Jogada inválida
    print("Jogada inválida")

desenha_tabuleiro(tabuleiro)