from avaliar_e_aplicar_troca import avaliar_e_aplicar_troca

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
