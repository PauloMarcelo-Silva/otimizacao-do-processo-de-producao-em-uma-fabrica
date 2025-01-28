from vnd import vnd
from perturbacao import perturbacao

def ils(fabrica, num_iter=100):
    melhor_custo = fabrica.custo_tempo
    melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

    for _ in range(num_iter):
        vnd(fabrica)

        if fabrica.custo_tempo < melhor_custo:
            melhor_custo = fabrica.custo_tempo
            melhor_linha_producao = [linha[:] for linha in fabrica.linha_producao]

        perturbacao(fabrica)

    fabrica.linha_producao = melhor_linha_producao
    fabrica.custo_tempo = melhor_custo
