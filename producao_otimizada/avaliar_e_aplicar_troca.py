# avaliar_e_aplicar_troca.py
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
