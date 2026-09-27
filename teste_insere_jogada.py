def insere_jogada(mat_tabuleiro,lin:int, col:int,jogador:str):
    if mat_tabuleiro[lin][col] is not None:
        print("Posição oculpada! Tente outra casa.")
        return None
    else:
        mat_tabuleiro[lin][col] = jogador
        return mat_tabuleiro


tabuleiro: list[list[str]] = [[None for col in range(3)]for lin in range(3)]