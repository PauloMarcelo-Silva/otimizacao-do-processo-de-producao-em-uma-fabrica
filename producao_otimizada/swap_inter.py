from avaliar_e_aplicar_troca import avaliar_e_aplicar_troca

def swap_inter(fabrica):
    melhor_l = -1
    melhor_custo = fabrica.custo_tempo
    melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    for linha1 in range(fabrica.num_linhas):
        for linha2 in range(linha1 + 1, fabrica.num_linhas):
            for pos1 in range(len(fabrica.linha_producao[linha1])):
                for pos2 in range(len(fabrica.linha_producao[linha2])):
                    if avaliar_e_aplicar_troca(fabrica, linha1, pos1, linha2, pos2):
                        melhor_custo = fabrica.custo_tempo
                        melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    if melhor_l != -1:
        fabrica.linha_producao = melhor_linha_producao
        fabrica.custo_tempo = melhor_custo
