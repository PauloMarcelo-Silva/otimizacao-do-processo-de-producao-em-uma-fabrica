def swap_intra(fabrica):
    melhor_l = -1
    melhor_custo = fabrica.custo_tempo
    melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    for linha in range(fabrica.num_linhas):
        for pos1 in range(len(fabrica.linha_producao[linha]) - 1):
            for pos2 in range(pos1 + 1, len(fabrica.linha_producao[linha])):
                if avaliar_e_aplicar_troca(fabrica, linha, pos1, linha, pos2):
                    melhor_custo = fabrica.custo_tempo
                    melhor_l = linha
                    melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    if melhor_l != -1:
        fabrica.linha_producao = melhor_linha_producao
        fabrica.custo_tempo = melhor_custo

def avaliar_e_aplicar_troca(fabrica, linha1, pos1, linha2, pos2):
    produto1 = fabrica.linha_producao[linha1][pos1]
    produto2 = fabrica.linha_producao[linha2][pos2]
    
    fabrica.linha_producao[linha1][pos1] = produto2
    fabrica.linha_producao[linha2][pos2] = produto1
    
    custo_linha = 0
    for i in range(fabrica.num_linhas):
        tempo_linha = 0
        for k in range(len(fabrica.linha_producao[i])):
            produto_ant = fabrica.linha_producao[i][k]
            tempo_linha += fabrica.tempos[produto_ant - 1]
            if k > 0:
                produto_atual = fabrica.linha_producao[i][k - 1]
                tempo_linha += fabrica.preparos[produto_atual - 1][produto_ant - 1]

        if tempo_linha > custo_linha:
            custo_linha = tempo_linha

    if custo_linha < fabrica.custo_tempo:
        fabrica.custo_tempo = custo_linha
        return True
    else:
        fabrica.linha_producao[linha1][pos1] = produto1
        fabrica.linha_producao[linha2][pos2] = produto2
        return False
