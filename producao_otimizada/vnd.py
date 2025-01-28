from swap_intra import swap_intra
from swap_inter import swap_inter

def vnd(fabrica):
    melhor_custo = fabrica.custo_tempo
    melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    custo_anterior = fabrica.custo_tempo

    while True:
        swap_intra(fabrica)
        if fabrica.custo_tempo < melhor_custo:
            melhor_custo = fabrica.custo_tempo
            melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]
        else:
            fabrica.linha_producao = melhor_linha_producao
            fabrica.custo_tempo = melhor_custo

        swap_inter(fabrica)
        if fabrica.custo_tempo < melhor_custo:
            melhor_custo = fabrica.custo_tempo
            melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]
        else:
            fabrica.linha_producao = melhor_linha_producao
            fabrica.custo_tempo = melhor_custo
            break
