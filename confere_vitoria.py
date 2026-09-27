def verifica_vitoria(tabuleiro, peca_jogador):
    n = len(tabuleiro)        

    # Estrutura para acumluar as contagens
    cont_linhas = [0] * n        # Guarda a contagem do elemento por linha
    cont_colunas = [0] * n       # Guarda a contagem do elemento por coluna
    diag_principal = 0           # Guarda a contagem da diagonal principal
    diag_secundaria = 0          # Guarda a contagem da diagonal secundaria

    # Único loop para percorrer a matriz uma única vez
    for lin in range(n):
        for col in range(n):
            if tabuleiro[lin][col] == peca_jogador:
                # Atualiza a linha atual
                cont_linhas[lin] += 1

                # Atualiza a coluna atual
                cont_colunas[col] +=1

                # Verifica se está na diagonal principal (lin == col)
                if lin == col:
                    diag_principal += 1

                # Verifica se está na diagonal secundária (lin + col == n-1)
                if lin + col == n -1:
                    diag_secundaria += 1
                    
    return cont_linhas, cont_colunas, diag_principal,  diag_secundaria


tabuleiro = [
    ['X', 'X', 'X'],
    ['O', 'O', 'X'],
    ['O', 'X', 'O']
]

linhas, colunas, d_principal, d_secundaria = verifica_vitoria(tabuleiro, 'X')

print(f"Ocorrências por linha: {linhas}")
print(f"Ocorrência por coluna: {colunas}")
print(f"Diagonal principal: {d_principal}")
print(f"Diagonal Secundária: {d_secundaria}")